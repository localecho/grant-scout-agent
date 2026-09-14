**Grade: A-**

Both named gaps are genuinely closed, not cosmetically: `build_srt` consumes measured actuals end-to-end, and the drift check is a real build-failing gate with a sensible rationale distinguishing padding from breakage. The pipeline is honest — captions provably match rendered output, and a broken render cannot ship silently.

What's left for a full A:

1. **The final mux is never verified.** You probe every segment, then `-c copy` concat them — but never ffprobe `grant-scout-demo.mp4` itself and compare it to `sum(actual_durations)`. Concat-demuxer timestamp edge cases (especially AAC priming at segment joins) can make the final file diverge from the segment sum, which would silently invalidate the SRT you just carefully built from per-segment measurements. One more probe + drift check closes the loop completely.

2. **`ffprobe_duration` ignores `returncode`.** If ffprobe fails (missing file, corrupt segment), `float("")` raises a bare `ValueError` instead of a diagnostic. Minor, but `run()` sets the pattern this function doesn't follow.

Everything else — validation, error messages, the 50ms warn / 100ms fail split, cumulative-timeline correctness — is solid. Fix #1 especially and this is an A: #1 is a real verification hole, not polish.