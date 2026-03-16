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

Nav links added for "Why Not DIY?" (`#why-not-diy`) and "FAQ" (`#faq`) inserted between the existing "Site Care" and "Contact" nav links, in both desktop and mobile nav. Desktop nav will have 6 links + CTA button — acceptable on the current layout.

---

## Section 1: Why Not DIY?

**Location:** `index.html`, between Site Care and FAQ
**ID:** `#why-not-diy`
**Background:** `#ffffff`

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

Footer kicker line: background `#f0fdf4`, border-top `1px solid #bbf7d0`, text color `#15803d`, italic: *"You could do your own plumbing too. Most people don't."*

### Design Specs
- Outer wrapper: `border-bottom: 1px solid #e5e7eb`, `padding: 72px 24px`, `background: #ffffff`
- Inner: `max-width: 1100px; margin: 0 auto`
- Table: `width: 100%; border-collapse: collapse; font-size: 13px`
- Table header row bg: `#f9fafb`
- Groundwork column header: text `#16a34a`, `font-weight: 700`
- Wix column header: text `#9ca3af`, `font-weight: 600`
- Cell padding: `11px 20px`
- Alternating rows: odd = `#ffffff`, even = `#fafafa`
- Row border: `border-bottom: 1px solid #f3f4f6`
- Green checkmark cells: `color: #16a34a; font-weight: 700`
- Grey cross/text cells: `color: #d1d5db`
- Kicker line padding: `16px 24px`; font-size `13px`

---

## Section 2: FAQ

**Location:** `index.html`, between Why Not DIY? and Contact
**ID:** `#faq`
**Background:** `#f9fafb`

### Questions & Answers

1. **How long does it take to build my site?**
   Most sites are live in 1–2 weeks from the time we have your content (photos, copy, logo). The biggest delay is always waiting on content — the build itself is fast. Need it sooner? We can make it happen.

2. **Do I own my website?**
   Yes — you own all the content, copy, and design. We host the site on our infrastructure, which keeps it fast and maintained. If you ever want to move it, we'll hand everything over. No hostage situations.

3. **What if I need changes after launch?**
   Text and photo updates are included in our monthly maintenance plan — just send a message. Larger changes (new pages, new features) are quoted separately. Either way, you're talking to the person who built it, not a support ticket.

4. **Can't I just use Wix or Squarespace?**
   You could. You'd spend 20–40 hours learning the platform, building something that looks like every other Wix site, paying $25–40/month forever, and handling everything yourself when it breaks. Most business owners have better things to do with their time.

5. **Will my site show up on Google?**
   Every site we build includes on-page SEO basics — title tags, meta descriptions, site speed, mobile-friendliness, and proper structure. That's the foundation. For ongoing rankings and Google Business Profile management, ask us about the Growth plan.

6. **What do I need to provide to get started?**
   Ideally: your logo, a few photos of your work or team, and a sense of what services you offer. That's it. No logo? We can help. No photos? We use professional stock. We've launched sites with nothing more than a phone call.

7. **Do you work with businesses outside of Phoenix?**
   We're based in Phoenix and focused on the Valley — Scottsdale, Mesa, Tempe, Chandler, Gilbert, Glendale. We like working with local businesses we can actually visit. Reach out and we'll let you know if it's a fit.

### Design Specs
- Outer: `background: #f9fafb; padding: 72px 24px; border-bottom: 1px solid #e5e7eb`
- Inner: `max-width: 860px; margin: 0 auto` (narrower than other sections — reads better as text)
- Each FAQ item: `border-bottom: 1px solid #e5e7eb`
- Button: full width, `display: flex; justify-content: space-between; align-items: center; padding: 18px 0; background: none; border: none; cursor: pointer; text-align: left`
- Question text: `font-size: 15px; font-weight: 600; color: #111827`
- Icon: `+` / `−`, `color: #16a34a; font-size: 20px; flex-shrink: 0; margin-left: 16px`
- Hover: question text color changes to `#16a34a`; no background change (section bg is already `#f9fafb`)
- Answer div: `display: none` by default; `padding: 0 0 18px; font-size: 14px; color: #6b7280; line-height: 1.7`
- **JS approach:** Class-based toggle. On click, close all other `.faq-answer` divs (set `display: none`, reset icons to `+`), then toggle the clicked item. Only one open at a time. Pure vanilla JS, no dependencies.

---

## Section 3: Four New Demo Sites

### Template
Copy `demo-plumbing.html` as the structural template for each new demo. It includes: demo banner bar at top, Google Fonts import (Barlow Condensed + DM Sans or equivalent), sticky nav with JS scroll-triggered `.solid` class, hero with full-screen bg image, all standard sections, and footer. Replace fonts, colors, content, and section designs per each demo's brief below.

### demo-autorepair.html
- **Brand name:** Desert Ridge Auto
- **Tagline:** "Phoenix's Trusted Auto Repair Shop"
- **Location shown:** Mesa, AZ
- **Palette:** Charcoal bg `#1a1a1a`, accent orange `#ea580c`, white text
- **Font:** Import `Barlow+Condensed:wght@700;800` + `DM+Sans:wght@400;500;600` from Google Fonts
- **Hero image:** `https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=1600&q=80`
- **Services:** Oil Change & Fluids, Brake Repair, AC & Heating, Engine Diagnostics, Tire Services, Transmission
- **Unique section:** "What to Expect" 4-step process strip: Drop Off → Diagnosis → Approval → Pick Up
- **Trust badges:** ASE Certified, Loaner Vehicles Available, 12-Month Warranty
- **CTA band image:** `https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1600&q=80`
- **Reviews:** 3 fictional reviews
  - "Brought my truck in for brakes and they had it done same day. Fair price, no runaround." — Mike T., Mesa
  - "They diagnosed an issue two other shops missed. Honest and fast." — Sandra R., Gilbert
  - "Been taking my cars here for 3 years. Never felt like I was getting ripped off." — James K., Chandler
- **Work grid card image:** `https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=600&q=80`
- **Work grid badge:** text `#fff`, background `rgba(234,88,12,0.88)`, label "Auto Repair"
- **Demo card location line:** Auto Repair · Mesa

### demo-cleaning.html
- **Brand name:** Spotless Valley Cleaning
- **Tagline:** "Home & Office Cleaning You Can Trust"
- **Location shown:** Chandler, AZ
- **Palette:** White `#ffffff`, teal `#0d9488`, light grey `#f9fafb`
- **Font:** Import `Plus+Jakarta+Sans:wght@400;600;700;800` from Google Fonts (bright, readable, modern — fits light aesthetic)
- **Hero image:** `https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1600&q=80`
- **Unique trait:** Brightest, most airy demo — white bg dominant, NOT dark. Deliberate contrast from other demos.
- **Services:** Standard Clean, Deep Clean, Move-In/Out, Office Cleaning, Post-Construction, Recurring Plans
- **Unique section:** "What's Included" checklist card — two-column bullet list (kitchen, bathrooms, floors, surfaces, etc.)
- **CTA band:** Book online button, teal background, clean image of spotless interior
- **CTA band image:** `https://images.unsplash.com/photo-1563453392212-326f5e854473?w=1600&q=80`
- **Reviews:**
  - "My house has never looked this good. They got things I didn't even know were dirty." — Laura M., Chandler
  - "Super reliable, always on time, and they remember how I like things done." — David P., Gilbert
  - "Used them for a move-out clean. Got my full deposit back. Worth every penny." — Priya N., Tempe
- **Work grid card image:** `https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80`
- **Work grid badge:** text `#fff`, background `rgba(13,148,136,0.88)`, label "Cleaning"
- **Demo card location line:** Cleaning · Chandler

### demo-pestcontrol.html
- **Brand name:** Arizona Shield Pest Control
- **Tagline:** "Keep Your Home Pest-Free. Guaranteed."
- **Location shown:** Phoenix, AZ
- **Palette:** Navy `#1e3a5f`, green `#16a34a`, white text
- **Font:** Import `Barlow+Condensed:wght@700;800` + `DM+Sans:wght@400;500;600`
- **Hero image:** `https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1600&q=80`
- **Pests grid (icon + label):** Ants, Cockroaches, Scorpions, Termites, Rodents, Bed Bugs, Spiders, Wasps
- **Unique section:** Urgency band — "Same-Day Service Available" with Phoenix-specific scorpion mention
- **Guarantee callout:** 30-day re-treatment guarantee banner
- **CTA band image:** `https://images.unsplash.com/photo-1558618047-3c8c51e7c4cc?w=1600&q=80` — fallback to `photo-1585771724684-38269d6639fd` if broken
- **Reviews:**
  - "Had a scorpion problem for years. One treatment and they've been gone for 6 months." — Carlos V., Phoenix
  - "Called at 8am, they were here by noon. Exactly what I needed." — Tammy W., Glendale
  - "Quarterly service keeps our restaurant 100% compliant. Reliable every time." — Ray L., Scottsdale
- **Work grid card image:** `https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80`
- **Work grid badge:** text `#fff`, background `rgba(30,58,95,0.88)`, label "Pest Control"
- **Demo card location line:** Pest Control · Phoenix

### demo-gym.html
- **Brand name:** Iron Valley Fitness
- **Tagline:** "Train Hard. Stay Consistent. See Results."
- **Location shown:** Scottsdale, AZ
- **Palette:** Near-black `#0a0a0a`, electric yellow `#facc15`, white text
- **Font:** Import `Barlow+Condensed:wght@700;800` + `DM+Sans:wght@400;500;600`
- **Hero image:** `https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1600&q=80`
- **Membership tiers:** Day Pass ($15), Monthly ($49/mo), Annual ($39/mo billed annually)
- **Unique section:** Class schedule teaser — grid of class types (HIIT, Strength, Yoga, Spin, Boxing, Open Gym) with times
- **Trainer spotlight:** 2–3 cards with fictional trainer names, specialty, and headshot placeholder
- **CTA:** "Claim Your Free Week" — prominent yellow button
- **CTA band image:** `https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=1600&q=80`
- **Reviews:**
  - "Best gym in Scottsdale. Equipment is always clean and the staff actually knows your name." — Ashley B., Scottsdale
  - "Lost 30 lbs in 4 months. The coaches here are the real deal." — Marcus T., Phoenix
  - "Switched from a big chain gym. Never going back. Community here is unmatched." — Nina R., Tempe
- **Work grid card image:** `https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=600&q=80`
- **Work grid badge:** text `#111827`, background `rgba(250,204,21,0.92)`, label "Gym & Fitness"
- **Demo card location line:** Gym & Fitness · Scottsdale

---

## index.html Updates

### Work grid (Section 2)
Add 4 new demo cards after the existing 8, using the exact same card HTML pattern. See badge colors and image URLs above for each.

### Nav links
Desktop nav: insert `<a href="#why-not-diy">Why Not DIY?</a>` and `<a href="#faq">FAQ</a>` between the "Site Care" and "Contact" links.
Mobile nav: same insertion order.

### Contact form dropdown
Add these exact `<option>` strings (in this order, after existing options, before "Other"):
- `Auto Repair`
- `Pest Control`
- `Gym / Fitness`
(Note: "Cleaning / Maid Service" already exists — do not duplicate)

---

## Testing Checklist

After all changes are built and deployed to Netlify:

### Functional
- [ ] All 4 new demo pages load without console errors (Chrome + Safari)
- [ ] All 4 demo cards in the Work grid link to the correct `.html` file
- [ ] FAQ accordion opens/closes correctly in Chrome and Safari
- [ ] Only one FAQ item is open at a time — clicking a new one closes the previous
- [ ] FAQ hover turns question text green
- [ ] "Why Not DIY?" and "FAQ" nav links scroll to correct sections
- [ ] Contact form industry dropdown includes Auto Repair, Pest Control, Gym / Fitness
- [ ] Quote form submits and redirects to `/thank-you.html` (test on live Netlify URL)

### Visual
- [ ] Why Not DIY table renders correctly at 375px mobile (table scrolls horizontally if needed)
- [ ] FAQ section readable at 375px mobile
- [ ] All 4 new demo cards display correct badge colors and images in the Work grid
- [ ] All 4 new demo pages pass visual check at 375px and 1280px
- [ ] No broken images on any new demo page (check all Unsplash URLs load)

### Cross-browser
- [ ] Test accordion JS in Chrome (latest)
- [ ] Test accordion JS in Safari (latest)

---

## Out of Scope

- Pricing section (decided: keep pricing off the site, quote-only)
- ROI calculator or framing section (deferred)
- Redesigning existing 8 demo pages
- Any backend / CMS changes
- Google Analytics or tracking setup
