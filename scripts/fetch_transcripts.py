#!/usr/bin/env python3
"""
fetch_transcripts.py — Free, no-API-key YouTube transcript collector.

Uses the `youtube-transcript-api` package (https://pypi.org/project/youtube-transcript-api/),
which pulls the publicly available caption track for a video. No Google API key and no
Supadata key required — this is one of the "other free methods" the task allows.

Input:  research/youtube-transcripts/videos.json
        A list of {author, video_id, title, url, date} objects (see that file).

Output: research/youtube-transcripts/<author-slug>/<video_id>__<title-slug>.md
        One markdown file per video: metadata header + cleaned, timestamped transcript.

Usage:
    python scripts/fetch_transcripts.py                # fetch everything in videos.json
    python scripts/fetch_transcripts.py <VIDEO_ID> ... # ad-hoc, prints to stdout

Notes:
    * Forces UTF-8 output so it runs cleanly on Windows consoles.
    * Skips videos whose transcript file already exists (idempotent / re-runnable).
    * Records failures (transcripts disabled, no captions, etc.) instead of crashing.
"""

import io
import json
import os
import re
import sys

# Force UTF-8 so Windows (cp1252) consoles don't choke on transcript text.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSCRIPT_DIR = os.path.join(ROOT, "research", "youtube-transcripts")
VIDEOS_JSON = os.path.join(TRANSCRIPT_DIR, "videos.json")


def slugify(text, maxlen=60):
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:maxlen].strip("-") or "untitled"


def fmt_timestamp(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def fetch_one(video_id):
    """Return a list of snippet objects (.text, .start) for a video, or raise."""
    api = YouTubeTranscriptApi()
    return api.fetch(video_id)


def write_markdown(meta, snippets):
    author_slug = slugify(meta.get("author", "unknown"))
    out_dir = os.path.join(TRANSCRIPT_DIR, author_slug)
    os.makedirs(out_dir, exist_ok=True)
    fname = f"{meta['video_id']}__{slugify(meta.get('title', meta['video_id']))}.md"
    path = os.path.join(out_dir, fname)

    word_count = sum(len(s.text.split()) for s in snippets)
    lines = [
        f"# {meta.get('title', meta['video_id'])}",
        "",
        f"- **Author/Speaker:** {meta.get('author', 'Unknown')}",
        f"- **Video:** {meta.get('url', 'https://www.youtube.com/watch?v=' + meta['video_id'])}",
        f"- **Video ID:** {meta['video_id']}",
        f"- **Published:** {meta.get('date', 'unknown')}",
        f"- **Transcript words:** ~{word_count}",
        "- **Source:** youtube-transcript-api (free, no API key)",
        "",
        "---",
        "",
        "## Transcript",
        "",
    ]
    for s in snippets:
        text = s.text.replace("\n", " ").strip()
        if text:
            lines.append(f"`[{fmt_timestamp(s.start)}]` {text}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path, word_count


def run_from_json():
    if not os.path.exists(VIDEOS_JSON):
        print(f"No videos.json at {VIDEOS_JSON}", file=sys.stderr)
        sys.exit(1)
    with open(VIDEOS_JSON, encoding="utf-8") as f:
        videos = json.load(f)

    ok, skipped, failed = 0, 0, []
    for meta in videos:
        vid = meta["video_id"]
        author_slug = slugify(meta.get("author", "unknown"))
        fname = f"{vid}__{slugify(meta.get('title', vid))}.md"
        path = os.path.join(TRANSCRIPT_DIR, author_slug, fname)
        if os.path.exists(path):
            print(f"  skip (exists): {meta.get('author')} — {meta.get('title')}")
            skipped += 1
            continue
        try:
            snippets = fetch_one(vid)
            out, wc = write_markdown(meta, snippets)
            print(f"  ok ({wc:>5} words): {os.path.relpath(out, ROOT)}")
            ok += 1
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            print(f"  FAIL [{type(e).__name__}]: {meta.get('author')} — {vid}")
            failed.append((vid, type(e).__name__))
        except Exception as e:  # noqa: BLE001 — log anything unexpected, keep going
            print(f"  FAIL [{type(e).__name__}]: {meta.get('author')} — {vid}: {str(e)[:120]}")
            failed.append((vid, type(e).__name__))

    print(f"\nDone. ok={ok} skipped={skipped} failed={len(failed)}")
    if failed:
        print("Failures:")
        for vid, err in failed:
            print(f"  - {vid}: {err}")


def run_adhoc(video_ids):
    for vid in video_ids:
        print(f"\n===== {vid} =====")
        try:
            for s in fetch_one(vid):
                print(f"[{fmt_timestamp(s.start)}] {s.text}")
        except Exception as e:  # noqa: BLE001
            print(f"FAIL [{type(e).__name__}]: {str(e)[:160]}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_adhoc(sys.argv[1:])
    else:
        run_from_json()
