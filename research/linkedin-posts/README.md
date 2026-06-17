# LinkedIn Posts — collection notes

Recent public LinkedIn posts for the 10 experts, one folder per author.

## Method (free, no paid scraper)

LinkedIn **profile** pages block automated access (they return HTTP 999 to bots), so a profile
crawl is not possible with free tooling. However, individual **public post permalinks** — URLs of
the form `linkedin.com/posts/<slug>_<words>-activity-<id>-<code>` — *are* publicly readable. The
process here was:

1. Find each expert's public post permalinks via web search.
2. Fetch each permalink and extract the verbatim post text, relative date, and engagement counts.
3. Keep only posts whose text was actually retrieved — **nothing is fabricated**.

## Honesty notes

- **Dates** are LinkedIn's relative labels ("7 months ago") captured on 2026-06-17 — exact
  timestamps are not exposed, so treat them as approximate.
- A few longer posts came back as **verbatim opening + faithful summary** rather than full verbatim
  body; these are flagged inline as _(partial verbatim)_ so the paraphrase is never mistaken for an
  exact quote.
- Some authors' most recent (2025–26) activity did not surface as fetchable public permalinks;
  where retrievable posts skew older, that is noted in the author's file. For those, the freshest
  material lives in [`../youtube-transcripts/`](../youtube-transcripts/) and
  [`../other/`](../other/) (podcasts, books).
- A handful of permalinks returned BLOCKED and were excluded rather than guessed at.

## Coverage

| Author | Posts collected | Freshest post |
|---|---|---|
| Lloyed Lobo | 4 | ~2023 |
| David Spinks | 4 | ~2023 |
| Erica Kuhl | 3 | ~late 2025 |
| Holly Firestone | 3 | ~2023 |
| Carrie Melissa Jones | 3 | ~early 2024 |
| Mac Reddin | 4 | ~2025-04 |
| Rosie Sherry | 2 | ~2023 |
| Bailey Richardson | 4 | ~2025-11 |
| Christina Garnett | 3 | ~2024 |
| Brian Oblinger | 3 | ~2024 |
