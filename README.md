# 100Hire Research Project — Community-Led Growth for B2B SaaS

A research base on **community-led growth (CLG) for B2B SaaS**: 10 hand-picked practitioners,
their recent content collected through free APIs and public sources, and organized so it can
support a real playbook later.

> **Topic chosen (1 of 8):** Community-led growth for B2B SaaS.
> I picked it because the expert pool is high-signal but *non-obvious* — it rewards knowing who
> actually built communities over who ranks first on Google — and because CLG ties cleanly to the
> B2B SaaS metrics that matter (retention, advocacy, pipeline), which makes it a strong base for a
> future playbook.

---

## What I collected (at a glance)

| Deliverable | Where | Count |
|---|---|---|
| Vetted experts with links, dates, annotations | [`research/sources.md`](research/sources.md) | 10 (+3 honorable mentions) |
| YouTube transcripts (full text, by author) | [`research/youtube-transcripts/`](research/youtube-transcripts/) | 18 videos, 9 experts |
| LinkedIn posts (verbatim, by author) | [`research/linkedin-posts/`](research/linkedin-posts/) | 33 posts, 10 experts |
| Podcast index + books index | [`research/other/`](research/other/) | 2 reference files |
| Reusable transcript-collection tool | [`scripts/fetch_transcripts.py`](scripts/fetch_transcripts.py) | — |

---

## The 10 experts (and why them)

Selected for **practitioner depth + B2B SaaS relevance + verifiability** — people who built or ran
real communities (or community-led companies), not commentators. The set deliberately spans the
field's range rather than clustering on the same few famous names. Full annotations and links in
[`research/sources.md`](research/sources.md).

| # | Expert | Why they're high-signal |
|---|---|---|
| 1 | **Lloyed Lobo** | Bootstrapped Boast.AI to $10M+ ARR via CLG + built Traction (100k); wrote *From Grassroots to Greatness* |
| 2 | **David Spinks** | Founded CMX; wrote *The Business of Belonging* — defined the category |
| 3 | **Erica Kuhl** | Built the Salesforce Trailblazer Community (~3M members); now EVP/GM at Gainsight |
| 4 | **Holly Firestone** | Ran community at Atlassian, Salesforce & Venafi; "Return on Community" framing |
| 5 | **Carrie Melissa Jones** | Co-founded CMX; co-wrote *Building Brand Communities*; still teaches the ops in 2025 |
| 6 | **Mac Reddin** | CEO of Commsor (the CLG-tooling company); now pioneering "go-to-network" |
| 7 | **Rosie Sherry** | Bootstrapped Ministry of Testing; ex-Indie Hackers; founder of Rosieland |
| 8 | **Bailey Richardson** | *Get Together* (Stripe Press); built community at Instagram → Substack → OpenAI |
| 9 | **Christina Garnett** | Built HubSpot's HubFans advocacy program; active into 2026; 2025 book |
| 10 | **Brian Oblinger** | Pure enterprise B2B/SaaS community consultant; hosts *In Before The Lock* |

Honorable mentions considered but cut (with reasons) are listed in `sources.md` — Greg Isenberg
(consumer/AI lean), Jenny Weigle, Noele Flowers.

---

## How I chose them (methodology)

1. **Started from practice, not search rank.** Seeded ~13 candidates known for *doing* CLG
   (building communities or community-led companies), then verified each against live sources.
2. **Verified, didn't assume.** Every LinkedIn handle, YouTube video ID, and podcast episode was
   checked against a real source. Anything I couldn't confirm on-page is marked _(unverified)_
   rather than guessed. Several plausible-but-unconfirmed video dates were flagged, not invented.
3. **Covered the range.** Final 10 spans company-builders, enterprise in-house leaders, category
   authors, a bootstrapped independent, and a pure-enterprise consultant — so a future playbook
   draws on different vantage points, not one echo chamber.
4. **Quality over volume.** Kept the substantive posts/talks and dropped low-signal items (e.g.
   one-line reshares) — consistent with "10 high-signal sources beat 50 generic ones."

---

## How the content was collected (APIs & tools)

The task allows "Supadata **or other free methods**," so everything here uses **free, no-key**
tooling:

- **YouTube transcripts** — [`scripts/fetch_transcripts.py`](scripts/fetch_transcripts.py) uses the
  [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) package (no API key).
  It reads a manifest of verified video IDs
  ([`research/youtube-transcripts/videos.json`](research/youtube-transcripts/videos.json)), pulls
  each public caption track, and writes one markdown file per video (metadata header + timestamped
  transcript). It's idempotent (skips files that already exist) and logs failures instead of
  crashing.
- **LinkedIn posts** — LinkedIn blocks automated access to *profile* pages (HTTP 999), but
  individual **public post permalinks** are readable. I found permalinks via web search and fetched
  the verbatim post text + date + engagement. Only successfully fetched text is included; partial
  extractions are flagged _(partial verbatim)_. Details in
  [`research/linkedin-posts/README.md`](research/linkedin-posts/README.md).
- **Podcasts / books** — indexed with verified links in [`research/other/`](research/other/)
  (the primary recent channel for audio-first experts like Brian Oblinger).

### Reproduce the transcript collection

```bash
pip install -r requirements.txt
python scripts/fetch_transcripts.py            # pulls everything in videos.json
python scripts/fetch_transcripts.py <VIDEO_ID>  # ad-hoc, prints to stdout
```

---

## Repository structure

```
100hire-project/
├── README.md                       # this file
├── requirements.txt
├── scripts/
│   └── fetch_transcripts.py        # free YouTube transcript collector (no API key)
└── research/
    ├── sources.md                  # 10 experts: links, dates, annotations, method notes
    ├── linkedin-posts/             # verbatim posts, one folder per author
    │   ├── README.md               # collection method + honesty notes
    │   └── <author>/posts.md
    ├── youtube-transcripts/        # one folder per author
    │   ├── videos.json             # verified video manifest the script reads
    │   └── <author>/<id>__<slug>.md
    └── other/
        ├── podcasts.md             # hosted shows + dated guest appearances
        └── books.md                # the 5 foundational CLG books by these experts
```

---

## Honesty & limitations

- **Dates:** YouTube upload dates aren't cleanly exposed via the transcript API, and LinkedIn shows
  only relative dates ("7 months ago") captured on 2026-06-17 — approximate dates are labeled as such.
- **Two short YouTube items** (Bailey HBS clip, Christina RevGenius clip) are ~1-minute highlight
  reels, not full talks; the word count in each file's header makes that clear, and both authors
  have full-length transcripts as well.
- **No fabrication:** every video ID produced a real transcript; every LinkedIn quote was actually
  fetched; unverifiable items are flagged rather than presented as fact.

---

## Project log

- **2026-06-17 — Research project (this step):** chose the CLG topic, vetted 10 experts, collected
  18 transcripts + 33 LinkedIn posts + podcast/book indexes, built the transcript tool, committed
  incrementally.
- **2026-05-30 — Environment setup (step 1):** installed Cursor IDE, Claude Code, and Codex; created
  and pushed this public GitHub repo. _(Original setup notes preserved in
  [`docs/setup-notes.md`](docs/setup-notes.md).)_
