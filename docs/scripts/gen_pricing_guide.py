#!/usr/bin/env python3
"""Generate Groundwork Studio AZ LLC Client Pricing Guide PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import os, shutil

OUT_REPO = "/Users/evanbaukol/Sites/groundwork-studio/docs/Groundwork_Client_Pricing_Guide.pdf"
OUT_DESK = "/Users/evanbaukol/Desktop/Groundwork Studio \u2014 Docs/Groundwork_Client_Pricing_Guide.pdf"

# ── Colors ─────────────────────────────────────────────────────────────────────
GS_GREEN   = colors.HexColor("#16a34a")
GS_DARK    = colors.HexColor("#111827")
GS_GRAY    = colors.HexColor("#6b7280")
GS_LIGHT   = colors.HexColor("#f0fdf4")
GS_BORDER  = colors.HexColor("#d1fae5")
LINE       = colors.HexColor("#e5e7eb")
WHITE      = colors.white
GS_BLUE    = colors.HexColor("#eff6ff")
GS_BLUE_B  = colors.HexColor("#bfdbfe")
GS_BLUE_T  = colors.HexColor("#1d4ed8")

# ── Styles ─────────────────────────────────────────────────────────────────────
def sty(name, **kw): return ParagraphStyle(name, **kw)

LABEL_TOP = sty("LABEL_TOP", fontSize=9,   fontName="Helvetica-Bold", textColor=GS_GREEN,
                alignment=TA_CENTER, letterSpacing=3, spaceAfter=0)
TITLE     = sty("TITLE",     fontSize=26,  fontName="Helvetica-Bold", textColor=GS_DARK,
                alignment=TA_CENTER, spaceAfter=0, leading=30)
SUBTITLE  = sty("SUBTITLE",  fontSize=10,  fontName="Helvetica",      textColor=GS_GRAY,
                alignment=TA_CENTER, spaceAfter=0)
LABEL     = sty("LABEL",     fontSize=7.5, fontName="Helvetica-Bold", textColor=GS_GREEN,
                spaceAfter=4, spaceBefore=4, letterSpacing=1.5)
H2        = sty("H2",        fontSize=13,  fontName="Helvetica-Bold", textColor=GS_DARK,
                spaceAfter=6, spaceBefore=0)
BODY      = sty("BODY",      fontSize=9,   fontName="Helvetica",      textColor=GS_DARK,
                spaceAfter=4, leading=14)
BODYJ     = sty("BODYJ",     fontSize=9,   fontName="Helvetica",      textColor=GS_DARK,
                spaceAfter=4, leading=14, alignment=TA_JUSTIFY)
SMALL     = sty("SMALL",     fontSize=7.5, fontName="Helvetica",      textColor=GS_GRAY,
                spaceAfter=2, leading=12, alignment=TA_CENTER)
SMALLL    = sty("SMALLL",    fontSize=7.5, fontName="Helvetica",      textColor=GS_GRAY,
                spaceAfter=2, leading=12)

def hr(color=LINE, t=0.75): return HRFlowable(width="100%", thickness=t, color=color,
                                               spaceAfter=8, spaceBefore=4)
def blank(h=0.1):            return Spacer(1, h*inch)

FOOTER = "Groundwork Studio \u00b7 teamground.work \u00b7 evan@teamground.work \u00b7 (480) 452-6473 \u00b7 Phoenix, AZ"

def footer(): return [blank(0.12), hr(GS_BORDER), Paragraph(FOOTER, SMALL)]

def cell(text, bold=False, size=9, color=GS_DARK, align=TA_LEFT, leading=13):
    return Paragraph(text, sty(f"c_{hash(text+str(bold)+str(size))}",
                               fontSize=size,
                               fontName="Helvetica-Bold" if bold else "Helvetica",
                               textColor=color, alignment=align, leading=leading))


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 1  —  INTRO + WHAT YOU'RE PAYING FOR + GUARANTEE
# ═══════════════════════════════════════════════════════════════════════════════
def page_intro():
    s = []

    # Header — label / title / divider / subtitle
    s += [
        blank(0.25),
        Paragraph("GROUNDWORK STUDIO", LABEL_TOP),
        blank(0.12),
        Paragraph("Client Pricing Guide", TITLE),
        blank(0.14),
        Paragraph("Clean, fast websites for local businesses \u2014 built in days, not months.", SUBTITLE),
        blank(0.22),
        hr(GS_GREEN, 2),
        blank(0.18),
    ]

    # What You're Paying For
    s += [
        Paragraph("WHAT YOU\u2019RE PAYING FOR", LABEL),
        Paragraph(
            "Every site we build is designed and coded from scratch \u2014 no drag-and-drop builders, "
            "no templates from a library, no recycled layouts. Each page is custom-written, "
            "mobile-optimized, and built for speed and search visibility. Here\u2019s what\u2019s "
            "included in every build, regardless of tier:",
            BODYJ),
        blank(0.08),
    ]

    includes = [
        ("Custom Design",
         "Your site is built to match your brand \u2014 not a template. Colors, layout, fonts, "
         "and tone are all tailored to your business and the customers you\u2019re trying to reach."),
        ("Mobile-First Build",
         "Over 60% of local service searches happen on a phone. Every page is designed to look "
         "and work perfectly on mobile before anything else."),
        ("Fast Load Times",
         "We use lightweight, hand-coded HTML and CSS \u2014 no bloated plugins or page builders. "
         "Google rewards fast sites with higher rankings. Slow sites lose customers before the "
         "page even loads."),
        ("SEO-Ready Structure",
         "Page titles, headings, meta descriptions, and URL structure are all set up correctly "
         "from day one. You won\u2019t need to hire an SEO consultant just to get found locally."),
        ("Copywriting Included",
         "We write the words on your site \u2014 not just the layout. You provide the facts; we "
         "turn them into clear, professional copy that speaks to your customers and drives action."),
        ("2 Rounds of Revisions",
         "Every build includes two full rounds of revisions. We don\u2019t go live until you give "
         "the sign-off \u2014 your satisfaction is part of the deliverable."),
    ]

    rows = [[cell(f"<b>{t}</b>", size=9, leading=14), cell(d, size=9, leading=14)]
            for t, d in includes]
    t = Table(rows, colWidths=[1.55*inch, 4.7*inch])
    t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("VALIGN",         (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",     (0,0),(-1,-1), 6),
        ("BOTTOMPADDING",  (0,0),(-1,-1), 6),
        ("LEFTPADDING",    (0,0),(-1,-1), 8),
        ("RIGHTPADDING",   (0,0),(-1,-1), 8),
        ("GRID",           (0,0),(-1,-1), 0.5, LINE),
        ("FONTNAME",       (0,0),(0,-1),  "Helvetica-Bold"),
    ]))
    s += [t, blank(0.14)]

    # 35-Day Guarantee banner
    gg_t = Table(
        [
            [cell("35-DAY SATISFACTION GUARANTEE", bold=True, size=11, color=GS_GREEN, leading=15)],
            [Paragraph(
                "If your site goes live and you\u2019re not satisfied \u2014 or it hasn\u2019t "
                "generated results within <b>35 days of launch</b> \u2014 we\u2019ll refund your "
                "full build fee. No hoops. Just a written request within the window and we\u2019ll "
                "process it within 5 business days.",
                sty("gg_p1", fontSize=9, fontName="Helvetica", textColor=GS_DARK, leading=14))],
        ],
        colWidths=[6.25*inch]
    )
    gg_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
        ("BOX",           (0,0),(-1,-1), 1.5, GS_GREEN),
        ("TOPPADDING",    (0,0),(0,0),  11),
        ("BOTTOMPADDING", (0,0),(0,0),   4),
        ("TOPPADDING",    (0,1),(0,1),   3),
        ("BOTTOMPADDING", (0,1),(0,1),  12),
        ("LEFTPADDING",   (0,0),(-1,-1), 16),
        ("RIGHTPADDING",  (0,0),(-1,-1), 16),
    ]))
    s += [gg_t]

    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 2  —  HOW IT WORKS + SITE TIERS OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
def page_tiers_overview():
    s = [PageBreak()]

    # How It Works
    s += [
        Paragraph("HOW IT WORKS \u2014 FROM SIGN-OFF TO LAUNCH", LABEL),
        blank(0.04),
    ]

    steps = [
        ("1", "Pick Your Tier",    "Choose the tier that fits. Tiers are baselines \u2014 you\u2019re free to add or swap pages."),
        ("2", "Pay 50% to Start",  "Work begins on deposit. Most sites live within 1\u20132 weeks from content received."),
        ("3", "Send Your Content", "Logo, photos, and any text you want included. We help shape it and make it great."),
        ("4", "Review & Approve",  "2 full rounds of revisions. We don\u2019t go live until you sign off."),
        ("5", "Pay Balance, Go Live", "Final 50% due on launch day. Site goes live the moment payment clears."),
    ]

    step_cells = []
    for n, title, desc in steps:
        box = Table(
            [[cell(n, bold=True, size=16, color=GS_GREEN, align=TA_CENTER)],
             [cell(f"<b>{title}</b>", size=8, align=TA_CENTER)],
             [cell(desc, size=7.5, color=GS_GRAY, align=TA_CENTER, leading=11)]],
            colWidths=[1.15*inch]
        )
        box.setStyle(TableStyle([
            ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
            ("BOX",           (0,0),(-1,-1), 1.0, GS_BORDER),
            ("TOPPADDING",    (0,0),(-1,-1), 8),
            ("BOTTOMPADDING", (0,0),(-1,-1), 8),
            ("LEFTPADDING",   (0,0),(-1,-1), 4),
            ("RIGHTPADDING",  (0,0),(-1,-1), 4),
            ("ALIGN",         (0,0),(-1,-1), "CENTER"),
        ]))
        step_cells.append(box)
        if n != "5":
            step_cells.append(Table(
                [[cell("\u2192", bold=True, size=12, color=GS_GREEN, align=TA_CENTER)]],
                colWidths=[0.2*inch]
            ))

    col_ws = []
    for i in range(5):
        col_ws.append(1.15*inch)
        if i < 4: col_ws.append(0.2*inch)

    proc_t = Table([step_cells], colWidths=col_ws)
    proc_t.setStyle(TableStyle([
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("ALIGN",        (0,0),(-1,-1), "CENTER"),
        ("LEFTPADDING",  (0,0),(-1,-1), 0),
        ("RIGHTPADDING", (0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1), 0),
    ]))
    s += [proc_t, blank(0.2), hr()]

    # Site Tiers Overview
    s += [
        blank(0.05),
        Paragraph("SITE TIERS \u2014 YOUR STARTING POINT", LABEL),
        Paragraph(
            "Tiers are baselines, not boxes. The tier you choose sets your page count and starting "
            "price. You can add pages, remove them, or mix across tiers. Every tier includes "
            "service detail sections \u2014 you give us the content, we make it shine.",
            BODYJ),
        blank(0.06),
        Paragraph(
            "<b>What is a page?</b>  Each distinct URL counts as one page "
            "(e.g., Home, Services, About, Contact = 4 pages). More pages = deeper content, "
            "better SEO, more room to convert visitors.",
            BODY),
        blank(0.1),
    ]

    tier_hdr  = ["TIER 1\nFoundation\n$1,000", "TIER 2\nStandard\n$1,500",
                 "TIER 3\nElevated\n$2,000",   "TIER 4\nPremium\n$2,500"]
    tier_desc = [
        "1 page \u00b7 Home, Services, Areas We Serve, Contact + Scheduling",
        "Tier 1 + About, Gallery, Reviews, FAQ",
        "Tier 2 + Financing \u00b7 Specials \u00b7 Blog (1\u20137 pages, varies by industry)",
        "Tier 3 + Online Booking + Deep SEO \u2014 8\u201311 pages",
    ]
    tier_fit  = [
        "New businesses establishing a clean, professional online presence",
        "Growing businesses that need trust signals and social proof",
        "Full-featured build for established businesses",
        "Full suite for businesses that want to dominate locally",
    ]

    tier_t = Table(
        [[cell(h, bold=True, size=9, color=WHITE, align=TA_CENTER, leading=13) for h in tier_hdr],
         [cell(d, size=8.5, align=TA_CENTER, leading=13) for d in tier_desc],
         [cell(f, size=8, color=GS_GRAY, align=TA_CENTER, leading=12) for f in tier_fit]],
        colWidths=[1.5625*inch]*4
    )
    tier_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0), GS_GREEN),
        ("BACKGROUND",    (0,1),(-1,1), GS_LIGHT),
        ("GRID",          (0,0),(-1,-1), 0.5, GS_BORDER),
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 9),
        ("BOTTOMPADDING", (0,0),(-1,-1), 9),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ]))
    s += [tier_t, blank(0.08)]
    s += [Paragraph(
        "Mix pages from any tier, skip what you don\u2019t need, or go fully custom. "
        "Custom estimates available \u2014 just ask.",
        sty("tier_note", fontSize=8, fontName="Helvetica", textColor=GS_GRAY,
            alignment=TA_CENTER, leading=12))]

    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 3  —  WHAT EACH TIER GETS YOU (DETAIL)
# ═══════════════════════════════════════════════════════════════════════════════
def page_tier_detail():
    s = [PageBreak()]

    s += [
        Paragraph("WHAT EACH TIER GETS YOU \u2014 IN PLAIN TERMS", LABEL),
        blank(0.06),
    ]

    tier_details = [
        ("Tier 1\nFoundation\n$1,000",
         "1 page \u2014 Home, Services Overview, Areas We Serve, Contact + Scheduling. "
         "Service detail sections built in for every service you offer.",
         "$1,000 is not a template. Every pixel is designed and coded for your business \u2014 "
         "your brand, your services, your customers. Includes copywriting, mobile optimization, "
         "SEO-ready structure, and full hosting setup. That\u2019s the price."),
        ("Tier 2\nStandard\n$1,500",
         "Everything in Tier 1, plus About, Gallery, Reviews, and FAQ sections.",
         "The extra $500 adds four high-converting sections. An About page increases contact "
         "rates \u2014 people want to know who they\u2019re letting in. Gallery and Reviews give "
         "visitors the proof they need. FAQ cuts down on repetitive calls. Each section takes "
         "real design and writing time."),
        ("Tier 3\nElevated\n$2,000",
         "1\u20137 pages \u2014 Everything in Tier 2, plus Financing Page, Specials Page, and Blog. "
         "Exact configuration varies by industry.",
         "At this level you\u2019re building a complete online business presence. Financing pages "
         "remove the biggest objection before a customer calls. A blog and specials page give you "
         "a place to run offers and publish content without rebuilding the site. This is the tier "
         "most established service businesses end up wanting."),
        ("Tier 4\nPremium\n$2,500",
         "8\u201311 pages \u2014 Everything in Tier 3, plus Online Booking System and Deep SEO "
         "Architecture across every page.",
         "$2,500 reflects the full scope: a booking system requires integration and multi-device "
         "testing; 8\u201311 pages means 8\u201311 individually designed, written, and optimized "
         "pages. Deep SEO architecture means every page is built to rank. This tier is for "
         "businesses that want to dominate their local market."),
    ]

    hdr = [cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER)
           for h in ["TIER", "PAGES INCLUDED", "WHY THIS PRICE"]]
    rows = [[cell(t, bold=True, size=9, color=GS_DARK, leading=14),
             cell(p, size=8.5, leading=13),
             cell(w, size=8.5, leading=13)]
            for t, p, w in tier_details]

    td_t = Table([hdr] + rows, colWidths=[1.05*inch, 2.25*inch, 2.95*inch])
    td_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 10),
        ("BOTTOMPADDING", (0,0),(-1,-1), 10),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ]))
    s += [td_t]

    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 4  —  MONTHLY PLANS
# ═══════════════════════════════════════════════════════════════════════════════
def page_monthly():
    s = [PageBreak()]

    s += [
        Paragraph("MONTHLY PLANS \u2014 KEEPING YOUR SITE RUNNING", LABEL),
        Paragraph(
            "Once your site is live, the <b>Maintenance Plan is required</b> to keep your site "
            "online \u2014 it covers hosting, SSL, uptime monitoring, and content updates. "
            "The <b>Growth Plan is completely optional</b> and is for businesses that want active "
            "Google presence management, review monitoring, and ongoing SEO work. "
            "You can start on Maintenance and upgrade to Growth at any time.",
            BODYJ),
        blank(0.12),
    ]

    mh = [cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER)
          for h in ["TIER", "MONTHLY RATE", "WHAT\u2019S INCLUDED"]]

    maint_rows = [
        ("T1 Foundation", "$125/mo",
         "Netlify hosting on a global CDN, SSL certificate (HTTPS), uptime monitoring with alerts, "
         "all security and platform updates, minor content edits on request (up to 1 hr/month), "
         "and a monthly uptime report sent to you."),
        ("T2 Standard",  "$150/mo", "Everything above. Slightly more surface area to maintain and monitor each month."),
        ("T3 Elevated",  "$175/mo", "Everything above. More pages means more content to update, more links to verify, and a larger site to keep optimized."),
        ("T4 Premium",   "$200/mo", "Everything above. 8\u201311 pages plus booking integration and deep SEO architecture require the most ongoing attention."),
    ]
    mr = [[cell(t, bold=True, size=9), cell(r, bold=True, size=11, color=GS_GREEN, align=TA_CENTER), cell(d, size=8.5, leading=13)]
          for t, r, d in maint_rows]
    mt = Table([mh] + mr, colWidths=[1.1*inch, 1.1*inch, 4.05*inch])
    mt.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
        ("ALIGN",         (0,1),(1,-1),  "CENTER"),
        ("VALIGN",        (0,1),(1,-1),  "MIDDLE"),
    ]))

    s += [
        Paragraph("MAINTENANCE PLAN", sty("mp_lbl", fontSize=8, fontName="Helvetica-Bold",
                  textColor=GS_GREEN, letterSpacing=1.5, spaceAfter=6)),
        mt,
        blank(0.04),
        Paragraph(
            "Why the rate varies by tier: More pages means more to monitor, maintain, and update. "
            "The rate reflects actual time spent. Most clients choose this plan. "
            "Less than a tank of gas per month.",
            SMALLL),
        blank(0.18),
    ]

    gh = [cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER)
          for h in ["TIER", "MONTHLY RATE", "WHAT\u2019S INCLUDED"]]
    growth_rows = [
        ("T1 Foundation", "$275/mo",
         "Everything in Maintenance, plus 1\u20133 Google Business Profile posts per month, "
         "responses to all new Google reviews, monthly SEO refresh (meta titles and descriptions "
         "updated), and a monthly keyword ranking report."),
        ("T2 Standard",  "$300/mo", "Everything in T1 Growth. Additional SEO surface area across added pages."),
        ("T3 Elevated",  "$350/mo", "Everything above, plus proactive review generation strategy, page copy optimization, and quarterly competitor keyword gap analysis."),
        ("T4 Premium",   "$425/mo", "Everything above across all 8\u201311 pages. Maximum SEO investment for businesses that want to dominate local search."),
    ]
    gr = [[cell(t, bold=True, size=9), cell(r, bold=True, size=11, color=GS_GREEN, align=TA_CENTER), cell(d, size=8.5, leading=13)]
          for t, r, d in growth_rows]
    gt = Table([gh] + gr, colWidths=[1.1*inch, 1.1*inch, 4.05*inch])
    gt.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
        ("ALIGN",         (0,1),(1,-1),  "CENTER"),
        ("VALIGN",        (0,1),(1,-1),  "MIDDLE"),
    ]))

    s += [
        Paragraph("GROWTH PLAN \u2014 OPTIONAL UPGRADE",
                  sty("gp_lbl", fontSize=8, fontName="Helvetica-Bold",
                      textColor=GS_GREEN, letterSpacing=1.5, spaceAfter=4)),
        Paragraph(
            "Not required \u2014 add this if you want active Google presence management, "
            "review monitoring, keyword tracking, and ongoing SEO. Cancel anytime with 30 days notice.",
            sty("gp_intro", fontSize=8.5, fontName="Helvetica", textColor=GS_GRAY,
                leading=13, spaceAfter=8)),
        gt,
        blank(0.04),
        Paragraph(
            "Why it costs more: Real, ongoing work each month \u2014 writing posts, monitoring "
            "rankings, responding to reviews, and making data-driven adjustments. "
            "Not automated. A real person working on your Google presence every month.",
            SMALLL),
    ]

    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 5  —  NEXTDOOR + ADD-ON SERVICES
# ═══════════════════════════════════════════════════════════════════════════════
def page_addons():
    s = [PageBreak()]

    # Nextdoor
    s += [
        Paragraph("LOCAL PRESENCE ADD-ON \u2014 NEXTDOOR MANAGEMENT", LABEL),
    ]
    nd_t = Table(
        [[cell("PRICE", bold=True, size=8, color=WHITE, align=TA_CENTER),
          cell("WHAT\u2019S INCLUDED", bold=True, size=8, color=WHITE, align=TA_CENTER)],
         [cell("$49/mo +\n$99 setup\n(any tier)", bold=True, size=10, color=GS_GREEN,
               align=TA_CENTER, leading=14),
          cell(
            "$99 Setup: We create and fully configure your Nextdoor Business page. "
            "Monthly: One neighborhood post written and published per month, monitoring for "
            "neighbor recommendations and service requests, responding to messages in your area. "
            "<b>Why Nextdoor matters:</b> Most homeowners don\u2019t Google for a plumber or "
            "roofer \u2014 they ask their neighbors. Nextdoor is where those conversations happen. "
            "Flat rate \u2014 same price regardless of tier.",
            size=8.5, leading=13)]],
        colWidths=[1.3*inch, 4.95*inch]
    )
    nd_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0), GS_GREEN),
        ("BACKGROUND",    (0,1),(-1,1), GS_LIGHT),
        ("GRID",          (0,0),(-1,-1), 0.5, GS_BORDER),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 9),
        ("BOTTOMPADDING", (0,0),(-1,-1), 9),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ]))
    s += [nd_t, blank(0.06)]
    s += [Paragraph(
        "If you cancel your monthly plan, your site will go offline. "
        "A $250 migration fee applies if you\u2019d like the site files transferred to a new host.",
        SMALLL), blank(0.16), hr()]

    # Add-On Services
    s += [
        blank(0.05),
        Paragraph("ADD-ON SERVICES \u2014 OPTIONAL EXTRAS", LABEL),
        Paragraph("Nothing below is bundled in unless you choose it. Available with any tier.", BODY),
        blank(0.08),
    ]

    ah = [cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER)
          for h in ["ADD-ON", "PRICE", "WHAT YOU GET \u2014 AND WHY IT\u2019S PRICED THIS WAY"]]

    addons = [
        ("Logo & Brand Identity",       "$300 \u2013 $600",
         "A professionally designed logo and full brand kit \u2014 color palette, fonts, and logo "
         "files in all formats (PNG, SVG, PDF). Simple wordmark is $300; custom icon-based logo "
         "with full brand guidelines is $600. Delivered before the site launches so everything matches."),
        ("Google Business Profile Setup", "$200 \u2013 $350",
         "We create or claim your Google Business listing, upload photos, write your business "
         "description, configure your service list and hours, and complete full verification. "
         "Range reflects whether the listing exists and needs cleanup ($200) or needs to be built "
         "from scratch ($350)."),
        ("Local SEO Setup",              "$250\none-time",
         "<b>Done once, done right.</b>  Google Business Profile setup and optimization, schema "
         "markup (tells Google your exact business type, location, and services), citation "
         "submissions to Yelp, BBB, and Apple Maps, plus a keyword research doc for your top 5 "
         "search terms. No monthly fees \u2014 one flat add-on to your build. The fastest way to "
         "start showing up in local searches from day one."),
        ("SEO Foundation Package",       "$400 \u2013 $700",
         "Keyword research specific to your service area, meta titles and descriptions written for "
         "every page, schema markup, and sitemap submission to Google Search Console. Range reflects "
         "site size \u2014 Tier 1 is $400; Tier 4 is closer to $700."),
        ("Booking / Scheduling Integration", "$300 \u2013 $500",
         "Connects an online booking tool (Calendly, Square Appointments, or Acuity) to your site "
         "so customers can schedule without calling. Price reflects integration complexity and "
         "whether a new account needs setup."),
        ("Google & Meta Ads Setup",      "$400 setup +\n10\u201315%/mo\nof ad spend",
         "We build and manage paid ad campaigns on Google Search and/or Facebook/Instagram targeting "
         "customers in your service area. You control the budget. The setup fee covers campaign "
         "architecture and ad copy; monthly percentage covers ongoing management and reporting."),
        ("Domain Registration & Setup",  "$50 \u2013 $75",
         "We handle the domain purchase and full DNS connection \u2014 no GoDaddy account needed. "
         "Alternatively, buy your own domain ($12\u2013$15/yr) and we connect it at no extra charge. "
         "The $50\u2013$75 is for the purchase and setup service only."),
        ("Rush Delivery",                "+25% of\nbuild fee",
         "Guarantees your project moves to the front of the queue and is completed in under 2 weeks. "
         "Standard turnaround is already 1\u20132 weeks \u2014 rush delivery reserves dedicated "
         "focus time and may require evening or weekend work to hit the deadline."),
    ]

    seo_idx = next(i+1 for i, (t,_,_) in enumerate(addons) if "Local SEO" in t)

    ar = [[cell(t, bold=True, size=9, color=GS_DARK, leading=13),
           cell(p, bold=True, size=9, color=GS_GREEN, align=TA_CENTER, leading=13),
           cell(d, size=8.5, leading=13)]
          for t, p, d in addons]

    at = Table([ah] + ar, colWidths=[1.45*inch, 0.9*inch, 3.9*inch])
    at.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),            GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),           [WHITE, colors.HexColor("#f9fafb")]),
        ("BACKGROUND",    (0,seo_idx),(-1,seo_idx), GS_BLUE),
        ("BOX",           (0,seo_idx),(-1,seo_idx), 1.0, GS_BLUE_B),
        ("GRID",          (0,0),(-1,-1),            0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1),            "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1),            7),
        ("BOTTOMPADDING", (0,0),(-1,-1),            7),
        ("LEFTPADDING",   (0,0),(-1,-1),            8),
        ("RIGHTPADDING",  (0,0),(-1,-1),            8),
        ("ALIGN",         (0,1),(1,-1),             "CENTER"),
        ("TEXTCOLOR",     (1,seo_idx),(1,seo_idx),  GS_BLUE_T),
    ]))
    s += [at]

    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 6  —  GOOD TO KNOW + CTA
# ═══════════════════════════════════════════════════════════════════════════════
def page_good_to_know():
    s = [PageBreak()]

    s += [
        Paragraph("GOOD TO KNOW", LABEL),
        blank(0.06),
    ]

    gk_rows = [
        ("Revisions",
         "2 full rounds included. One consolidated list of changes per round \u2014 not individual "
         "requests spread over days. Additional rounds are $75/hour."),
        ("Content Deadline",
         "Logo, photos, and copy due within 14 days of signing. After that, a $200 delay fee "
         "applies and your timeline shifts accordingly."),
        ("Ownership",
         "Your text, photos, and copy are yours. The underlying code belongs to Groundwork Studio "
         "until the build fee is paid in full. Cancel your monthly plan and a $250 migration fee "
         "applies to transfer files to a new host."),
        ("Custom Quotes",
         "Tiers are starting points. Mix pages from any tier, skip what you don\u2019t need, or "
         "go fully custom. Contact us for an exact quote."),
    ]

    gk_data = [[cell(k, bold=True, size=9, color=GS_GREEN, leading=13),
                cell(v, size=9, leading=13)] for k, v in gk_rows]
    gk_t = Table(gk_data, colWidths=[1.45*inch, 4.8*inch])
    gk_t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("GRID",           (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",         (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",     (0,0),(-1,-1), 9),
        ("BOTTOMPADDING",  (0,0),(-1,-1), 9),
        ("LEFTPADDING",    (0,0),(-1,-1), 8),
        ("RIGHTPADDING",   (0,0),(-1,-1), 8),
    ]))
    s += [gk_t, blank(0.3)]

    # CTA
    s += [
        hr(GS_GREEN, 2),
        blank(0.18),
        Paragraph("Ready to get started?", sty("cta_h", fontSize=16, fontName="Helvetica-Bold",
                  textColor=GS_DARK, alignment=TA_CENTER, spaceAfter=0)),
        blank(0.1),
        Paragraph(
            "Text or call <b>(480) 452-6473</b>  \u00b7  Email <b>evan@teamground.work</b>  "
            "\u00b7  See examples at <b>teamground.work</b>",
            sty("cta_body", fontSize=10, fontName="Helvetica", textColor=GS_GRAY,
                alignment=TA_CENTER, leading=15)),
        blank(0.18),
        hr(GS_GREEN, 2),
    ]

    s += [blank(0.08), hr(GS_BORDER), Paragraph(FOOTER, SMALL)]
    return s


# ═══════════════════════════════════════════════════════════════════════════════
def story():
    return (page_intro() + page_tiers_overview() + page_tier_detail() +
            page_monthly() + page_addons() + page_good_to_know())


def build():
    os.makedirs(os.path.dirname(OUT_REPO), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT_REPO, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.65*inch, bottomMargin=0.65*inch,
        title="Groundwork Studio \u2014 Client Pricing Guide",
        author="Groundwork Studio AZ LLC",
    )
    doc.build(story())
    shutil.copy(OUT_REPO, OUT_DESK)
    print(f"\u2713 Pricing Guide saved to:\n  {OUT_REPO}\n  {OUT_DESK}")


if __name__ == "__main__":
    build()
