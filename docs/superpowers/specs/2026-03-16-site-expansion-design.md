# Groundwork Studio — Site Expansion Design
**Date:** 2026-03-16
**Status:** Approved

---

## Overview

Expand `teamground.work` to better justify pricing, handle objections proactively, and show broader industry range. No pricing numbers are shown publicly — the goal is to get visitors convinced before they fill out the quote form.

Three deliverables:
1. **"Why Not DIY?" section** — comparison table vs Wix/Fiverr/DIY
2. **FAQ section** — 7 accordion questions handling real objections
3. **4 new demo sites** — Auto Repair, Cleaning Service, Pest Control, Gym/Fitness

---

## Updated Page Flow

| Position | Section | Change |
|---|---|---|
| 1 | Hero | No change |
| 2 | Work — Demo Grid | +4 new demo cards → 12 total |
| 3 | How It Works | No change |
| 4 | Site Care | No change |
| 5 | Why Not DIY? | **New** |
| 6 | FAQ | **New** |
| 7 | Contact Form | No change |

Nav links added for "Why Not DIY?" (`#why-not-diy`) and "FAQ" (`#faq`) in both desktop and mobile nav.

---

## Section 1: Why Not DIY?

**Location:** `index.html`, between Site Care and FAQ
**ID:** `#why-not-diy`
**Background:** White

### Content

Header label: `WHY NOT DIY?`
Headline: *"A custom site from a real developer isn't the same as doing it yourself."*

Comparison table — 7 rows:

| Row | Groundwork Studio | Wix / DIY / Fiverr |
|---|---|---|
| Built specifically for your business | ✓ | ✗ |
| Mobile-ready & fast out of the box | ✓ | Sometimes |
| SEO built in from day one | ✓ | ✗ |
| Someone to call when something breaks | ✓ | ✗ |
| Updates handled for you | ✓ | Your problem |
| No platform lock-in fees | ✓ | $20–40/mo forever |
| Local Phoenix developer, not overseas | ✓ | ✗ |

Footer kicker line (green bg): *"You could do your own plumbing too. Most people don't."*

### Design
- Matches existing section style: white bg, `#e5e7eb` border-bottom, `max-width:1100px`
- Table header: green for Groundwork column, grey for Wix column
- Alternating row shading (`#fafafa` / white)
- Green checkmarks (`#16a34a`), grey X marks (`#d1d5db`)

---

## Section 2: FAQ

**Location:** `index.html`, between Why Not DIY? and Contact
**ID:** `#faq`
**Background:** `#f9fafb`

### Questions & Answers

1. **How long does it take to build my site?**
   Most sites live in 1–2 weeks from content receipt. Biggest delay is always waiting on content — the build itself is fast.

2. **Do I own my website?**
   Yes — all content, copy, and design. Hosted on our infrastructure for speed/maintenance. Everything handed over if they ever want to move.

3. **What if I need changes after launch?**
   Text/photo updates included in monthly maintenance plan. Larger changes quoted separately. Always talking to the person who built it.

4. **Can't I just use Wix or Squarespace?**
   You could. 20–40 hours learning the platform, looks like every other Wix site, $25–40/mo forever, handle everything yourself when it breaks.

5. **Will my site show up on Google?**
   On-page SEO included (title tags, meta, speed, mobile, structure). Ongoing rankings via Growth plan.

6. **What do I need to provide to get started?**
   Logo, a few photos, sense of services. No logo or photos? We handle it. Have launched sites from a single phone call.

7. **Do you work with businesses outside of Phoenix?**
   Focused on the Valley (Scottsdale, Mesa, Tempe, Chandler, Gilbert, Glendale). Local-first. Reach out to see if it's a fit.

### Design
- `#f9fafb` background, `max-width:1100px`
- Accordion: each item is a full-width button + collapsible answer div
- `+` icon toggles to `−` when open; only one item open at a time
- Hover state: `#f9fafb` bg on question row, question text turns green
- Pure HTML/CSS/JS — no dependencies

---

## Section 3: Four New Demo Sites

Each demo is a standalone HTML file following the established pattern of existing demos. Each has: sticky nav, hero with bg image, services section, process/trust section, CTA band, reviews, footer.

### demo-autorepair.html
- **Brand:** Desert Ridge Auto
- **Palette:** Charcoal (`#1a1a1a`) + orange (`#ea580c`)
- **Key sections:** Service cards (oil change, brakes, AC, diagnostics, tires, engine), trust badges (ASE Certified, loaner vehicles, warranty), photo CTA band
- **Unique element:** "What to expect" process strip (drop off → diagnosis → approval → pick up)

### demo-cleaning.html
- **Brand:** Spotless Valley Cleaning
- **Palette:** White + teal (`#0d9488`)
- **Key sections:** Residential / Commercial split cards, "What's included" checklist, before/after framing, booking CTA
- **Unique element:** Airy light layout — most other demos are dark, this one is bright/fresh as contrast

### demo-pestcontrol.html
- **Brand:** Arizona Shield Pest Control
- **Palette:** Navy (`#1e3a5f`) + green (`#16a34a`)
- **Key sections:** "Pests we handle" icon grid (ants, roaches, scorpions, termites, rodents, bed bugs), guarantee/warranty callout banner, emergency same-day service band
- **Unique element:** Urgency-forward — scorpion/pest imagery, "same-day service" prominently placed for Phoenix relevance

### demo-gym.html
- **Brand:** Iron Valley Fitness
- **Palette:** Near-black (`#0a0a0a`) + electric yellow (`#facc15`)
- **Key sections:** Membership tiers (Day Pass / Monthly / Annual), class schedule teaser, trainer spotlight cards, free trial CTA
- **Unique element:** Bold, high-contrast dark aesthetic — stands out from all other demos which are lighter

---

## index.html Updates

### Work grid (Section 2)
Add 4 new demo cards following the same card pattern:
- Auto Repair card — orange badge, garage/mechanic Unsplash image
- Cleaning Service card — teal badge, clean home Unsplash image
- Pest Control card — green badge, pest/exterminator Unsplash image
- Gym / Fitness card — yellow badge, gym Unsplash image

### Nav links
Desktop and mobile nav: add `Why Not DIY?` → `#why-not-diy` and `FAQ` → `#faq`

### Contact form dropdown
Add to industry select: `Auto Repair`, `Cleaning / Maid Service` (already exists), `Pest Control`, `Gym / Fitness`

---

## Testing Checklist

After all changes are built:
- [ ] All 4 new demo pages load without errors
- [ ] All 4 demo cards in the Work grid link correctly
- [ ] Why Not DIY section renders correctly at mobile widths
- [ ] FAQ accordion opens/closes correctly; only one item open at a time
- [ ] Nav links scroll to correct sections
- [ ] Contact form industry dropdown includes new options
- [ ] Quote form submits and redirects to `/thank-you.html`
- [ ] All pages pass a visual check on mobile (375px) and desktop (1280px)

---

## Out of Scope

- Pricing section (decided: keep pricing off the site, quote-only)
- ROI calculator (deferred — may revisit)
- Redesigning existing demo pages
- Any backend / CMS changes
