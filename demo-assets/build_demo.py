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
    return wav, ffprobe_duration(wav)


def hex_rgb(h: str) -> tuple[int, int, int]:
    stripped = h.lstrip("#")
    if len(stripped) != 6:
        raise ValueError(f"bg color {h!r} must be a 6-hex-digit color like '#0d1117'")
    try:
        r, g, b = (int(stripped[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError as exc:
        raise ValueError(f"bg color {h!r} is not valid hex") from exc
    return r, g, b


def png_to_segment(png: Path, audio: Path, duration: float, out: Path) -> None:
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(audio),
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
        str(out),
    ])


def draw_multiline(draw: ImageDraw.ImageDraw, xy, text: str, font, fill, spacing: int, anchor_center_x: int | None = None):
    y = xy[1]
    for line in text.split("\n"):
        w = draw.textlength(line, font=font)
        x = (anchor_center_x - w / 2) if anchor_center_x is not None else xy[0]
        draw.text((x, y), line, font=font, fill=fill)
        bbox = font.getbbox(line) or (0, 0, 0, font.size)
        y += (bbox[3] - bbox[1]) + spacing


def cover_resize(src: Image.Image, w: int, h: int) -> Image.Image:
    sw, sh = src.size
    scale = max(w / sw, h / sh)
    nw, nh = round(sw * scale), round(sh * scale)
    src = src.resize((nw, nh), Image.LANCZOS)
    left = (nw - w) // 2
    top = (nh - h) // 2
    return src.crop((left, top, left + w, top + h))


def render_card(beat: dict, duration: float, audio: Path, out: Path) -> None:
    art = beat.get("img")
    if art:
        base = cover_resize(Image.open(ROOT / "art" / art).convert("RGB"), W, H)
        # bottom caption panel: fades in over fade_h, then flat-opaque so text
        # never sits on a half-transparent, hard-to-read strip
        panel_h, fade_h, max_alpha = 320, 90, 235
        gradient = Image.new("L", (1, panel_h), max_alpha)
        for y in range(fade_h):
            gradient.putpixel((0, y), int(max_alpha * (y / fade_h)))
        gradient = gradient.resize((W, panel_h))
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        black = Image.new("RGBA", (W, panel_h), (5, 6, 8, 255))
        black.putalpha(gradient)
        overlay.paste(black, (0, H - panel_h), black)
        img = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
    else:
        bg = hex_rgb(beat.get("bg", "#0d1117"))
        img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(SANS_BOLD, 56 if not art else 42)
    sub_font = ImageFont.truetype(SANS, 28 if not art else 22)
    if art:
        draw_multiline(d, (60, H - 210), beat["title"], title_font, (255, 255, 255), 12)
        draw_multiline(d, (60, H - 210 + 62), beat.get("sub", ""), sub_font, (216, 222, 228), 10)
    else:
        draw_multiline(d, (0, H // 2 - 140), beat["title"], title_font, (255, 255, 255), 18, anchor_center_x=W // 2)
        draw_multiline(d, (0, H // 2 - 10), beat.get("sub", ""), sub_font, (201, 209, 217), 14, anchor_center_x=W // 2)
    png = WORK / f"{beat['id']}.png"
    img.save(png)
    png_to_segment(png, audio, duration, out)


def render_screen(beat: dict, duration: float, audio: Path, out: Path) -> None:
    img = Image.new("RGB", (W, H), (1, 4, 9))
    d = ImageDraw.Draw(img)
    mono_font = ImageFont.truetype(MONO, 26)
    body_font = ImageFont.truetype(MONO, 24)
    d.text((60, 60), beat["prompt"], font=mono_font, fill=(63, 185, 80))
    draw_multiline(d, (60, 130), beat["body"], body_font, (230, 237, 243), 12)
    png = WORK / f"{beat['id']}.png"
    img.save(png)
    png_to_segment(png, audio, duration, out)


def ffprobe_duration(path: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or not r.stdout.strip():
        raise SystemExit(f"FAIL: ffprobe couldn't read a duration from {path} -- "
                          f"{r.stderr.strip() or 'empty output'}")
    return float(r.stdout.strip())


DRIFT_TOLERANCE_S = 0.1


def measure_drift(segment_paths: list[Path], expected_durations: list[float]) -> list[float]:
    """Real per-segment ffprobe of every rendered file. AAC encoding can add
    priming/padding samples per segment, and `-c copy` concat carries that
    forward uncorrected -- checking only the final file's aggregate duration
    can look fine while individual segments (and therefore captions built
    from *expected* durations) are off. Returns each segment's actual
    duration; the caller builds the SRT from these, not from what was asked
    for, so caption sync is exact regardless of encoder padding."""
    actuals = []
    for seg, expected in zip(segment_paths, expected_durations, strict=True):
        actual = ffprobe_duration(seg)
        drift = abs(actual - expected)
        actuals.append(actual)
        if drift > 0.05:
            print(f"  drift {seg.name}: expected {expected:.2f}s, actual {actual:.2f}s "
                  f"({drift * 1000:.0f}ms)", file=sys.stderr)
        if drift > DRIFT_TOLERANCE_S:
            # A drift this large isn't encoder padding, it's a rendering
            # failure (e.g. `say` producing near-empty audio) -- a build
            # that can't fail on this isn't actually verifying anything.
            raise SystemExit(
                f"FAIL: {seg.name} drifted {drift * 1000:.0f}ms from expected "
                f"({DRIFT_TOLERANCE_S * 1000:.0f}ms tolerance) -- rendering is "
                f"broken, not just padded; fix before shipping this build."
            )
    return actuals


def build_srt(beats: list[dict], actual_durations: list[float]) -> str:
    """Cumulative timeline from measured segment durations, not the durations
    that were requested -- captions land on what the video actually plays."""
    lines: list[str] = []
    t = 0.0
    for i, (beat, duration) in enumerate(zip(beats, actual_durations, strict=True), 1):
        start, end = t, t + duration
        lines += [str(i), f"{fmt_ts(start)} --> {fmt_ts(end)}", beat["vo"], ""]
        t = end
    return "\n".join(lines)


def main() -> None:
    WORK.mkdir(exist_ok=True)
    beats = json.loads((ROOT / "beats.json").read_text())
    segment_paths: list[Path] = []
    expected_durations: list[float] = []
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
        expected_durations.append(duration)
        t += duration
        print(f"[{i}/{len(beats)}] {beat['id']}: {duration}s (running total {t:.1f}s)")

    concat_file = WORK / "concat.txt"
    concat_file.write_text("\n".join(f"file '{p}'" for p in segment_paths))
    out_mp4 = ROOT / "grant-scout-demo.mp4"
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", str(out_mp4),
    ])

    actual_durations = measure_drift(segment_paths, expected_durations)
    max_drift_ms = max(abs(a - e) for a, e in zip(actual_durations, expected_durations)) * 1000
    (ROOT / "grant-scout-demo.srt").write_text(build_srt(beats, actual_durations))
    print(f"Max per-segment drift: {max_drift_ms:.0f}ms (within {DRIFT_TOLERANCE_S * 1000:.0f}ms "
          f"tolerance; SRT built from measured durations, not requested ones)")

    # The segments going IN were verified above; the concat -c copy MUXING
    # ITSELF can still diverge (timestamp edge cases at join points,
    # especially AAC priming) -- probe the actual shipped file too, not just
    # its inputs, or the SRT built from segment measurements could still be
    # wrong against what a viewer actually plays.
    final_duration = ffprobe_duration(out_mp4)
    concat_drift = abs(final_duration - sum(actual_durations))
    if concat_drift > DRIFT_TOLERANCE_S:
        raise SystemExit(
            f"FAIL: final mux {out_mp4.name} is {final_duration:.2f}s but its "
            f"segments sum to {sum(actual_durations):.2f}s ({concat_drift * 1000:.0f}ms "
            f"drift) -- concat itself introduced drift the SRT doesn't account for."
        )
    print(f"Final mux verified: {final_duration:.2f}s vs {sum(actual_durations):.2f}s "
          f"segment sum ({concat_drift * 1000:.0f}ms drift)")
    print(f"\nDONE. Total runtime: {final_duration:.1f}s -> {out_mp4}")


def fmt_ts(sec: float) -> str:
    total_ms = int(round(sec * 1000))
    h, rem_ms = divmod(total_ms, 3_600_000)
    m, rem_ms = divmod(rem_ms, 60_000)
    s, ms = divmod(rem_ms, 1_000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


if __name__ == "__main__":
    main()
