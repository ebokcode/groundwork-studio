#!/usr/bin/env python3
"""Generate Groundwork Studio Quarterly Performance Report Template PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
import os, shutil

OUT_REPO = "/Users/evanbaukol/Sites/groundwork-studio/docs/Groundwork_Quarterly_Report_Template.pdf"
OUT_DESK = "/Users/evanbaukol/Desktop/Groundwork Studio \u2014 Docs/Groundwork_Quarterly_Report_Template.pdf"

# ── Colors ─────────────────────────────────────────────────────────────────────
GS_GREEN   = colors.HexColor("#16a34a")
GS_DARK    = colors.HexColor("#111827")
GS_GRAY    = colors.HexColor("#6b7280")
GS_LIGHT   = colors.HexColor("#f0fdf4")
GS_BORDER  = colors.HexColor("#d1fae5")
GS_MID     = colors.HexColor("#dcfce7")
LINE       = colors.HexColor("#e5e7eb")
WHITE      = colors.white
GS_SLATE   = colors.HexColor("#f8fafc")
GS_BLUE    = colors.HexColor("#eff6ff")
GS_BLUE_B  = colors.HexColor("#bfdbfe")
GS_BLUE_C  = colors.HexColor("#3b82f6")
GS_AMBER   = colors.HexColor("#d97706")
GS_AMBER_L = colors.HexColor("#fef3c7")
GS_AMBER_B = colors.HexColor("#fcd34d")
GS_RED     = colors.HexColor("#dc2626")
GS_RED_L   = colors.HexColor("#fef2f2")
GS_RED_B   = colors.HexColor("#fecaca")

# ── Styles ──────────────────────────────────────────────────────────────────────
def sty(name, **kw): return ParagraphStyle(name, **kw)

LABEL_TOP = sty("LABEL_TOP", fontSize=9,   fontName="Helvetica-Bold", textColor=GS_GREEN,
                alignment=TA_CENTER, letterSpacing=3, spaceAfter=0)
TITLE     = sty("TITLE",     fontSize=26,  fontName="Helvetica-Bold", textColor=GS_DARK,
                alignment=TA_CENTER, spaceAfter=0, leading=30)
SUBTITLE  = sty("SUBTITLE",  fontSize=10,  fontName="Helvetica",      textColor=GS_GRAY,
                alignment=TA_CENTER, spaceAfter=0)
LABEL     = sty("LABEL",     fontSize=7.5, fontName="Helvetica-Bold", textColor=GS_GREEN,
                spaceAfter=4, spaceBefore=4, letterSpacing=1.5)
H2        = sty("H2",        fontSize=15,  fontName="Helvetica-Bold", textColor=GS_DARK,
                spaceAfter=6, spaceBefore=0, leading=18)
H3        = sty("H3",        fontSize=10,  fontName="Helvetica-Bold", textColor=GS_DARK,
                spaceAfter=4, spaceBefore=8)
BODY      = sty("BODY",      fontSize=9,   fontName="Helvetica",      textColor=GS_DARK,
                spaceAfter=4, leading=14)
BODYJ     = sty("BODYJ",     fontSize=9,   fontName="Helvetica",      textColor=GS_DARK,
                spaceAfter=4, leading=14, alignment=TA_JUSTIFY)
SMALL     = sty("SMALL",     fontSize=7.5, fontName="Helvetica",      textColor=GS_GRAY,
                spaceAfter=2, leading=12, alignment=TA_CENTER)
SMALLL    = sty("SMALLL",    fontSize=7.5, fontName="Helvetica",      textColor=GS_GRAY,
                spaceAfter=2, leading=12)
NOTE      = sty("NOTE",      fontSize=7,   fontName="Helvetica-Oblique", textColor=GS_GRAY,
                spaceAfter=2, leading=11, alignment=TA_CENTER)

def hr(color=LINE, t=0.75): return HRFlowable(width="100%", thickness=t, color=color,
                                               spaceAfter=8, spaceBefore=4)
def blank(h=0.1): return Spacer(1, h*inch)

FOOTER_TXT = "Groundwork Studio AZ LLC  \u00b7  teamground.work  \u00b7  evan@teamground.work  \u00b7  (480) 452-6473"

def footer():
    return [
        blank(0.1),
        hr(GS_BORDER),
        Paragraph(FOOTER_TXT, SMALL),
        Paragraph("Template — replace bracketed placeholders and sample data before delivery to client.", NOTE),
    ]

def cell(text, bold=False, size=9, color=GS_DARK, align=TA_LEFT, leading=13):
    return Paragraph(text, sty(f"c_{hash(text+str(bold)+str(size)+str(align))}",
                               fontSize=size,
                               fontName="Helvetica-Bold" if bold else "Helvetica",
                               textColor=color, alignment=align, leading=leading))


# ── KPI Card ────────────────────────────────────────────────────────────────────
def kpi_card(label, value, sub, bg=GS_LIGHT, border=GS_BORDER, val_color=GS_GREEN, w=1.5*inch):
    t = Table([
        [Paragraph(label, sty(f"kl_{hash(label+str(w))}", fontSize=7,
                              fontName="Helvetica-Bold", textColor=GS_GRAY,
                              letterSpacing=1.0, alignment=TA_CENTER))],
        [Paragraph(value, sty(f"kv_{hash(value+label)}", fontSize=22,
                              fontName="Helvetica-Bold", textColor=val_color,
                              alignment=TA_CENTER, leading=24, spaceAfter=0))],
        [Paragraph(sub, sty(f"ks_{hash(sub+label)}", fontSize=7.5,
                            fontName="Helvetica", textColor=GS_GRAY,
                            alignment=TA_CENTER, leading=11))],
    ], colWidths=[w])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), bg),
        ("BOX",           (0,0),(-1,-1), 1.0, border),
        ("TOPPADDING",    (0,0),(0,0), 10),
        ("BOTTOMPADDING", (0,0),(0,0), 2),
        ("TOPPADDING",    (0,1),(0,1), 2),
        ("BOTTOMPADDING", (0,1),(0,1), 2),
        ("TOPPADDING",    (0,2),(0,2), 0),
        ("BOTTOMPADDING", (0,2),(0,2), 10),
        ("LEFTPADDING",   (0,0),(-1,-1), 6),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    return t

def kpi_row_table(cards, col_widths):
    t = Table([cards], colWidths=col_widths)
    t.setStyle(TableStyle([
        ("LEFTPADDING",   (0,0),(-1,-1), 3),
        ("RIGHTPADDING",  (0,0),(-1,-1), 3),
        ("TOPPADDING",    (0,0),(-1,-1), 0),
        ("BOTTOMPADDING", (0,0),(-1,-1), 0),
    ]))
    return t


# ── Bar Chart ───────────────────────────────────────────────────────────────────
def bar_chart(data_series, labels, chart_colors, dw=430, dh=160):
    d = Drawing(dw, dh)
    n = len(data_series)
    bc = VerticalBarChart()
    bc.x = 48
    bc.y = 32
    bc.height = dh - 50
    bc.width  = dw - 68
    bc.data   = [tuple(s) for s in data_series]
    bc.strokeColor = None
    bc.fillColor   = None
    for i, c in enumerate(chart_colors):
        bc.bars[i].fillColor   = c
        bc.bars[i].strokeColor = None
    bc.barWidth     = max(22 - n * 4, 8)
    bc.groupSpacing = 10
    bc.categoryAxis.categoryNames  = labels
    bc.categoryAxis.labels.fontSize   = 8
    bc.categoryAxis.labels.fontName   = "Helvetica"
    bc.categoryAxis.labels.fillColor  = GS_GRAY
    bc.categoryAxis.visibleTicks      = False
    bc.categoryAxis.strokeColor       = LINE
    bc.valueAxis.valueMin    = 0
    bc.valueAxis.labels.fontSize  = 8
    bc.valueAxis.labels.fontName  = "Helvetica"
    bc.valueAxis.labels.fillColor = GS_GRAY
    bc.valueAxis.visibleGrid      = True
    bc.valueAxis.gridStrokeColor  = LINE
    bc.valueAxis.gridStrokeDashArray = [2, 2]
    bc.valueAxis.visibleTicks     = False
    bc.valueAxis.strokeColor      = LINE
    d.add(bc)
    return d


# ── Line Chart ──────────────────────────────────────────────────────────────────
def line_chart(data_series, labels, chart_colors, dw=430, dh=150):
    d = Drawing(dw, dh)
    lc = HorizontalLineChart()
    lc.x = 48
    lc.y = 32
    lc.height = dh - 50
    lc.width  = dw - 68
    lc.data   = [tuple(s) for s in data_series]
    lc.strokeColor = None
    lc.fillColor   = None
    for i, c in enumerate(chart_colors):
        lc.lines[i].strokeColor = c
        lc.lines[i].strokeWidth = 2.5
    lc.joinedLines = True
    lc.categoryAxis.categoryNames  = labels
    lc.categoryAxis.labels.fontSize   = 8
    lc.categoryAxis.labels.fontName   = "Helvetica"
    lc.categoryAxis.labels.fillColor  = GS_GRAY
    lc.categoryAxis.visibleTicks      = False
    lc.categoryAxis.strokeColor       = LINE
    lc.valueAxis.labels.fontSize  = 8
    lc.valueAxis.labels.fontName  = "Helvetica"
    lc.valueAxis.labels.fillColor = GS_GRAY
    lc.valueAxis.visibleGrid      = True
    lc.valueAxis.gridStrokeColor  = LINE
    lc.valueAxis.gridStrokeDashArray = [2, 2]
    lc.valueAxis.visibleTicks     = False
    lc.valueAxis.strokeColor      = LINE
    d.add(lc)
    return d


# ── Legend helper ───────────────────────────────────────────────────────────────
def legend_row(items):
    """items = list of (label, color) tuples."""
    cells = []
    for label, c in items:
        cells.append(Paragraph(
            f"<font color='#{c.hexval()[2:]}'>&#9632;</font>  {label}",
            sty(f"leg_{hash(label)}", fontSize=8, fontName="Helvetica",
                textColor=GS_DARK, leading=12)
        ))
    col_w = [1.4*inch] * len(items)
    t = Table([cells], colWidths=col_w)
    t.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 40),
        ("TOPPADDING",   (0,0),(-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1), 0),
    ]))
    return t


# ── Section header strip ────────────────────────────────────────────────────────
def section_header(label_text, title_text):
    return [
        Paragraph(label_text, LABEL),
        blank(0.05),
        Paragraph(title_text, H2),
        hr(GS_GREEN, 2),
        blank(0.08),
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 1  —  COVER + FULL METRICS SNAPSHOT
# ═══════════════════════════════════════════════════════════════════════════════
def page_cover():
    s = []

    s += [
        blank(0.25),
        Paragraph("GROUNDWORK STUDIO", LABEL_TOP),
        blank(0.1),
        Paragraph("Quarterly Performance Report", TITLE),
        blank(0.14),
        Paragraph("[CLIENT NAME]  \u00b7  [Q1 2025]  \u00b7  January \u2013 March 2025",
                  sty("cs", fontSize=11, fontName="Helvetica-Bold",
                      textColor=GS_DARK, alignment=TA_CENTER)),
        blank(0.05),
        Paragraph("Prepared by Evan Baukol  \u00b7  Groundwork Studio AZ LLC",
                  sty("cp", fontSize=9, fontName="Helvetica", textColor=GS_GRAY, alignment=TA_CENTER)),
        blank(0.2),
        hr(GS_GREEN, 2),
        blank(0.16),
    ]

    # 4 hero KPI cards
    cw = [1.56*inch, 1.56*inch, 1.56*inch, 1.57*inch]
    s += [kpi_row_table([
        kpi_card("TOTAL SESSIONS",     "1,257",   "\u2191 39% vs prior quarter", w=1.5*inch),
        kpi_card("SEARCH IMPRESSIONS", "10,910",  "\u2191 58% vs prior quarter", w=1.5*inch),
        kpi_card("GBP PROFILE VIEWS",  "1,640",   "\u2191 22% vs prior quarter", w=1.5*inch),
        kpi_card("SITE UPTIME",        "99.98%",  "0 outages this quarter",      w=1.5*inch),
    ], cw), blank(0.16)]

    # Quarter summary callout
    qsummary = Table([
        [Paragraph("QUARTER AT A GLANCE", sty("qg_l", fontSize=8, fontName="Helvetica-Bold",
                   textColor=GS_GREEN, letterSpacing=1.5, spaceAfter=0))],
        [Paragraph(
            "Website traffic grew <b>39%</b> this quarter, driven by improving Google search rankings and "
            "a stronger Google Business Profile. Search impressions nearly doubled, organic clicks increased "
            "<b>74%</b>, and average search position improved from 24.2 \u2192 14.3. "
            "The site maintained near-perfect uptime with zero security incidents. "
            "Overall momentum is strong \u2014 detailed breakdowns follow on the pages below.",
            sty("qg_b", fontSize=9.5, fontName="Helvetica", textColor=GS_DARK, leading=15))],
    ], colWidths=[6.25*inch])
    qsummary.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
        ("BOX",           (0,0),(-1,-1), 1.5, GS_GREEN),
        ("TOPPADDING",    (0,0),(0,0), 10),
        ("BOTTOMPADDING", (0,0),(0,0), 4),
        ("TOPPADDING",    (0,1),(0,1), 2),
        ("BOTTOMPADDING", (0,1),(0,1), 14),
        ("LEFTPADDING",   (0,0),(-1,-1), 14),
        ("RIGHTPADDING",  (0,0),(-1,-1), 14),
    ]))
    s += [qsummary, blank(0.14)]

    # Full metrics snapshot table
    s += [Paragraph("FULL METRICS SNAPSHOT", sty("ms_l", fontSize=8, fontName="Helvetica-Bold",
                    textColor=GS_GREEN, letterSpacing=1.5, spaceAfter=6))]

    mhdr = ["Metric", "Q1 Total", "Q4 Prior", "Change", "Trend"]
    mrows = [
        ["Total Website Sessions",    "1,257",  "903",    "+354",   "\u25b2 +39.2%"],
        ["Unique Users",              "1,050",  "762",    "+288",   "\u25b2 +37.8%"],
        ["Pageviews",                 "3,841",  "2,614",  "+1,227", "\u25b2 +46.9%"],
        ["Bounce Rate",               "41.2%",  "52.7%",  "\u22121.5%", "\u25b2 improved"],
        ["Google Search Impressions", "10,910", "6,901",  "+4,009", "\u25b2 +58.1%"],
        ["Google Search Clicks",      "280",    "161",    "+119",   "\u25b2 +73.9%"],
        ["Avg. Click-Through Rate",   "2.6%",   "2.3%",   "+0.3%",  "\u25b2 +13.0%"],
        ["Avg. Search Position",      "14.3",   "24.2",   "\u22129.9", "\u25b2 improved"],
        ["GBP Profile Views",         "1,640",  "1,342",  "+298",   "\u25b2 +22.2%"],
        ["GBP Phone Calls",           "114",    "87",     "+27",    "\u25b2 +31.0%"],
        ["GBP Direction Requests",    "52",     "38",     "+14",    "\u25b2 +36.8%"],
        ["Site Uptime",               "99.98%", "99.94%", "+0.04%", "\u25b2 improved"],
    ]

    ms_data = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in mhdr]]
    for row in mrows:
        trend = row[4]
        t_col = GS_GREEN if "\u25b2" in trend else GS_RED
        ms_data.append([
            cell(row[0], size=8),
            cell(row[1], bold=True, size=8, align=TA_CENTER),
            cell(row[2], size=8, color=GS_GRAY, align=TA_CENTER),
            cell(row[3], size=8, align=TA_CENTER),
            Paragraph(trend, sty(f"tr_{hash(trend+row[0])}", fontSize=8,
                                 fontName="Helvetica-Bold", textColor=t_col,
                                 alignment=TA_CENTER, leading=12)),
        ])

    ms_t = Table(ms_data, colWidths=[2.15*inch, 0.88*inch, 0.88*inch, 0.78*inch, 1.56*inch])
    ms_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 7),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    s += [ms_t]
    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 2  —  WEBSITE TRAFFIC
# ═══════════════════════════════════════════════════════════════════════════════
def page_traffic():
    s = [PageBreak()]
    s += section_header("WEBSITE TRAFFIC", "Traffic Overview")

    cw = [1.56*inch, 1.56*inch, 1.56*inch, 1.57*inch]
    s += [kpi_row_table([
        kpi_card("TOTAL SESSIONS", "1,257",  "Jan \u2013 Mar 2025",   w=1.5*inch),
        kpi_card("UNIQUE USERS",   "1,050",  "Jan \u2013 Mar 2025",   w=1.5*inch),
        kpi_card("PAGEVIEWS",      "3,841",  "Jan \u2013 Mar 2025",   w=1.5*inch),
        kpi_card("AVG. DURATION",  "2m 14s", "per session",           w=1.5*inch),
    ], cw), blank(0.16)]

    # Bar chart — Sessions vs Users
    s += [Paragraph("Monthly Sessions vs. Unique Users", H3)]
    s += [bar_chart([[312, 427, 518], [248, 361, 441]],
                    ["January", "February", "March"],
                    [GS_GREEN, GS_BLUE_C], dw=430, dh=155)]
    s += [legend_row([("Sessions", GS_GREEN), ("Unique Users", GS_BLUE_C)]), blank(0.1)]

    # Monthly breakdown table
    s += [Paragraph("Monthly Breakdown", H3)]
    th = ["Month", "Sessions", "Users", "Pageviews", "Avg. Duration", "Bounce Rate"]
    tr = [
        ["January",     "312",   "248",   "921",   "1m 58s", "47.3%"],
        ["February",    "427",   "361",   "1,304", "2m 09s", "43.1%"],
        ["March",       "518",   "441",   "1,616", "2m 34s", "36.7%"],
        ["Q1 TOTAL",  "1,257", "1,050",  "3,841", "2m 14s", "41.2%"],
    ]
    td = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in th]]
    for i, row in enumerate(tr):
        is_tot = i == 3
        td.append([cell(v, bold=is_tot, size=8.5,
                        color=GS_GREEN if is_tot and j == 0 else GS_DARK,
                        align=TA_CENTER if j > 0 else TA_LEFT)
                   for j, v in enumerate(row)])
    tt = Table(td, colWidths=[1.05*inch, 0.9*inch, 0.9*inch, 0.9*inch, 1.05*inch, 0.95*inch])
    tt.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("BACKGROUND",    (0,4),(-1,4),  GS_LIGHT),
        ("ROWBACKGROUNDS",(0,1),(-1,3),  [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
        ("LINEABOVE",     (0,4),(-1,4),  1.5, GS_GREEN),
    ]))
    s += [tt, blank(0.12)]

    # Traffic sources table
    s += [Paragraph("Traffic Sources", H3)]
    sh = ["Source", "Sessions", "% of Total", "Trend vs Prior Quarter"]
    sr = [
        ["Organic Search (Google)",  "687", "54.6%", "\u25b2 +61%"],
        ["Direct",                   "289", "23.0%", "\u25b2 +18%"],
        ["Google Business Profile",  "196", "15.6%", "\u25b2 +44%"],
        ["Referral",                  "62",  "4.9%", "\u25b2 +12%"],
        ["Social",                    "23",  "1.8%", "\u25b2 +5%"],
    ]
    sd = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in sh]]
    for row in sr:
        sd.append([
            cell(row[0], size=8.5),
            cell(row[1], bold=True, size=8.5, align=TA_CENTER),
            cell(row[2], size=8.5, color=GS_GRAY, align=TA_CENTER),
            Paragraph(row[3], sty(f"srt_{hash(row[3]+row[0])}", fontSize=8.5,
                                  fontName="Helvetica-Bold", textColor=GS_GREEN,
                                  alignment=TA_CENTER, leading=13)),
        ])
    src_t = Table(sd, colWidths=[2.5*inch, 0.9*inch, 1.0*inch, 1.85*inch])
    src_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    s += [src_t]
    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 3  —  SEARCH PERFORMANCE (GOOGLE SEARCH CONSOLE)
# ═══════════════════════════════════════════════════════════════════════════════
def page_search():
    s = [PageBreak()]
    s += section_header("SEARCH PERFORMANCE", "Google Search Console")

    cw = [1.56*inch, 1.56*inch, 1.56*inch, 1.57*inch]
    s += [kpi_row_table([
        kpi_card("TOTAL IMPRESSIONS", "10,910", "times shown in search",    w=1.5*inch),
        kpi_card("ORGANIC CLICKS",    "280",    "click-throughs to site",   w=1.5*inch),
        kpi_card("AVG. CTR",          "2.6%",   "\u2191 from 2.3% last qtr",w=1.5*inch),
        kpi_card("AVG. POSITION",     "14.3",   "\u2191 from 24.2 last qtr",w=1.5*inch),
    ], cw), blank(0.16)]

    # Search impressions line chart
    s += [Paragraph("Monthly Search Impressions", H3)]
    s += [line_chart([[2840, 3920, 4150]], ["January", "February", "March"],
                     [GS_GREEN], dw=430, dh=140), blank(0.12)]

    # Month-by-month search table
    s += [Paragraph("Month-by-Month Search Data", H3)]
    sc_h = ["Month", "Impressions", "Clicks", "CTR", "Avg. Position", "Pos. Change"]
    sc_r = [
        ["January",  "2,840", "68",  "2.4%", "24.2", "\u2014"],
        ["February", "3,920", "94",  "2.4%", "18.7", "\u25b2 +5.5"],
        ["March",    "4,150", "118", "2.8%", "14.3", "\u25b2 +4.4"],
        ["Q1 TOTAL", "10,910","280", "2.6%", "14.3", "\u25b2 +9.9"],
    ]
    sc_d = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in sc_h]]
    for i, row in enumerate(sc_r):
        is_tot = i == 3
        pc = row[5]
        sc_d.append([
            cell(row[0], bold=is_tot, size=8.5, color=GS_GREEN if is_tot else GS_DARK),
            cell(row[1], bold=is_tot, size=8.5, align=TA_CENTER),
            cell(row[2], size=8.5, align=TA_CENTER),
            cell(row[3], size=8.5, align=TA_CENTER),
            cell(row[4], bold=is_tot, size=8.5, color=GS_GREEN if is_tot else GS_DARK, align=TA_CENTER),
            Paragraph(pc, sty(f"pc_{hash(pc+str(i))}", fontSize=8.5,
                              fontName="Helvetica-Bold",
                              textColor=GS_GREEN if "\u25b2" in pc else GS_GRAY,
                              alignment=TA_CENTER, leading=13)),
        ])
    sc_t = Table(sc_d, colWidths=[1.0*inch, 1.0*inch, 0.75*inch, 0.75*inch, 1.05*inch, 1.7*inch])
    sc_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("BACKGROUND",    (0,4),(-1,4),  GS_LIGHT),
        ("ROWBACKGROUNDS",(0,1),(-1,3),  [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
        ("LINEABOVE",     (0,4),(-1,4),  1.5, GS_GREEN),
    ]))
    s += [sc_t, blank(0.14)]

    # Top keywords table
    s += [Paragraph("Top Keywords This Quarter", H3)]
    kw_h = ["Keyword / Search Term", "Impressions", "Clicks", "CTR", "Avg. Position"]
    kw_r = [
        ["[primary service] [city]",          "1,840", "72", "3.9%",  "4.2"],
        ["[primary service] near me",          "1,210", "48", "4.0%",  "5.7"],
        ["[secondary service] [city]",           "920", "31", "3.4%",  "7.1"],
        ["best [service] in [city]",             "780", "22", "2.8%",  "9.4"],
        ["[service] company [city]",             "640", "18", "2.8%", "11.2"],
        ["affordable [service] [city]",          "510", "14", "2.7%", "13.8"],
        ["[city] [service] reviews",             "420", "11", "2.6%", "16.4"],
        ["[service] contractor [city]",          "380",  "9", "2.4%", "18.1"],
        ["[city] [secondary service]",           "290",  "7", "2.4%", "21.3"],
        ["[service] estimate [city]",            "220",  "5", "2.3%", "24.7"],
    ]
    kw_d = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in kw_h]]
    for row in kw_r:
        kw_d.append([
            cell(row[0], size=8.5),
            cell(row[1], size=8.5, align=TA_CENTER),
            cell(row[2], bold=True, size=8.5, color=GS_GREEN, align=TA_CENTER),
            cell(row[3], size=8.5, align=TA_CENTER),
            cell(row[4], size=8.5, color=GS_GRAY, align=TA_CENTER),
        ])
    kw_t = Table(kw_d, colWidths=[2.5*inch, 0.95*inch, 0.7*inch, 0.7*inch, 1.4*inch])
    kw_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    s += [kw_t]
    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 4  —  GOOGLE BUSINESS PROFILE
# ═══════════════════════════════════════════════════════════════════════════════
def page_gbp():
    s = [PageBreak()]
    s += section_header("GOOGLE BUSINESS PROFILE", "GBP Performance")

    cw = [1.56*inch, 1.56*inch, 1.56*inch, 1.57*inch]
    s += [kpi_row_table([
        kpi_card("GBP VIEWS",      "1,640", "profile impressions",    w=1.5*inch),
        kpi_card("PHONE CALLS",    "114",   "tapped call button",      w=1.5*inch),
        kpi_card("DIRECTIONS",     "52",    "direction requests",      w=1.5*inch),
        kpi_card("WEBSITE CLICKS", "196",   "clicks from GBP to site", w=1.5*inch),
    ], cw), blank(0.16)]

    # GBP grouped bar chart
    s += [Paragraph("Monthly GBP Activity", H3)]
    s += [bar_chart(
        [[420, 580, 640], [28, 39, 47], [45, 67, 84]],
        ["January", "February", "March"],
        [GS_GREEN, GS_BLUE_C, GS_AMBER], dw=430, dh=155)]
    s += [legend_row([
        ("Profile Views", GS_GREEN),
        ("Phone Calls", GS_BLUE_C),
        ("Website Clicks", GS_AMBER),
    ]), blank(0.12)]

    # Monthly GBP breakdown table
    s += [Paragraph("Monthly GBP Breakdown", H3)]
    gh = ["Month", "Profile Views", "Searches", "Phone Calls", "Directions", "Web Clicks"]
    gr = [
        ["January",  "420",   "680",   "28", "12",  "45"],
        ["February", "580",   "920",   "39", "18",  "67"],
        ["March",    "640",  "1,040",  "47", "22",  "84"],
        ["Q1 TOTAL","1,640", "2,640", "114", "52", "196"],
    ]
    gd = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in gh]]
    for i, row in enumerate(gr):
        is_tot = i == 3
        gd.append([cell(v, bold=is_tot, size=8.5,
                        color=GS_GREEN if is_tot and j == 0 else GS_DARK,
                        align=TA_CENTER if j > 0 else TA_LEFT)
                   for j, v in enumerate(row)])
    g_t = Table(gd, colWidths=[1.0*inch, 1.0*inch, 1.0*inch, 0.9*inch, 0.9*inch, 1.0*inch])
    g_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("BACKGROUND",    (0,4),(-1,4),  GS_LIGHT),
        ("ROWBACKGROUNDS",(0,1),(-1,3),  [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
        ("LINEABOVE",     (0,4),(-1,4),  1.5, GS_GREEN),
    ]))
    s += [g_t, blank(0.16)]

    # How customers found you — two side-by-side boxes
    s += [Paragraph("How Customers Found You", H3)]

    def found_box(title, value, subtitle, bg, bdr, val_col):
        t = Table([
            [Paragraph(title, sty(f"fbt_{hash(title)}", fontSize=7.5, fontName="Helvetica-Bold",
                                  textColor=GS_GRAY, alignment=TA_CENTER, letterSpacing=1.0))],
            [Paragraph(value, sty(f"fbv_{hash(value)}", fontSize=28, fontName="Helvetica-Bold",
                                  textColor=val_col, alignment=TA_CENTER, leading=30))],
            [Paragraph(subtitle, sty(f"fbs_{hash(subtitle)}", fontSize=8, fontName="Helvetica",
                                     textColor=GS_GRAY, alignment=TA_CENTER, leading=12))],
        ], colWidths=[3.0*inch])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0,0),(-1,-1), bg),
            ("BOX",           (0,0),(-1,-1), 0.75, bdr),
            ("TOPPADDING",    (0,0),(0,0), 12),
            ("BOTTOMPADDING", (0,0),(0,0), 4),
            ("TOPPADDING",    (0,1),(0,1), 4),
            ("BOTTOMPADDING", (0,1),(0,1), 4),
            ("TOPPADDING",    (0,2),(0,2), 0),
            ("BOTTOMPADDING", (0,2),(0,2), 14),
            ("LEFTPADDING",   (0,0),(-1,-1), 10),
            ("RIGHTPADDING",  (0,0),(-1,-1), 10),
        ]))
        return t

    frow = Table([[
        found_box("DIRECT SEARCHES",    "1,180", "Searched your business name directly",
                  GS_LIGHT, GS_BORDER, GS_GREEN),
        found_box("DISCOVERY SEARCHES", "1,460", "Found you through category or service search",
                  GS_BLUE, GS_BLUE_B, GS_BLUE_C),
    ]], colWidths=[3.1*inch, 3.15*inch])
    frow.setStyle(TableStyle([
        ("LEFTPADDING",   (0,0),(-1,-1), 0),
        ("RIGHTPADDING",  (0,0),(-1,-1), 0),
        ("TOPPADDING",    (0,0),(-1,-1), 0),
        ("BOTTOMPADDING", (0,0),(-1,-1), 0),
        ("LEFTPADDING",   (1,0),(1,0),   10),
    ]))
    s += [frow]
    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 5  —  TECHNICAL HEALTH
# ═══════════════════════════════════════════════════════════════════════════════
def page_technical():
    s = [PageBreak()]
    s += section_header("TECHNICAL HEALTH", "Site Performance & Security")

    cw = [1.56*inch, 1.56*inch, 1.56*inch, 1.57*inch]
    s += [kpi_row_table([
        kpi_card("OVERALL SCORE",  "94/100", "PageSpeed Insights",  w=1.5*inch),
        kpi_card("MOBILE SCORE",   "91/100", "Google Mobile Test",  w=1.5*inch),
        kpi_card("DESKTOP SCORE",  "97/100", "Google Desktop Test", w=1.5*inch),
        kpi_card("UPTIME",         "99.98%", "0 outages, 2m 42s total downtime", w=1.5*inch),
    ], cw), blank(0.16)]

    # Core Web Vitals table
    s += [Paragraph("Core Web Vitals", H3)]
    pf_h = ["Core Web Vital", "Value", "Score", "Rating"]
    pf_r = [
        ("First Contentful Paint",   "0.8s",  "98",  "Excellent", GS_GREEN),
        ("Largest Contentful Paint", "1.2s",  "94",  "Excellent", GS_GREEN),
        ("Total Blocking Time",      "0ms",   "100", "Excellent", GS_GREEN),
        ("Cumulative Layout Shift",  "0.02",  "97",  "Excellent", GS_GREEN),
        ("Speed Index",              "1.1s",  "95",  "Excellent", GS_GREEN),
        ("Time to Interactive",      "1.4s",  "92",  "Excellent", GS_GREEN),
    ]
    pf_d = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in pf_h]]
    for name, val, score, rating, r_col in pf_r:
        pf_d.append([
            cell(name, size=8.5),
            cell(val,  bold=True, size=8.5, align=TA_CENTER),
            cell(score, bold=True, size=8.5, color=r_col, align=TA_CENTER),
            Paragraph(rating, sty(f"rat_{hash(name)}", fontSize=8.5,
                                  fontName="Helvetica-Bold", textColor=r_col,
                                  alignment=TA_CENTER, leading=13)),
        ])
    pf_t = Table(pf_d, colWidths=[2.5*inch, 1.0*inch, 0.9*inch, 1.85*inch])
    pf_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    s += [pf_t, blank(0.14)]

    # Security & uptime table
    s += [Paragraph("Security & Uptime Checks", H3)]
    sec_h = ["Check", "Status", "Details"]
    sec_r = [
        ("SSL Certificate",     "\u2713 ACTIVE",  "Valid \u2014 expires [MM/DD/YYYY]"),
        ("HTTPS Redirect",      "\u2713 ACTIVE",  "All HTTP traffic auto-redirects to HTTPS"),
        ("Uptime This Quarter", "99.98%",          "2 min 42 sec total downtime \u2014 0 incidents"),
        ("Security Incidents",  "0 FOUND",         "No unauthorized access attempts logged"),
        ("Domain Expiry",       "\u2713 ACTIVE",  "Expires [MM/DD/YYYY] \u2014 auto-renew enabled"),
        ("DNS Health",          "\u2713 HEALTHY", "All DNS records resolving correctly"),
        ("Mobile Friendliness", "\u2713 PASSED",  "Google Mobile-Friendly Test: Pass"),
        ("Broken Links",        "0 FOUND",         "Full site crawl completed [Month YYYY]"),
        ("Form Functionality",  "\u2713 WORKING", "Contact form tested \u2014 submissions routing correctly"),
    ]
    sec_d = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in sec_h]]
    for name, status, detail in sec_r:
        s_col = GS_GREEN if ("\u2713" in status or status in ("0 FOUND", "99.98%")) else GS_AMBER
        sec_d.append([
            cell(name, size=8.5),
            Paragraph(status, sty(f"ss_{hash(status+name)}", fontSize=8.5,
                                  fontName="Helvetica-Bold", textColor=s_col,
                                  alignment=TA_CENTER, leading=13)),
            cell(detail, size=8, color=GS_GRAY),
        ])
    sec_t = Table(sec_d, colWidths=[1.75*inch, 1.15*inch, 3.35*inch])
    sec_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    s += [sec_t]
    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 6  —  REVIEW SUMMARY + WORK COMPLETED
# ═══════════════════════════════════════════════════════════════════════════════
def page_reviews_work():
    s = [PageBreak()]
    s += section_header("REVIEW SUMMARY", "Google Reviews")

    # Review KPI cards
    cw = [1.56*inch, 1.56*inch, 1.56*inch, 1.57*inch]
    s += [kpi_row_table([
        kpi_card("OVERALL RATING", "4.8 \u2605",  "Google Business Profile",
                 bg=GS_AMBER_L, border=GS_AMBER_B, val_color=GS_AMBER, w=1.5*inch),
        kpi_card("NEW REVIEWS",    "6",           "received this quarter",   w=1.5*inch),
        kpi_card("TOTAL REVIEWS",  "14",          "lifetime on Google",      w=1.5*inch),
        kpi_card("RESPONSE RATE",  "83%",         "reviews responded to",    w=1.5*inch),
    ], cw), blank(0.14)]

    # Rating breakdown
    s += [Paragraph("Rating Distribution", H3)]
    ratings = [
        ("\u2605\u2605\u2605\u2605\u2605  5 stars", 10, "71%"),
        ("\u2605\u2605\u2605\u2605\u2606  4 stars",  3, "21%"),
        ("\u2605\u2605\u2605\u2606\u2606  3 stars",  1,  "7%"),
        ("\u2605\u2605\u2606\u2606\u2606  2 stars",  0,  "0%"),
        ("\u2605\u2606\u2606\u2606\u2606  1 star",   0,  "0%"),
    ]
    rat_d = []
    for label, count, pct in ratings:
        c = GS_AMBER if count > 0 else GS_GRAY
        rat_d.append([
            Paragraph(label, sty(f"rl_{hash(label)}", fontSize=9, fontName="Helvetica",
                                 textColor=c, leading=13)),
            cell(str(count), bold=count > 0, size=9, align=TA_CENTER),
            cell(pct, size=9, color=GS_GRAY, align=TA_CENTER),
        ])
    rat_t = Table(rat_d, colWidths=[2.0*inch, 0.7*inch, 0.7*inch])
    rat_t.setStyle(TableStyle([
        ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
    ]))
    s += [rat_t, blank(0.14), hr(GS_BORDER)]

    # Work completed
    s += section_header("WORK COMPLETED", "Changes & Updates This Quarter")

    work_cats = [
        ("Content Updates", [
            "Updated services page with [X] new service descriptions provided by client",
            "Added [X] new project photos to gallery \u2014 compressed and optimized",
            "Revised homepage headline and intro paragraph",
            "Added testimonials section with [X] client quotes",
        ]),
        ("SEO Work", [
            "Updated all meta titles and descriptions with target keywords",
            "Fixed [X] missing alt-text tags on images",
            "Resubmitted updated XML sitemap to Google Search Console",
            "Optimized page load speed \u2014 reduced image file sizes by [X]%",
        ]),
        ("Technical Maintenance", [
            "SSL certificate verified and active",
            "Full link audit \u2014 0 broken links found",
            "Cross-browser testing: Chrome, Safari, Firefox, Edge",
            "Mobile responsiveness verified on latest iOS and Android",
        ]),
        ("Google Business Profile", [
            "Posted [X] service updates and photos to GBP",
            "Responded to [X] of [X] new reviews within 48 hours",
            "Updated business hours / holiday schedule as needed",
        ]),
    ]

    for cat, items in work_cats:
        cat_hdr = Table([[
            Paragraph(cat, sty(f"wch_{hash(cat)}", fontSize=9.5, fontName="Helvetica-Bold",
                               textColor=GS_GREEN, leading=13))
        ]], colWidths=[6.25*inch])
        cat_hdr.setStyle(TableStyle([
            ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
            ("BOX",           (0,0),(-1,-1), 0.5, GS_BORDER),
            ("TOPPADDING",    (0,0),(-1,-1), 6),
            ("BOTTOMPADDING", (0,0),(-1,-1), 6),
            ("LEFTPADDING",   (0,0),(-1,-1), 10),
        ]))
        s += [cat_hdr]
        item_d = [[
            Paragraph("\u2713", sty(f"wci_{hash(it)}", fontSize=9, fontName="Helvetica-Bold",
                                   textColor=GS_GREEN, alignment=TA_CENTER)),
            Paragraph(it, sty(f"wct_{hash(it)}", fontSize=9, fontName="Helvetica",
                              textColor=GS_DARK, leading=13)),
        ] for it in items]
        item_t = Table(item_d, colWidths=[0.28*inch, 5.97*inch])
        item_t.setStyle(TableStyle([
            ("VALIGN",        (0,0),(-1,-1), "TOP"),
            ("TOPPADDING",    (0,0),(-1,-1), 4),
            ("BOTTOMPADDING", (0,0),(-1,-1), 4),
            ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, GS_SLATE]),
            ("LINEBELOW",     (0,0),(-1,-1), 0.5, LINE),
            ("LEFTPADDING",   (1,0),(1,-1),  8),
        ]))
        s += [item_t, blank(0.06)]

    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 7  —  RECOMMENDATIONS + NEXT QUARTER GOALS
# ═══════════════════════════════════════════════════════════════════════════════
def page_recommendations():
    s = [PageBreak()]
    s += section_header("RECOMMENDATIONS", "Action Items & Q2 Goals")

    recs = [
        ("HIGH PRIORITY", GS_RED,    GS_RED_L,  GS_RED_B,
         "Grow Your Google Review Count",
         "You have 14 reviews with a strong 4.8 rating. Reaching 20+ reviews this quarter "
         "will meaningfully boost your local search ranking and build trust with new visitors. "
         "We recommend sending a follow-up text to recent customers with a direct link to your "
         "Google review page within 24 hours of job completion. "
         "<b>Target: 8 new reviews in Q2.</b>"),

        ("HIGH PRIORITY", GS_AMBER,  GS_AMBER_L, GS_AMBER_B,
         "Expand Content for Top Service Keywords",
         "Your top 2 keywords currently rank positions 4\u20136, which is strong. "
         "Several keywords in positions 8\u201315 could be moved into top 5 with a dedicated "
         "service page targeting that specific term. We recommend adding one new page for "
         "'[secondary service]' this quarter. "
         "<b>Estimated impact: +15% organic clicks.</b>"),

        ("MEDIUM PRIORITY", GS_BLUE_C, GS_BLUE, GS_BLUE_B,
         "Add a Before / After or Project Gallery Section",
         "Pages with visual content see significantly more time-on-site and lower bounce rates. "
         "Adding 10\u201315 photos of your recent work \u2014 with before/after comparisons where "
         "relevant \u2014 will give potential customers the visual proof they need to call. "
         "Send us the photos and we'll build it within the week. "
         "<b>Estimated completion: 5\u20137 days from content receipt.</b>"),

        ("ONGOING", GS_GREEN, GS_LIGHT, GS_BORDER,
         "Maintain Weekly Google Business Profile Posts",
         "GBP posting is directly contributing to your Discovery Search growth. "
         "Keeping 1 post per week going into Q2 will compound these results and signal "
         "to Google that your profile is active. "
         "<b>Included as part of the Growth Plan.</b>"),
    ]

    for priority, p_col, bg, bdr, title, desc in recs:
        box = Table([
            [Paragraph(priority, sty(f"rp_{hash(priority+title)}", fontSize=7.5,
                                     fontName="Helvetica-Bold", textColor=p_col,
                                     letterSpacing=1.2, spaceAfter=0))],
            [Paragraph(title, sty(f"rt_{hash(title)}", fontSize=11,
                                  fontName="Helvetica-Bold", textColor=GS_DARK,
                                  leading=14, spaceAfter=0))],
            [Paragraph(desc, sty(f"rd_{hash(desc)}", fontSize=9, fontName="Helvetica",
                                 textColor=GS_DARK, leading=14))],
        ], colWidths=[6.25*inch])
        box.setStyle(TableStyle([
            ("BACKGROUND",    (0,0),(-1,-1), bg),
            ("BOX",           (0,0),(-1,-1), 1.0, bdr),
            ("TOPPADDING",    (0,0),(0,0), 10),
            ("BOTTOMPADDING", (0,0),(0,0), 2),
            ("TOPPADDING",    (0,1),(0,1), 2),
            ("BOTTOMPADDING", (0,1),(0,1), 4),
            ("TOPPADDING",    (0,2),(0,2), 2),
            ("BOTTOMPADDING", (0,2),(0,2), 12),
            ("LEFTPADDING",   (0,0),(-1,-1), 14),
            ("RIGHTPADDING",  (0,0),(-1,-1), 14),
        ]))
        s += [box, blank(0.07)]

    # Next quarter goals table
    s += [blank(0.06), Paragraph("Q2 Goals & Focus Areas", H3)]
    g_h = ["Goal", "Target Metric", "Timeline", "Owner"]
    g_r = [
        ["Grow to 20+ Google reviews",           "20 total reviews",         "By end of Q2",   "Client (we provide link)"],
        ["Rank top 5 for [secondary keyword]",   "Position 1\u20135",        "8\u201310 weeks", "Groundwork Studio"],
        ["Launch gallery / before-after section","Live page, 15+ photos",    "Week 2 of Q2",   "Client sends photos"],
        ["Maintain site uptime above 99.9%",     "0 outages",                "All quarter",    "Groundwork Studio"],
        ["Reach 1,600 sessions in June",         "1,600/month by June",      "End of Q2",      "Organic + GBP growth"],
    ]
    gd = [[cell(h, bold=True, size=8, color=WHITE, align=TA_CENTER) for h in g_h]]
    for row in g_r:
        gd.append([cell(v, size=8.5) for v in row])
    g_t = Table(gd, colWidths=[1.85*inch, 1.35*inch, 1.0*inch, 2.05*inch])
    g_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0),  GS_GREEN),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, GS_SLATE]),
        ("GRID",          (0,0),(-1,-1), 0.5, LINE),
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
        ("TOPPADDING",    (0,0),(-1,-1), 7),
        ("BOTTOMPADDING", (0,0),(-1,-1), 7),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 6),
    ]))
    s += [g_t, blank(0.16)]

    # CTA
    cta = Table([
        [Paragraph("Questions? Let\u2019s connect.", sty("ctah", fontSize=13,
                   fontName="Helvetica-Bold", textColor=GS_GREEN,
                   alignment=TA_CENTER, spaceAfter=0))],
        [Paragraph(
            "Reply to this report, call, or text \u2014 we\u2019re always available to walk through anything here.<br/>"
            "<b>(480) 452-6473  \u00b7  evan@teamground.work  \u00b7  teamground.work</b>",
            sty("ctab", fontSize=10, fontName="Helvetica", textColor=GS_DARK,
                alignment=TA_CENTER, leading=16))],
    ], colWidths=[6.25*inch])
    cta.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), GS_LIGHT),
        ("BOX",           (0,0),(-1,-1), 2.0, GS_GREEN),
        ("TOPPADDING",    (0,0),(0,0), 14),
        ("BOTTOMPADDING", (0,0),(0,0), 4),
        ("TOPPADDING",    (0,1),(0,1), 4),
        ("BOTTOMPADDING", (0,1),(0,1), 16),
        ("LEFTPADDING",   (0,0),(-1,-1), 14),
        ("RIGHTPADDING",  (0,0),(-1,-1), 14),
    ]))
    s += [cta]
    s += footer()
    return s


# ═══════════════════════════════════════════════════════════════════════════════
def story():
    return (page_cover() + page_traffic() + page_search() +
            page_gbp() + page_technical() + page_reviews_work() +
            page_recommendations())


def build():
    os.makedirs(os.path.dirname(OUT_REPO), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT_REPO, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.65*inch,  bottomMargin=0.65*inch,
        title="Groundwork Studio — Quarterly Performance Report",
        author="Groundwork Studio AZ LLC",
    )
    doc.build(story())
    shutil.copy(OUT_REPO, OUT_DESK)
    print(f"\u2713 Quarterly Report saved to:\n  {OUT_REPO}\n  {OUT_DESK}")


if __name__ == "__main__":
    build()
