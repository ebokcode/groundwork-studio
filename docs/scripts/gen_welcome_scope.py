#!/usr/bin/env python3
"""Generate Groundwork Studio AZ LLC Welcome & Scope Document PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import os, shutil

OUT_REPO = "/Users/evanbaukol/Sites/groundwork-studio/docs/Groundwork_Welcome_Scope.pdf"
OUT_DESK = "/Users/evanbaukol/Desktop/Groundwork Studio \u2014 Docs/Groundwork_Welcome_Scope.pdf"

GS_GREEN  = colors.HexColor("#16a34a")
GS_DARK   = colors.HexColor("#111827")
GS_GRAY   = colors.HexColor("#6b7280")
GS_LIGHT  = colors.HexColor("#f0fdf4")
GS_BORDER = colors.HexColor("#d1fae5")
GS_MID    = colors.HexColor("#dcfce7")
LINE      = colors.HexColor("#e5e7eb")
WHITE     = colors.white

def sty(name, **kw): return ParagraphStyle(name, **kw)

TITLE  = sty("TITLE",  fontSize=20, fontName="Helvetica-Bold", textColor=GS_DARK,  alignment=TA_CENTER, spaceAfter=2)
SUB    = sty("SUB",    fontSize=9,  fontName="Helvetica",      textColor=GS_GRAY,  alignment=TA_CENTER, spaceAfter=4)
LABEL  = sty("LABEL",  fontSize=7.5,fontName="Helvetica-Bold", textColor=GS_GREEN, spaceAfter=2, spaceBefore=12, letterSpacing=1.5)
H2     = sty("H2",     fontSize=11, fontName="Helvetica-Bold", textColor=GS_DARK,  spaceAfter=4, spaceBefore=8)
BODY   = sty("BODY",   fontSize=9,  fontName="Helvetica",      textColor=GS_DARK,  spaceAfter=3, leading=14)
BODYJ  = sty("BODYJ",  fontSize=9,  fontName="Helvetica",      textColor=GS_DARK,  spaceAfter=3, leading=14, alignment=TA_JUSTIFY)
FIELD  = sty("FIELD",  fontSize=9,  fontName="Helvetica",      textColor=GS_DARK,  spaceAfter=2, leading=13)
SMALL  = sty("SMALL",  fontSize=7.5,fontName="Helvetica",      textColor=GS_GRAY,  spaceAfter=2, leading=12, alignment=TA_CENTER)
STEP_N = sty("STEP_N", fontSize=16, fontName="Helvetica-Bold", textColor=GS_GREEN, alignment=TA_CENTER, leading=18)
STEP_L = sty("STEP_L", fontSize=8.5,fontName="Helvetica-Bold", textColor=GS_DARK,  alignment=TA_CENTER, leading=12)
STEP_S = sty("STEP_S", fontSize=7.5,fontName="Helvetica",      textColor=GS_GRAY,  alignment=TA_CENTER, leading=11)
CHECK  = sty("CHECK",  fontSize=9,  fontName="Helvetica",      textColor=GS_DARK,  spaceAfter=2, leading=14, leftIndent=6)

def hr(color=LINE, t=0.75):  return HRFlowable(width="100%", thickness=t, color=color, spaceAfter=6, spaceBefore=4)
def blank(h=0.08):            return Spacer(1, h*inch)


def fill_line(label, wide=False):
    """A label + underline fill row."""
    line_w = 4.8*inch if wide else 3.8*inch
    lbl_w  = 6.25*inch - line_w
    t = Table(
        [[Paragraph(label, sty(f"fl_{hash(label)}", fontSize=8, fontName="Helvetica-Bold",
                               textColor=GS_GRAY, leading=11)), ""]],
        colWidths=[lbl_w, line_w]
    )
    t.setStyle(TableStyle([
        ("LINEBELOW",     (1,0),(1,0), 0.75, GS_DARK),
        ("VALIGN",        (0,0),(-1,-1), "BOTTOM"),
        ("BOTTOMPADDING", (0,0),(-1,-1), 2),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
    ]))
    return t


def step_box(num, label, sub):
    """Single step pill for the process timeline."""
    cell = Table(
        [[Paragraph(str(num), STEP_N)],
         [Paragraph(label, STEP_L)],
         [Paragraph(sub,   STEP_S)]],
        colWidths=[1.12*inch]
    )
    cell.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
        ("BOX",           (0,0),(-1,-1), 1.0, GS_BORDER),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(-1,-1), 4),
        ("RIGHTPADDING",  (0,0),(-1,-1), 4),
        ("ALIGN",         (0,0),(-1,-1), "CENTER"),
    ]))
    return cell


def arrow():
    return Table(
        [[Paragraph("\u2192", sty("arr", fontSize=14, fontName="Helvetica-Bold",
                                  textColor=GS_GREEN, alignment=TA_CENTER))]],
        colWidths=[0.22*inch]
    )


def checklist_row(icon, text):
    return [
        Paragraph(icon, sty(f"ic_{hash(text)}", fontSize=10, fontName="Helvetica",
                             textColor=GS_GREEN, alignment=TA_CENTER)),
        Paragraph(text, CHECK),
    ]


def story():
    s = []

    # ─────────────────────────────────────────────────────────────────────────
    # PAGE 1
    # ─────────────────────────────────────────────────────────────────────────

    # ── HEADER ────────────────────────────────────────────────────────────────
    s += [
        blank(0.2),
        Paragraph("Welcome to Groundwork Studio", TITLE),
        blank(0.12),
        Paragraph("Groundwork Studio AZ LLC  ·  teamground.work  ·  evan@teamground.work  ·  (480) 452-6473", SUB),
        blank(0.18),
        hr(GS_GREEN, 1.5),
        blank(0.15),
    ]

    # ── WELCOME NOTE ──────────────────────────────────────────────────────────
    s += [
        Paragraph(
            "We're glad to have you on board. This document outlines exactly what you're "
            "getting, what we need from you, and how the build process works from start to "
            "finish. Read through it once — it answers most questions before they come up.",
            BODYJ),
        blank(0.12),
    ]

    # ── SATISFACTION GUARANTEE BANNER ─────────────────────────────────────────
    guarantee_inner = Table(
        [[
            Paragraph("35-DAY SATISFACTION GUARANTEE",
                      sty("gg_title", fontSize=11, fontName="Helvetica-Bold",
                          textColor=GS_GREEN, spaceAfter=4, letterSpacing=0.5)),
        ]],
        colWidths=[6.25*inch]
    )
    guarantee_inner.setStyle(TableStyle([
        ("TOPPADDING",    (0,0),(-1,-1), 0),
        ("BOTTOMPADDING", (0,0),(-1,-1), 0),
    ]))

    guarantee_body = Table(
        [[
            Paragraph(
                "If your site goes live and you\u2019re not satisfied \u2014 or it hasn\u2019t generated "
                "results within <b>35 days of launch</b> \u2014 we\u2019ll refund your full build fee. "
                "No hoops. Just a written request within the window and we\u2019ll take care of it.",
                sty("gg_body", fontSize=9, fontName="Helvetica", textColor=GS_DARK, leading=14)),
        ]],
        colWidths=[6.25*inch]
    )

    guarantee_box = Table(
        [[guarantee_inner], [guarantee_body]],
        colWidths=[6.25*inch]
    )
    guarantee_box.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
        ("BOX",           (0,0),(-1,-1), 1.5, GS_GREEN),
        ("TOPPADDING",    (0,0),(-1,-1), 10),
        ("BOTTOMPADDING", (0,0),(-1,-1), 10),
        ("LEFTPADDING",   (0,0),(-1,-1), 14),
        ("RIGHTPADDING",  (0,0),(-1,-1), 14),
    ]))
    s += [guarantee_box, blank(0.12), hr()]

    # ── CLIENT + PROJECT INFO ─────────────────────────────────────────────────
    info_left = [
        [Paragraph("CLIENT", sty("cl_hdr", fontSize=8, fontName="Helvetica-Bold",
                                  textColor=GS_GREEN, letterSpacing=1.5)),
         Paragraph("PROJECT", sty("pr_hdr", fontSize=8, fontName="Helvetica-Bold",
                                   textColor=GS_GREEN, letterSpacing=1.5))],
        [Paragraph("Business Name", sty("bn", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY)),
         Paragraph("Tier / Package", sty("tp", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("_" * 36, FIELD),
         Paragraph("_" * 22, FIELD)],
        [Paragraph("Contact Name", sty("cn", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY)),
         Paragraph("Est. Launch Date", sty("ld", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("_" * 36, FIELD),
         Paragraph("_" * 22, FIELD)],
        [Paragraph("Email / Phone", sty("ep", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY)),
         Paragraph("Kick-Off Date", sty("kd", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("_" * 36, FIELD),
         Paragraph("_" * 22, FIELD)],
    ]
    info_t = Table(info_left, colWidths=[3.5*inch, 2.75*inch])
    info_t.setStyle(TableStyle([
        ("VALIGN",        (0,0),(-1,-1), "BOTTOM"),
        ("TOPPADDING",    (0,0),(-1,-1), 3),
        ("BOTTOMPADDING", (0,0),(-1,-1), 2),
        ("LINEAFTER",     (0,0),(0,-1), 0.5, LINE),
        ("LEFTPADDING",   (1,0),(1,-1), 16),
    ]))
    s += [info_t, blank(0.05), hr()]

    # ── SCOPE: WHAT YOU'RE GETTING ────────────────────────────────────────────
    s += [
        Paragraph("SCOPE — WHAT YOU'RE GETTING", LABEL),
        Paragraph("Pages & Sections Included", H2),
    ]
    for _ in range(4):
        s += [Paragraph("_" * 108, FIELD)]
    s += [blank(0.04)]

    s += [Paragraph("Features & Add-Ons", H2)]
    feat_rows = [
        ["Mobile-responsive design", "Google-ready (meta tags, sitemap)", "Contact form / click-to-call"],
        ["Google Maps embed",         "Photo gallery",                      "Custom color + logo branding"],
    ]
    for row in feat_rows:
        r_data = [[
            Paragraph(f"\u2610  {c}", sty(f"feat_{hash(c)}", fontSize=9, fontName="Helvetica",
                                          textColor=GS_DARK, leading=14))
            for c in row
        ]]
        rt = Table(r_data, colWidths=[2.2*inch, 2.35*inch, 1.7*inch])
        rt.setStyle(TableStyle([
            ("TOPPADDING",    (0,0),(-1,-1), 3),
            ("BOTTOMPADDING", (0,0),(-1,-1), 3),
            ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ]))
        s += [rt]

    s += [blank(0.05)]
    s += [Paragraph("Additional Notes / Custom Requests", H2)]
    for _ in range(2):
        s += [Paragraph("_" * 108, FIELD)]

    s += [blank(0.05), hr()]

    # ── FEES ──────────────────────────────────────────────────────────────────
    s += [Paragraph("FEES SUMMARY", LABEL)]
    fee_hdr = ["BUILD FEE", "DEPOSIT (50%)\nDUE NOW", "BALANCE (50%)\nDUE AT LAUNCH", "MONTHLY\nRETAINER"]
    fee_val = ["$__________", "$__________", "$__________", "$_________"]
    fee_t = Table(
        [[Paragraph(c, sty(f"fh{i}", fontSize=7.5, fontName="Helvetica-Bold",
                            textColor=GS_GRAY, alignment=TA_CENTER)) for i, c in enumerate(fee_hdr)],
         [Paragraph(c, sty(f"fv{i}", fontSize=15, fontName="Helvetica-Bold",
                            textColor=GS_DARK, alignment=TA_CENTER)) for i, c in enumerate(fee_val)]],
        colWidths=[1.5*inch, 1.65*inch, 1.65*inch, 1.45*inch]
    )
    fee_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0), GS_LIGHT),
        ("BOX",           (0,0),(-1,-1), 0.75, GS_BORDER),
        ("INNERGRID",     (0,0),(-1,-1), 0.5,  GS_BORDER),
        ("TOPPADDING",    (0,0),(-1,-1), 7),
        ("BOTTOMPADDING", (0,0),(-1,-1), 7),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ]))
    s += [fee_t, blank(0.04)]
    s += [
        Paragraph(
            "Deposit invoice will be sent via Wave once your contract is signed. "
            "Balance is due on launch day before the site goes live. "
            "Monthly retainer starts the 1st of the month after launch.",
            SMALL),
        blank(0.05), hr(),
    ]

    # ── PROCESS TIMELINE ──────────────────────────────────────────────────────
    s += [Paragraph("YOUR BUILD PROCESS", LABEL)]

    steps = [
        ("1", "Sign\nContract",  "DocuSign"),
        ("2", "Pay\nDeposit",    "via Wave"),
        ("3", "Send\nContent",   "14 days"),
        ("4", "Review\nDraft",   "2 rounds"),
        ("5", "Approve\n& Pay",  "Balance due"),
        ("6", "Go\nLive",        "Launch day"),
    ]

    row_cells = []
    for i, (n, l, sub) in enumerate(steps):
        row_cells.append(step_box(n, l, sub))
        if i < len(steps) - 1:
            row_cells.append(arrow())

    col_widths = []
    for i in range(len(steps)):
        col_widths.append(1.12*inch)
        if i < len(steps) - 1:
            col_widths.append(0.22*inch)

    proc_t = Table([row_cells], colWidths=col_widths)
    proc_t.setStyle(TableStyle([
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("ALIGN",         (0,0),(-1,-1), "CENTER"),
        ("LEFTPADDING",   (0,0),(-1,-1), 0),
        ("RIGHTPADDING",  (0,0),(-1,-1), 0),
        ("TOPPADDING",    (0,0),(-1,-1), 0),
        ("BOTTOMPADDING", (0,0),(-1,-1), 0),
    ]))
    s += [proc_t, blank(0.08)]

    # ─────────────────────────────────────────────────────────────────────────
    # PAGE 2
    # ─────────────────────────────────────────────────────────────────────────
    s.append(PageBreak())

    # ── WHAT WE NEED FROM YOU ─────────────────────────────────────────────────
    s += [
        Paragraph("WHAT WE NEED FROM YOU", LABEL),
        Paragraph(
            "Send all content within 14 days of signing to keep your project on schedule. "
            "The faster we get your materials, the faster your site goes live.",
            BODY),
        blank(0.08),
    ]

    checklist_items = [
        ("Logo file", "PNG or SVG, transparent background preferred. If you don't have one, let us know."),
        ("Brand colors", "Hex codes or just describe them — we'll match."),
        ("Photos",        "At least 5–10 high-quality photos of your team, work, or location. Phone photos are fine."),
        ("Business description", "2–3 sentences about what you do and who you serve. We can help draft this."),
        ("Services list", "Name and brief description of each service you offer."),
        ("Service area",  "Cities or zip codes you cover."),
        ("Contact info",  "Phone, email, address (or service-area-only), hours."),
        ("Google Business link", "Your Google Maps / Google Business profile URL if you have one."),
        ("Testimonials",  "2–5 reviews or quotes from happy customers (optional but recommended)."),
    ]

    cl_data = [checklist_row("\u2610", f"<b>{item}</b> — {desc}") for item, desc in checklist_items]
    cl_t = Table(cl_data, colWidths=[0.25*inch, 6.0*inch])
    cl_t.setStyle(TableStyle([
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 4),
        ("BOTTOMPADDING", (0,0),(-1,-1), 4),
        ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("LEFTPADDING",   (1,0),(1,-1), 6),
    ]))
    s += [cl_t, blank(0.08), hr()]

    # ── TIMELINE EXPECTATIONS ─────────────────────────────────────────────────
    s += [
        Paragraph("TIMELINE EXPECTATIONS", LABEL),
    ]
    timeline_rows = [
        ["After signing",        "Deposit invoice sent via Wave — work begins on receipt"],
        ["Week 1–2",             "Internal build: structure, layout, design"],
        ["Week 2–3",             "Draft sent to you for first review"],
        ["Your review window",   "5 business days to consolidate feedback into one list"],
        ["Revision round",       "Changes applied within 3–5 business days"],
        ["Final approval",       "Balance invoice sent — site goes live once payment clears"],
        ["After launch",         "Monthly retainer kicks in — you have a developer on call"],
    ]
    tl_data = [[
        Paragraph(r[0], sty(f"tl0_{i}", fontSize=8.5, fontName="Helvetica-Bold",
                             textColor=GS_DARK, leading=13)),
        Paragraph(r[1], sty(f"tl1_{i}", fontSize=8.5, fontName="Helvetica",
                             textColor=GS_DARK, leading=13)),
    ] for i, r in enumerate(timeline_rows)]
    tl_t = Table(tl_data, colWidths=[1.75*inch, 4.5*inch])
    tl_t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("GRID",           (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",         (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",     (0,0),(-1,-1), 7),
        ("BOTTOMPADDING",  (0,0),(-1,-1), 7),
        ("LEFTPADDING",    (0,0),(-1,-1), 10),
        ("BACKGROUND",     (0,0),(0,-1), GS_LIGHT),
    ]))
    s += [tl_t, blank(0.08), hr()]

    # ── WHAT HAPPENS AFTER LAUNCH ─────────────────────────────────────────────
    s += [
        Paragraph("AFTER LAUNCH — YOUR MONTHLY RETAINER COVERS", LABEL),
    ]
    post_items = [
        ("Hosting",            "Your site stays live on enterprise-grade infrastructure (Netlify)."),
        ("Security",           "SSL certificate, uptime monitoring, platform updates."),
        ("Content updates",    "Send us text or photo changes — we handle it, usually within 48 hours."),
        ("Developer access",   "Questions, tweaks, or small additions — just email us."),
        ("Cancellation",       "30 days written notice, any time. Site can be migrated to your own hosting for a one-time $250 fee."),
    ]
    post_data = [checklist_row("\u2714", f"<b>{item}</b> — {desc}") for item, desc in post_items]
    post_t = Table(post_data, colWidths=[0.25*inch, 6.0*inch])
    post_t.setStyle(TableStyle([
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, colors.HexColor("#f9fafb")]),
        ("LEFTPADDING",   (1,0),(1,-1), 6),
    ]))
    s += [post_t, blank(0.1)]

    # ── FOOTER ────────────────────────────────────────────────────────────────
    s += [
        hr(GS_BORDER),
        Paragraph(
            "Questions? Reach out anytime — evan@teamground.work  ·  (480) 452-6473  ·  teamground.work<br/>"
            "<i>Groundwork Studio AZ LLC  ·  Phoenix, AZ  ·  Arizona Limited Liability Company</i>",
            SMALL),
    ]

    return s


def build():
    os.makedirs(os.path.dirname(OUT_REPO), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT_REPO, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.65*inch, bottomMargin=0.65*inch,
        title="Groundwork Studio — Welcome & Scope",
        author="Groundwork Studio AZ LLC",
    )
    doc.build(story())
    shutil.copy(OUT_REPO, OUT_DESK)
    print(f"✓ Welcome & Scope saved to:\n  {OUT_REPO}\n  {OUT_DESK}")


if __name__ == "__main__":
    build()
