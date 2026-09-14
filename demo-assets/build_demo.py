"""Render demo-assets/beats.json into a demo video with real narration.

Reuses the Continuity Check pipeline (macOS `say` narration + ffmpeg card
rendering, no human voice, no puppeteer) -- see agentic-cinema-hackathon's
demo-assets for the prior art this generalizes from.

Usage:
    python3 demo-assets/build_demo.py
Output:
    demo-assets/grant-scout-demo.mp4
    demo-assets/grant-scout-demo.srt
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
WORK = ROOT / "work"
WORK.mkdir(exist_ok=True)

SANS_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO = "/System/Library/Fonts/Supplemental/Andale Mono.ttf"

W, H = 1280, 720
VOICE = "Samantha"

# ffmpeg on this machine (homebrew, no libfreetype) has no drawtext filter --
# same gap Continuity Check hit. Render frames as PNGs with Pillow instead
# and feed ffmpeg a still image + audio (like a title card), no drawtext.


def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("CMD FAILED:", " ".join(cmd), file=sys.stderr)
        print(r.stderr, file=sys.stderr)
        raise SystemExit(1)


def synth_narration(beat_id: str, text: str) -> tuple[Path, float]:
    aiff = WORK / f"{beat_id}.aiff"
    wav = WORK / f"{beat_id}.wav"
    run(["say", "-v", VOICE, "-o", str(aiff), text])
    run(["ffmpeg", "-y", "-i", str(aiff), "-ar", "44100", str(wav)])
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(wav)],
        capture_output=True, text=True,
    )
    return wav, float(r.stdout.strip())


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def draw_multiline(draw: ImageDraw.ImageDraw, xy, text: str, font, fill, spacing: int, anchor_center_x: int | None = None):
    y = xy[1]
    for line in text.split("\n"):
        w = draw.textlength(line, font=font)
        x = (anchor_center_x - w / 2) if anchor_center_x is not None else xy[0]
        draw.text((x, y), line, font=font, fill=fill)
        bbox = font.getbbox(line) or (0, 0, 0, font.size)
        y += (bbox[3] - bbox[1]) + spacing


def render_card(beat: dict, duration: float, audio: Path, out: Path) -> None:
    bg = hex_rgb(beat.get("bg", "#0d1117"))
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(SANS_BOLD, 56)
    sub_font = ImageFont.truetype(SANS, 28)
    draw_multiline(d, (0, H // 2 - 140), beat["title"], title_font, (255, 255, 255), 18, anchor_center_x=W // 2)
    draw_multiline(d, (0, H // 2 - 10), beat.get("sub", ""), sub_font, (201, 209, 217), 14, anchor_center_x=W // 2)
    png = WORK / f"{beat['id']}.png"
    img.save(png)
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(audio),
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
        str(out),
    ])


def render_screen(beat: dict, duration: float, audio: Path, out: Path) -> None:
    img = Image.new("RGB", (W, H), (1, 4, 9))
    d = ImageDraw.Draw(img)
    mono_font = ImageFont.truetype(MONO, 26)
    body_font = ImageFont.truetype(MONO, 24)
    d.text((60, 60), beat["prompt"], font=mono_font, fill=(63, 185, 80))
    draw_multiline(d, (60, 130), beat["body"], body_font, (230, 237, 243), 12)
    png = WORK / f"{beat['id']}.png"
    img.save(png)
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(audio),
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
        str(out),
    ])


def main() -> None:
    beats = json.loads((ROOT / "beats.json").read_text())
    segment_paths: list[Path] = []
    srt_lines: list[str] = []
    t = 0.0
    for i, beat in enumerate(beats, 1):
        wav, vo_dur = synth_narration(beat["id"], beat["vo"])
        duration = round(vo_dur + 0.8, 2)
        seg = WORK / f"{beat['id']}.mp4"
        if beat["kind"] == "card":
            render_card(beat, duration, wav, seg)
        else:
            render_screen(beat, duration, wav, seg)
        segment_paths.append(seg)

        start = t
        end = t + duration
        srt_lines.append(str(i))
        srt_lines.append(f"{fmt_ts(start)} --> {fmt_ts(end)}")
        srt_lines.append(beat["vo"])
        srt_lines.append("")
        t = end
        print(f"[{i}/{len(beats)}] {beat['id']}: {duration}s (running total {t:.1f}s)")

    concat_file = WORK / "concat.txt"
    concat_file.write_text("\n".join(f"file '{p}'" for p in segment_paths))
    out_mp4 = ROOT / "grant-scout-demo.mp4"
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", str(out_mp4),
    ])
    (ROOT / "grant-scout-demo.srt").write_text("\n".join(srt_lines))
    print(f"\nDONE. Total runtime: {t:.1f}s -> {out_mp4}")


def fmt_ts(sec: float) -> str:
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    ms = int(round((sec - int(sec)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


if __name__ == "__main__":
    main()
