# Outreach Lead Generation Tool — Design Spec

**Date:** 2026-03-16
**Project:** Groundwork Studio (teamground.work)
**Status:** Approved

---

## Problem

Manual prospecting via Apple Maps is slow and produces low volume. AI-assisted research (Alfred) returns well-established businesses with good websites rather than the actual targets: local service businesses with missing, broken, or outdated websites. One rejection so far, zero conversions — volume is the immediate priority.

## Goal

A Python CLI script that automatically finds local service businesses with bad or missing websites and outputs a ready-to-send CSV of leads with pre-written outreach scripts matched to each situation.

---

## Data Source

**Yelp Fusion API** — free tier, 500 calls/day, no credit card required.

Each call returns up to 50 businesses with: name, phone, address, rating, review count, and website URL (if listed). Pagination supports up to 1,000 results per query.

Target industries (matching existing demo sites):
- Pool service, plumbing, electrical, HVAC, roofing, painting, landscaping
- Auto repair, cleaning, pest control, gym/fitness, restaurant

---

## CLI Interface

```
python leads.py "<industry>" "<city, state>" [--limit N]
```

Examples:
```
python leads.py "pool service" "Phoenix, AZ"
python leads.py "plumber" "Scottsdale, AZ" --limit 100
python leads.py "electrician" "Mesa, AZ" --limit 50
```

---

## Website Checker

For each business returned by Yelp, the script checks the website status:

| Status | Condition | Priority |
|---|---|---|
| `none` | No URL listed on Yelp | High |
| `broken` | URL exists but times out, 404s, or fails to connect | High |
| `has_website` | URL loads successfully | Low (manual review) |

- Timeout: 5 seconds per request
- Processing speed: ~1–2 seconds per business
- 100 leads ≈ 2–3 minutes total runtime

Note: Automated "dated site" detection is unreliable and is not attempted. Broken and no-website leads provide sufficient volume. Businesses with working websites are included in output at low priority for optional manual review.

---

## Output

CSV file named: `leads-[industry]-[city]-[YYYY-MM-DD].csv`

Columns:
- `Business Name`
- `Phone`
- `Address`
- `Website Status` (none / broken / has_website)
- `Website URL`
- `Outreach Script`

The CSV is sorted by priority: `none` first, `broken` second, `has_website` last.

---

## Outreach Scripts

Three script templates, selected automatically based on website status. Each template is industry-aware — the industry term (e.g., "pool company", "plumber") is inserted dynamically.

**No website:**
> Hey, hope business is going well. Noticed you don't have a website yet — for a [industry], that means homeowners who are ready to book are moving on before they ever reach you. We build clean, modern sites for local service companies that start pulling in new calls within a couple of weeks — take a look at teamground.work. Interested?
>
> Evan · Groundwork Studio

**Broken website:**
> Hey, hope business is going well. Noticed your website isn't loading properly — for a [industry], that's quietly turning away homeowners who are ready to book before they ever reach you. We can get you a clean, working site that starts pulling in new service calls within a couple of weeks — take a look at teamground.work. Interested?
>
> Evan · Groundwork Studio

**Dated/low-priority website:**
> Hey, hope business is going well. Took a look at your site — it has the feel of something built a long time ago and hasn't kept up with the business you're probably running today. Homeowners sizing up a [industry] will move on quickly if the site doesn't inspire confidence. We build clean, modern sites for local service companies — take a look at teamground.work. Interested?
>
> Evan · Groundwork Studio

---

## File Structure

```
groundwork-studio/
  outreach/
    leads.py          # Main CLI script
    requirements.txt  # requests, python-dotenv
    .env              # YELP_API_KEY (git-ignored)
    output/           # Generated CSVs (git-ignored)
```

---

## Setup Requirements

1. Create a free Yelp Fusion API account at yelp.com/developers
2. Copy API key into `.env` as `YELP_API_KEY=...`
3. `pip install -r requirements.txt`
4. Run queries

---

## Constraints

- Yelp does not reliably provide email addresses — primary contact info is phone number
- Outreach channel is SMS/text (not email)
- Free tier: 500 API calls/day. Each `leads.py` run uses 1 call per 50 results (e.g., 100 results = 2 calls)
- No hosting required — runs entirely locally

---

## Out of Scope

- Email finding / enrichment (future upgrade)
- Automated sending of messages (future upgrade)
- Web UI / dashboard (future upgrade — Approach B)
- Paying for Google Places API (future upgrade)
