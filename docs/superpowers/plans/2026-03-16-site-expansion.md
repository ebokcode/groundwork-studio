# Site Expansion Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "Why Not DIY?" comparison section, FAQ accordion, and 4 new demo sites (Auto Repair, Cleaning, Pest Control, Gym/Fitness) to teamground.work.

**Architecture:** All changes are standalone static HTML files with inline styles and vanilla JS. `index.html` gets 2 new sections inserted and minor nav/grid/form updates. 4 new demo pages are created by copying `demo-plumbing.html` as a structural template and replacing all content, colors, and copy per the spec.

**Tech Stack:** Plain HTML, inline CSS, vanilla JS only. No build system. Hosted on Netlify via git push to main.

**Spec:** `docs/superpowers/specs/2026-03-16-site-expansion-design.md`

---

## File Map

| Action | File | What changes |
|--------|------|-------------|
| Modify | `index.html` | Insert Why Not DIY? section, FAQ section, 2 nav links, 4 work grid cards, 3 form options |
| Create | `demo-autorepair.html` | New demo — Desert Ridge Auto, charcoal + orange |
| Create | `demo-cleaning.html` | New demo — Spotless Valley Cleaning, white + teal |
| Create | `demo-pestcontrol.html` | New demo — Arizona Shield Pest Control, navy + green |
| Create | `demo-gym.html` | New demo — Iron Valley Fitness, near-black + yellow |

---

## Chunk 1: index.html Updates

### Task 1: Add "Why Not DIY?" section

**Files:**
- Modify: `index.html` — insert between the closing `</section>` of Site Care and the `<!-- CONTACT -->` comment

- [ ] **Step 1: Open `index.html` and locate the insertion point**

  Find the line: `<!-- CONTACT / CTA -->` (currently around line 430 after the Site Care section). The new section goes immediately before it.

- [ ] **Step 2: Insert the Why Not DIY? section**

  Insert this block at that location:

  ```html
  <!-- ============================================================
       WHY NOT DIY?
       ============================================================ -->
  <section id="why-not-diy" style="padding:72px 24px;border-bottom:1px solid #e5e7eb;background:#ffffff;">
    <div style="max-width:1100px;margin:0 auto;">

      <div style="font-size:11px;font-weight:700;letter-spacing:2.5px;color:#16a34a;text-transform:uppercase;margin-bottom:8px;">
        Why Not DIY?
      </div>
      <h2 style="font-size:28px;font-weight:800;color:#111827;margin-bottom:36px;line-height:1.2;">
        A custom site from a real developer<br>isn't the same as doing it yourself.
      </h2>

      <div style="overflow-x:auto;border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;">
        <table style="width:100%;border-collapse:collapse;font-size:13px;">
          <thead>
            <tr style="background:#f9fafb;">
              <th style="padding:11px 20px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb;width:44%;">What you're comparing</th>
              <th style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;border-bottom:1px solid #e5e7eb;width:28%;">Groundwork Studio</th>
              <th style="padding:11px 20px;text-align:center;color:#9ca3af;font-weight:600;border-bottom:1px solid #e5e7eb;width:28%;">Wix / DIY / Fiverr</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid #f3f4f6;">
              <td style="padding:11px 20px;color:#374151;font-weight:500;">Built specifically for your business</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#d1d5db;">✗</td>
            </tr>
            <tr style="background:#fafafa;border-bottom:1px solid #f3f4f6;">
              <td style="padding:11px 20px;color:#374151;font-weight:500;">Mobile-ready &amp; fast out of the box</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#9ca3af;font-style:italic;">Sometimes</td>
            </tr>
            <tr style="border-bottom:1px solid #f3f4f6;">
              <td style="padding:11px 20px;color:#374151;font-weight:500;">SEO built in from day one</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#d1d5db;">✗</td>
            </tr>
            <tr style="background:#fafafa;border-bottom:1px solid #f3f4f6;">
              <td style="padding:11px 20px;color:#374151;font-weight:500;">Someone to call when something breaks</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#d1d5db;">✗</td>
            </tr>
            <tr style="border-bottom:1px solid #f3f4f6;">
              <td style="padding:11px 20px;color:#374151;font-weight:500;">Updates handled for you</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#9ca3af;font-style:italic;">Your problem</td>
            </tr>
            <tr style="background:#fafafa;border-bottom:1px solid #f3f4f6;">
              <td style="padding:11px 20px;color:#374151;font-weight:500;">No platform lock-in fees</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#9ca3af;font-style:italic;">$20–40/mo forever</td>
            </tr>
            <tr>
              <td style="padding:11px 20px;color:#374151;font-weight:500;">Local Phoenix developer, not overseas</td>
              <td style="padding:11px 20px;text-align:center;color:#16a34a;font-weight:700;">✓</td>
              <td style="padding:11px 20px;text-align:center;color:#d1d5db;">✗</td>
            </tr>
          </tbody>
        </table>
        <div style="padding:14px 20px;background:#f0fdf4;border-top:1px solid #bbf7d0;font-size:13px;color:#15803d;font-style:italic;">
          "You could do your own plumbing too. Most people don't."
        </div>
      </div>

    </div>
  </section>
  ```

- [ ] **Step 3: Verify in browser at localhost — section renders, table is readable, kicker line is green**

- [ ] **Step 4: Verify at 375px mobile width — table scrolls horizontally without breaking layout**

- [ ] **Step 5: Commit**

  ```bash
  git add index.html
  git commit -m "Add Why Not DIY comparison section to index.html"
  ```

---

### Task 2: Add FAQ section

**Files:**
- Modify: `index.html` — insert between Why Not DIY? section and Contact section

- [ ] **Step 1: Locate insertion point**

  Find the `<!-- CONTACT / CTA -->` comment. The FAQ section goes immediately before it.

- [ ] **Step 2: Insert the FAQ section**

  ```html
  <!-- ============================================================
       FAQ
       ============================================================ -->
  <section id="faq" style="padding:72px 24px;border-bottom:1px solid #e5e7eb;background:#f9fafb;">
    <div style="max-width:860px;margin:0 auto;">

      <div style="font-size:11px;font-weight:700;letter-spacing:2.5px;color:#16a34a;text-transform:uppercase;margin-bottom:8px;">
        FAQ
      </div>
      <h2 style="font-size:28px;font-weight:800;color:#111827;margin-bottom:36px;">
        Common questions, straight answers.
      </h2>

      <div id="faq-accordion" style="border-top:1px solid #e5e7eb;">

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">How long does it take to build my site?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">Most sites are live in <strong style="color:#374151;">1–2 weeks</strong> from the time we have your content (photos, copy, logo). The biggest delay is always waiting on content — the build itself is fast. Need it sooner? We can make it happen.</p>
          </div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">Do I own my website?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">Yes — you own all the content, copy, and design. We host the site on our infrastructure, which keeps it fast and maintained. If you ever want to move it, we'll hand everything over. No hostage situations.</p>
          </div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">What if I need changes after launch?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">Text and photo updates are included in our monthly maintenance plan — just send a message. Larger changes (new pages, new features) are quoted separately. Either way, you're talking to the person who built it, not a support ticket.</p>
          </div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">Can't I just use Wix or Squarespace?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">You could. You'd spend 20–40 hours learning the platform, building something that looks like every other Wix site, paying $25–40/month forever, and handling everything yourself when it breaks. Most business owners have better things to do with their time.</p>
          </div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">Will my site show up on Google?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">Every site we build includes on-page SEO basics — title tags, meta descriptions, site speed, mobile-friendliness, and proper structure. That's the foundation. For ongoing rankings and Google Business Profile management, ask us about the Growth plan.</p>
          </div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">What do I need to provide to get started?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">Ideally: your logo, a few photos of your work or team, and a sense of what services you offer. That's it. No logo? We can help. No photos? We use professional stock. We've launched sites with nothing more than a phone call.</p>
          </div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid #e5e7eb;">
          <button onclick="toggleFaq(this)" style="width:100%;display:flex;justify-content:space-between;align-items:center;padding:18px 0;background:none;border:none;cursor:pointer;text-align:left;">
            <span style="font-size:15px;font-weight:600;color:#111827;transition:color .15s;">Do you work with businesses outside of Phoenix?</span>
            <span style="font-size:22px;color:#16a34a;font-weight:300;flex-shrink:0;margin-left:20px;line-height:1;">+</span>
          </button>
          <div style="display:none;padding:0 0 18px;">
            <p style="font-size:14px;color:#6b7280;line-height:1.7;margin:0;">We're based in Phoenix and focused on the Valley — Scottsdale, Mesa, Tempe, Chandler, Gilbert, Glendale. We like working with local businesses we can actually visit. Reach out and we'll let you know if it's a fit.</p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <script>
  function toggleFaq(btn) {
    const answer = btn.nextElementSibling;
    const icon = btn.querySelector('span:last-child');
    const isOpen = answer.style.display === 'block';
    // Close all
    document.querySelectorAll('#faq-accordion .faq-item > div').forEach(a => a.style.display = 'none');
    document.querySelectorAll('#faq-accordion .faq-item button span:last-child').forEach(i => i.textContent = '+');
    document.querySelectorAll('#faq-accordion .faq-item button span:first-child').forEach(s => s.style.color = '#111827');
    // Open clicked (if it was closed)
    if (!isOpen) {
      answer.style.display = 'block';
      icon.textContent = '−';
      btn.querySelector('span:first-child').style.color = '#16a34a';
    }
  }
  </script>
  ```

- [ ] **Step 3: Open in browser — verify all 7 items render**

- [ ] **Step 4: Click item 1 — verify it expands, icon changes to −, text turns green**

- [ ] **Step 5: Click item 2 — verify item 1 closes automatically, item 2 opens**

- [ ] **Step 6: Click item 2 again — verify it closes (toggle off)**

- [ ] **Step 7: Verify at 375px mobile — all questions readable, no overflow**

- [ ] **Step 8: Commit**

  ```bash
  git add index.html
  git commit -m "Add FAQ accordion section to index.html"
  ```

---

### Task 3: Nav links, work grid cards, and form options

**Files:**
- Modify: `index.html` — desktop nav, mobile nav, work grid, contact form dropdown

- [ ] **Step 1: Add desktop nav links**

  Find the desktop nav block. After the "Site Care" link and before "Contact":

  ```html
  <a href="#why-not-diy" style="font-size:14px;color:#374151;text-decoration:none;font-weight:500;">Why Not DIY?</a>
  <a href="#faq" style="font-size:14px;color:#374151;text-decoration:none;font-weight:500;">FAQ</a>
  ```

- [ ] **Step 2: Add mobile nav links**

  Find the mobile nav block. Same position — after Site Care link, before Contact:

  ```html
  <a href="#why-not-diy">Why Not DIY?</a>
  <a href="#faq">FAQ</a>
  ```

- [ ] **Step 3: Add 4 demo cards to the work grid**

  After the existing 8 cards (after the Painting card closing `</div>`), add:

  ```html
  <!-- Auto Repair -->
  <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;">
    <div style="height:140px;background:linear-gradient(rgba(26,26,26,0.72),rgba(26,26,26,0.72)),url('https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=600&q=80') center/cover no-repeat;display:flex;align-items:flex-end;padding:10px 12px;">
      <span style="font-size:11px;color:#fff;font-weight:600;background:rgba(234,88,12,0.88);padding:3px 8px;border-radius:4px;">Auto Repair</span>
    </div>
    <div style="padding:16px;">
      <div style="font-size:14px;font-weight:700;color:#111827;margin-bottom:4px;">Desert Ridge Auto</div>
      <div style="font-size:12px;color:#6b7280;margin-bottom:12px;">Auto Repair · Mesa</div>
      <a href="demo-autorepair.html" style="font-size:13px;font-weight:700;color:#16a34a;text-decoration:none;">View Demo →</a>
    </div>
  </div>

  <!-- Cleaning -->
  <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;">
    <div style="height:140px;background:linear-gradient(rgba(13,148,136,0.55),rgba(13,148,136,0.55)),url('https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80') center/cover no-repeat;display:flex;align-items:flex-end;padding:10px 12px;">
      <span style="font-size:11px;color:#fff;font-weight:600;background:rgba(13,148,136,0.88);padding:3px 8px;border-radius:4px;">Cleaning</span>
    </div>
    <div style="padding:16px;">
      <div style="font-size:14px;font-weight:700;color:#111827;margin-bottom:4px;">Spotless Valley Cleaning</div>
      <div style="font-size:12px;color:#6b7280;margin-bottom:12px;">Cleaning · Chandler</div>
      <a href="demo-cleaning.html" style="font-size:13px;font-weight:700;color:#16a34a;text-decoration:none;">View Demo →</a>
    </div>
  </div>

  <!-- Pest Control -->
  <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;">
    <div style="height:140px;background:linear-gradient(rgba(30,58,95,0.75),rgba(30,58,95,0.75)),url('https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80') center/cover no-repeat;display:flex;align-items:flex-end;padding:10px 12px;">
      <span style="font-size:11px;color:#fff;font-weight:600;background:rgba(30,58,95,0.88);padding:3px 8px;border-radius:4px;">Pest Control</span>
    </div>
    <div style="padding:16px;">
      <div style="font-size:14px;font-weight:700;color:#111827;margin-bottom:4px;">Arizona Shield Pest Control</div>
      <div style="font-size:12px;color:#6b7280;margin-bottom:12px;">Pest Control · Phoenix</div>
      <a href="demo-pestcontrol.html" style="font-size:13px;font-weight:700;color:#16a34a;text-decoration:none;">View Demo →</a>
    </div>
  </div>

  <!-- Gym & Fitness -->
  <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;">
    <div style="height:140px;background:linear-gradient(rgba(10,10,10,0.65),rgba(10,10,10,0.65)),url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=600&q=80') center/cover no-repeat;display:flex;align-items:flex-end;padding:10px 12px;">
      <span style="font-size:11px;color:#111827;font-weight:600;background:rgba(250,204,21,0.92);padding:3px 8px;border-radius:4px;">Gym &amp; Fitness</span>
    </div>
    <div style="padding:16px;">
      <div style="font-size:14px;font-weight:700;color:#111827;margin-bottom:4px;">Iron Valley Fitness</div>
      <div style="font-size:12px;color:#6b7280;margin-bottom:12px;">Gym &amp; Fitness · Scottsdale</div>
      <a href="demo-gym.html" style="font-size:13px;font-weight:700;color:#16a34a;text-decoration:none;">View Demo →</a>
    </div>
  </div>
  ```

- [ ] **Step 4: Add form dropdown options**

  In the contact form `<select name="industry">`, add before the `<option>Other</option>` line:

  ```html
  <option>Auto Repair</option>
  <option>Pest Control</option>
  <option>Gym / Fitness</option>
  ```

- [ ] **Step 5: Verify in browser — all 12 cards appear in the work grid**

- [ ] **Step 6: Verify nav — "Why Not DIY?" and "FAQ" links appear and scroll to correct sections**

- [ ] **Step 7: Verify form dropdown includes the 3 new options**

- [ ] **Step 8: Commit**

  ```bash
  git add index.html
  git commit -m "Add nav links, 4 demo cards, and form options to index.html"
  ```

---

## Chunk 2: Demo Sites

**Shared build pattern for all 4 demos:**
1. Copy `demo-plumbing.html` to the new filename
2. Replace Google Fonts import URL
3. Replace all CSS variables / color values
4. Replace all content (brand name, tagline, services, copy, reviews)
5. Replace all Unsplash image URLs
6. Replace the demo banner label text
7. Verify locally, commit

---

### Task 4: demo-autorepair.html

**Files:**
- Create: `demo-autorepair.html` (copy of `demo-plumbing.html` as base)

- [ ] **Step 1: Copy `demo-plumbing.html` to `demo-autorepair.html`**

  ```bash
  cp demo-plumbing.html demo-autorepair.html
  ```

- [ ] **Step 2: Replace `<title>` and meta description**

  ```html
  <title>Desert Ridge Auto — Mesa Auto Repair</title>
  <meta name="description" content="Honest, fast auto repair in Mesa, AZ. Oil changes, brakes, diagnostics, and more.">
  ```

- [ ] **Step 3: Replace Google Fonts import**

  Change the existing font import to:
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  ```
  (Plumbing already uses these — verify they are present; if not, add them)

- [ ] **Step 4: Replace color variables and demo banner**

  Replace the demo banner label with: `Auto Repair Demo`

  Replace all instances of the plumbing accent color (`#1d4ed8` blue) with `#ea580c` (orange).
  Replace all instances of the plumbing dark bg (`#08121e` or similar dark navy) with `#1a1a1a` (charcoal).

- [ ] **Step 5: Replace hero content**

  - Hero bg image URL: `https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=1600&q=80`
  - Brand name: `Desert Ridge Auto`
  - Tagline: `Phoenix's Trusted Auto Repair Shop`
  - Location badge: `Mesa, AZ`
  - Hero subheadline: `Honest repairs. Fair prices. Done right the first time.`
  - CTA buttons: `Get a Free Estimate` (primary) · `Call (480) 555-0191` (secondary)

- [ ] **Step 6: Replace services section**

  6 service cards:
  - Oil Change & Fluids
  - Brake Repair
  - AC & Heating
  - Engine Diagnostics
  - Tire Services
  - Transmission

- [ ] **Step 7: Replace process section (unique to this demo)**

  Replace the plumbing "How It Works" steps with a 4-step "What to Expect" strip:
  - Step 1: Drop Off — "Leave your vehicle with us — no appointment needed"
  - Step 2: Diagnosis — "We inspect and call you with a clear estimate before any work begins"
  - Step 3: Approval — "You say go, we get it done — same day for most repairs"
  - Step 4: Pick Up — "Your vehicle is ready, cleaned, and waiting for you"

- [ ] **Step 8: Replace trust badges strip**

  3 badges: `ASE Certified` · `Loaner Vehicles Available` · `12-Month Warranty`

- [ ] **Step 9: Replace photo CTA band**

  - Image: `https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1600&q=80`
  - Headline: `Don't wait for a small problem to become a big one.`
  - CTA button: `Get a Free Estimate →`
  - Phone: `(480) 555-0191`

- [ ] **Step 10: Replace reviews**

  - "Brought my truck in for brakes and they had it done same day. Fair price, no runaround." — Mike T., Mesa ★★★★★
  - "They diagnosed an issue two other shops missed. Honest and fast." — Sandra R., Gilbert ★★★★★
  - "Been taking my cars here for 3 years. Never felt like I was getting ripped off." — James K., Chandler ★★★★★

- [ ] **Step 11: Replace footer brand name, phone, and location**

  - Name: `Desert Ridge Auto`
  - Location: `Mesa, AZ`
  - Phone: `(480) 555-0191`

- [ ] **Step 12: Open `demo-autorepair.html` in browser — verify no plumbing colors remain, images load, all sections present**

- [ ] **Step 13: Commit**

  ```bash
  git add demo-autorepair.html
  git commit -m "Add Auto Repair demo — Desert Ridge Auto"
  ```

---

### Task 5: demo-cleaning.html

**Files:**
- Create: `demo-cleaning.html` (copy of `demo-plumbing.html` as base)

- [ ] **Step 1: Copy base file**

  ```bash
  cp demo-plumbing.html demo-cleaning.html
  ```

- [ ] **Step 2: Replace `<title>` and meta**

  ```html
  <title>Spotless Valley Cleaning — Chandler Home &amp; Office Cleaning</title>
  <meta name="description" content="Reliable home and office cleaning in Chandler, AZ. Recurring, deep clean, and move-out services.">
  ```

- [ ] **Step 3: Replace fonts**

  ```html
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  ```

  Replace all CSS font references from Barlow Condensed / DM Sans to `'Plus Jakarta Sans', sans-serif`.

- [ ] **Step 4: Replace color scheme**

  This demo is intentionally light/airy — the dominant bg is white, NOT dark.
  - Primary accent: `#0d9488` (teal)
  - Body bg: `#ffffff`
  - Section alt bg: `#f0fdfa` (very light teal tint)
  - Dark text: `#111827`
  - Replace all navy/dark plumbing bg values with `#ffffff` or `#f9fafb`
  - Hero section: use a light overlay (semi-transparent white) instead of dark overlay

- [ ] **Step 5: Replace demo banner label**

  `Cleaning Service Demo`

- [ ] **Step 6: Replace hero content**

  - Hero bg image: `https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1600&q=80`
  - Hero overlay: `rgba(13,148,136,0.55)` (teal tint, not dark)
  - Brand name: `Spotless Valley Cleaning`
  - Tagline: `Home & Office Cleaning You Can Trust`
  - Location badge: `Chandler, AZ`
  - Subheadline: `Professional, reliable cleaning services for homes and offices across the East Valley.`
  - CTAs: `Get a Free Quote` (primary) · `Call (480) 555-0274` (secondary)

- [ ] **Step 7: Replace services section**

  6 service cards:
  - Standard Clean
  - Deep Clean
  - Move-In / Move-Out
  - Office Cleaning
  - Post-Construction
  - Recurring Plans

- [ ] **Step 8: Replace process section with "What's Included" checklist**

  Replace the step-by-step process section with a two-column checklist card:
  - Left column: Kitchen (counters, sink, appliances outside), Bathrooms (toilets, tubs, mirrors, floors), Living Areas (dust surfaces, vacuum, mop)
  - Right column: Bedrooms (dust, vacuum, make beds on request), Windows (interior sills and glass), Extras on Deep Clean (inside oven, fridge, baseboards)

- [ ] **Step 9: Replace CTA band**

  - Image: `https://images.unsplash.com/photo-1563453392212-326f5e854473?w=1600&q=80`
  - Overlay: `rgba(13,148,136,0.7)`
  - Headline: `A cleaner space. Less stress. Every week.`
  - CTA: `Book Your First Clean →`
  - Phone: `(480) 555-0274`

- [ ] **Step 10: Replace reviews**

  - "My house has never looked this good. They got things I didn't even know were dirty." — Laura M., Chandler ★★★★★
  - "Super reliable, always on time, and they remember how I like things done." — David P., Gilbert ★★★★★
  - "Used them for a move-out clean. Got my full deposit back. Worth every penny." — Priya N., Tempe ★★★★★

- [ ] **Step 11: Replace footer**

  - Name: `Spotless Valley Cleaning`
  - Location: `Chandler, AZ`
  - Phone: `(480) 555-0274`

- [ ] **Step 12: Open in browser — verify bright/airy feel (not dark), teal accents, all images load**

- [ ] **Step 13: Commit**

  ```bash
  git add demo-cleaning.html
  git commit -m "Add Cleaning Service demo — Spotless Valley Cleaning"
  ```

---

### Task 6: demo-pestcontrol.html

**Files:**
- Create: `demo-pestcontrol.html` (copy of `demo-plumbing.html` as base)

- [ ] **Step 1: Copy base file**

  ```bash
  cp demo-plumbing.html demo-pestcontrol.html
  ```

- [ ] **Step 2: Replace `<title>` and meta**

  ```html
  <title>Arizona Shield Pest Control — Phoenix Exterminator</title>
  <meta name="description" content="Same-day pest control in Phoenix, AZ. Scorpions, ants, termites, roaches, and more. 30-day guarantee.">
  ```

- [ ] **Step 3: Fonts** — keep Barlow Condensed + DM Sans (same as plumbing template)

- [ ] **Step 4: Replace color scheme**

  - Primary dark bg: `#1e3a5f` (navy)
  - Accent: `#16a34a` (green — same as Groundwork brand, works for pest/nature)
  - Replace all plumbing blue accents with `#16a34a`
  - Replace all plumbing dark navy bg values with `#1e3a5f`

- [ ] **Step 5: Replace demo banner label**

  `Pest Control Demo`

- [ ] **Step 6: Replace hero content**

  - Hero bg image: `https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1600&q=80`
  - Brand name: `Arizona Shield Pest Control`
  - Tagline: `Keep Your Home Pest-Free. Guaranteed.`
  - Location badge: `Phoenix, AZ`
  - Subheadline: `Fast, effective treatment for scorpions, ants, roaches, termites, and more. Same-day service available.`
  - CTAs: `Get a Free Inspection` (primary) · `Call (602) 555-0183` (secondary)

- [ ] **Step 7: Replace services section with "Pests We Handle" grid**

  8 items with emoji icons and labels:
  - 🦂 Scorpions
  - 🐜 Ants
  - 🪳 Cockroaches
  - 🐀 Rodents
  - 🪲 Termites
  - 🛏 Bed Bugs
  - 🕷 Spiders
  - 🐝 Wasps & Bees

- [ ] **Step 8: Add urgency band (unique section)**

  After the pests grid, add a full-width urgency strip:
  ```
  Background: #ea580c (orange-red — alarm color)
  Text: "Same-Day Service Available · Scorpions in Phoenix are active year-round. Don't wait."
  CTA button: "Schedule Today →"
  ```

- [ ] **Step 9: Replace CTA band**

  - Image: `https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1600&q=80`
  - Headline: `30-Day Re-Treatment Guarantee.`
  - Sub: `If pests come back within 30 days, we come back for free.`
  - CTA: `Get a Free Inspection →`
  - Phone: `(602) 555-0183`

- [ ] **Step 10: Replace reviews**

  - "Had a scorpion problem for years. One treatment and they've been gone for 6 months." — Carlos V., Phoenix ★★★★★
  - "Called at 8am, they were here by noon. Exactly what I needed." — Tammy W., Glendale ★★★★★
  - "Quarterly service keeps our restaurant 100% compliant. Reliable every time." — Ray L., Scottsdale ★★★★★

- [ ] **Step 11: Replace footer**

  - Name: `Arizona Shield Pest Control`
  - Location: `Phoenix, AZ`
  - Phone: `(602) 555-0183`

- [ ] **Step 12: Open in browser — verify navy bg, green accents, urgency band renders, scorpion emoji grid shows**

- [ ] **Step 13: Commit**

  ```bash
  git add demo-pestcontrol.html
  git commit -m "Add Pest Control demo — Arizona Shield Pest Control"
  ```

---

### Task 7: demo-gym.html

**Files:**
- Create: `demo-gym.html` (copy of `demo-plumbing.html` as base)

- [ ] **Step 1: Copy base file**

  ```bash
  cp demo-plumbing.html demo-gym.html
  ```

- [ ] **Step 2: Replace `<title>` and meta**

  ```html
  <title>Iron Valley Fitness — Scottsdale Gym</title>
  <meta name="description" content="Scottsdale's premier fitness gym. Classes, personal training, and memberships starting at $49/mo. Try your first week free.">
  ```

- [ ] **Step 3: Fonts** — keep Barlow Condensed + DM Sans

- [ ] **Step 4: Replace color scheme**

  - Primary bg: `#0a0a0a` (near-black)
  - Accent: `#facc15` (electric yellow)
  - Replace ALL plumbing blue/navy accents with `#facc15`
  - Replace all plumbing dark bg values with `#0a0a0a`
  - Note: yellow on dark — text on yellow buttons must be `#111827` (dark), not white

- [ ] **Step 5: Replace demo banner label**

  `Gym & Fitness Demo`

- [ ] **Step 6: Replace hero content**

  - Hero bg image: `https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1600&q=80`
  - Brand name: `Iron Valley Fitness`
  - Tagline: `Train Hard. Stay Consistent. See Results.`
  - Location badge: `Scottsdale, AZ`
  - Subheadline: `State-of-the-art equipment, expert coaches, and a community that keeps you coming back.`
  - CTAs: `Claim Your Free Week` (primary, yellow bg + dark text) · `View Memberships` (secondary, ghost)

- [ ] **Step 7: Replace services section with membership tiers**

  3 membership cards:
  - Day Pass — $15/day — Full facility access, no commitment
  - Monthly — $49/mo — Unlimited access, group classes included
  - Annual — $39/mo — Best value, billed annually, includes 1 personal training session/mo

- [ ] **Step 8: Add class schedule teaser (unique section)**

  Replace the process section with a class grid showing 6 class types:
  - HIIT — Mon/Wed/Fri 6am, 5pm
  - Strength — Tue/Thu 7am, 6pm
  - Yoga — Mon/Wed 7pm
  - Spin — Tue/Thu/Sat 6am
  - Boxing — Mon/Wed/Fri 7pm
  - Open Gym — Daily 5am–11pm

- [ ] **Step 9: Replace CTA band**

  - Image: `https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=1600&q=80`
  - Headline: `Your first week is on us.`
  - Sub: `No commitment. No credit card. Just show up.`
  - CTA: `Claim Free Week →` (yellow button, dark text)
  - Phone: `(480) 555-0317`

- [ ] **Step 10: Replace reviews**

  - "Best gym in Scottsdale. Equipment is always clean and the staff actually knows your name." — Ashley B., Scottsdale ★★★★★
  - "Lost 30 lbs in 4 months. The coaches here are the real deal." — Marcus T., Phoenix ★★★★★
  - "Switched from a big chain gym. Never going back. Community here is unmatched." — Nina R., Tempe ★★★★★

- [ ] **Step 11: Replace footer**

  - Name: `Iron Valley Fitness`
  - Location: `Scottsdale, AZ`
  - Phone: `(480) 555-0317`

- [ ] **Step 12: Open in browser — verify near-black bg, yellow accents, yellow buttons have dark text, all images load**

- [ ] **Step 13: Commit**

  ```bash
  git add demo-gym.html
  git commit -m "Add Gym & Fitness demo — Iron Valley Fitness"
  ```

---

## Chunk 3: Final Testing & Deploy

### Task 8: Full testing checklist

- [ ] **Step 1: Open `index.html` — verify 12 demo cards in the work grid**

- [ ] **Step 2: Click all 4 new demo card links — verify each page loads**

- [ ] **Step 3: Verify FAQ accordion in Chrome**
  - Click item 1 → opens, icon changes to −, question text turns green
  - Click item 2 → item 1 closes automatically, item 2 opens
  - Click item 2 again → item 2 closes (toggle off)
  - Hover any question button → verify text color transitions to green
  - All 7 items work

- [ ] **Step 4: Verify FAQ accordion in Safari**
  - Repeat all sub-checks from Step 3 in Safari

- [ ] **Step 5: Verify Why Not DIY? renders at 375px (Chrome DevTools)**
  - Table scrolls horizontally if needed, no layout breaks

- [ ] **Step 6: Verify FAQ at 375px — all questions readable, no overflow**

- [ ] **Step 7: Verify all 4 new demo pages at 375px — no broken layouts**

- [ ] **Step 8: Verify all 4 new demo pages at 1280px — no broken layouts**

- [ ] **Step 9: Check all Unsplash images load on each new demo page — open browser console (F12) on each page**
  - Confirm zero 404 errors for any image URL
  - Pay special attention to `demo-pestcontrol.html` CTA band image (`photo-1585771724684-38269d6639fd`) — verify it loads
  - If any image 404s, replace the URL with an equivalent working Unsplash photo

- [ ] **Step 10: Click "Why Not DIY?" nav link — scrolls to correct section**

- [ ] **Step 11: Click "FAQ" nav link — scrolls to correct section**

- [ ] **Step 11b: Open browser console on each of the 4 new demo pages — confirm zero JS errors in Chrome and Safari**

- [ ] **Step 11c: Verify all 4 new work grid cards show correct badge color and thumbnail image**
  - Auto Repair: orange badge, auto shop image
  - Cleaning: teal badge, cleaning image
  - Pest Control: navy badge, pest control image
  - Gym & Fitness: yellow badge (dark text), gym image

- [ ] **Step 12: Open contact form — verify dropdown includes Auto Repair, Pest Control, Gym / Fitness**

- [ ] **Step 13: Push to Netlify and test live form submission**

  ```bash
  git push origin main
  ```

  After deploy (~1 min): submit the quote form on the live site, confirm redirect to `/thank-you.html`

- [ ] **Step 14: Final commit if any fixes were needed during testing**

  ```bash
  git add -A
  git commit -m "Fix issues found during testing"
  git push origin main
  ```
