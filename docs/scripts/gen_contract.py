#!/usr/bin/env python3
"""Generate Groundwork Studio AZ LLC Web Design Services Agreement PDF."""

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

OUT_REPO = "/Users/evanbaukol/Sites/groundwork-studio/docs/Groundwork_Contract_Template.pdf"
OUT_DESK = "/Users/evanbaukol/Desktop/Groundwork Studio \u2014 Docs/Groundwork_Contract_Template.pdf"

GS_GREEN  = colors.HexColor("#16a34a")
GS_DARK   = colors.HexColor("#111827")
GS_GRAY   = colors.HexColor("#6b7280")
GS_LIGHT  = colors.HexColor("#f0fdf4")
GS_BORDER = colors.HexColor("#d1fae5")
LINE      = colors.HexColor("#e5e7eb")

def sty(name, **kw): return ParagraphStyle(name, **kw)

TITLE  = sty("TITLE", fontSize=18, fontName="Helvetica-Bold", textColor=GS_DARK, alignment=TA_CENTER, spaceAfter=2)
SUB    = sty("SUB",   fontSize=9,  fontName="Helvetica", textColor=GS_GRAY, alignment=TA_CENTER, spaceAfter=6)
LABEL  = sty("LABEL", fontSize=7.5, fontName="Helvetica-Bold", textColor=GS_GREEN, spaceAfter=2, spaceBefore=10, letterSpacing=1.5)
H2     = sty("H2",    fontSize=10.5, fontName="Helvetica-Bold", textColor=GS_DARK, spaceAfter=4, spaceBefore=10)
BODY   = sty("BODY",  fontSize=9,  fontName="Helvetica", textColor=GS_DARK, spaceAfter=3, leading=14, alignment=TA_JUSTIFY)
FIELD  = sty("FIELD", fontSize=9,  fontName="Helvetica", textColor=GS_DARK, spaceAfter=2, leading=13)
SMALL  = sty("SMALL", fontSize=7.5, fontName="Helvetica", textColor=GS_GRAY, spaceAfter=2, leading=12, alignment=TA_CENTER)

def hr(color=LINE, t=0.75): return HRFlowable(width="100%", thickness=t, color=color, spaceAfter=6, spaceBefore=4)
def blank(h=0.08): return Spacer(1, h*inch)


def field(label):
    t = Table(
        [[Paragraph(label, sty(f"fl_{hash(label)}", fontSize=8.5, fontName="Helvetica-Bold",
                               textColor=GS_GRAY)), ""]],
        colWidths=[1.7*inch, 4.55*inch]
    )
    t.setStyle(TableStyle([
        ("LINEBELOW", (1,0), (1,0), 0.75, GS_DARK),
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    return t


def story():
    s = []

    # ── HEADER ────────────────────────────────────────────────────────────────
    s += [
        blank(0.2),
        Paragraph("Web Design Services Agreement", TITLE),
        blank(0.1),
        Paragraph("Groundwork Studio AZ LLC", sty("co", fontSize=11, fontName="Helvetica-Bold",
                  textColor=GS_GREEN, alignment=TA_CENTER, spaceAfter=0)),
        blank(0.07),
        Paragraph("Arizona Limited Liability Company · teamground.work", SUB),
        blank(0.18),
        hr(GS_GREEN, 1.5),
        blank(0.12),
    ]

    # ── PARTIES ───────────────────────────────────────────────────────────────
    sp_data = [
        [Paragraph("SERVICE PROVIDER", sty("sp_hdr", fontSize=8, fontName="Helvetica-Bold",
                   textColor=GS_GREEN, letterSpacing=1.5)),
         Paragraph("CLIENT", sty("cl_hdr", fontSize=8, fontName="Helvetica-Bold",
                   textColor=GS_GREEN, letterSpacing=1.5))],
        [Paragraph("Groundwork Studio AZ LLC", sty("sp1", fontSize=10, fontName="Helvetica-Bold", textColor=GS_DARK, leading=15)),
         Paragraph("Business / Client Name", sty("cl1", fontSize=8.5, fontName="Helvetica-Bold", textColor=GS_GRAY, leading=15))],
        [Paragraph("Evan Baukol, Owner", FIELD),
         Paragraph("_" * 38, FIELD)],
        [Paragraph("teamground.work", FIELD),
         Paragraph("Contact Name", sty("cl2", fontSize=8.5, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("evan@teamground.work", FIELD),
         Paragraph("_" * 38, FIELD)],
        [Paragraph("(480) 452-6473", FIELD),
         Paragraph("Phone / Email", sty("cl3", fontSize=8.5, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("AZ LLC Reg. No. on file", sty("azreg", fontSize=8, fontName="Helvetica", textColor=GS_GRAY)),
         Paragraph("_" * 38, FIELD)],
        [Paragraph("", FIELD),
         Paragraph("Address", sty("cl4", fontSize=8.5, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("", FIELD),
         Paragraph("_" * 38, FIELD)],
    ]
    sp_t = Table(sp_data, colWidths=[3.0*inch, 3.25*inch])
    sp_t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LINEAFTER", (0,0), (0,-1), 0.5, LINE),
        ("LEFTPADDING", (1,0), (1,-1), 16),
    ]))
    s += [sp_t, blank(0.05), hr()]

    # ── PROJECT SCOPE ─────────────────────────────────────────────────────────
    s += [
        Paragraph("PROJECT SCOPE", LABEL),
    ]
    scope_data = [
        [Paragraph("PROJECT TITLE", sty("ptl", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY)),
         Paragraph("TIER", sty("tier", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY)),
         Paragraph("EST. LAUNCH DATE", sty("eld", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY))],
        [Paragraph("_" * 38, FIELD), Paragraph("_" * 10, FIELD), Paragraph("_" * 18, FIELD)],
    ]
    scope_t = Table(scope_data, colWidths=[3.2*inch, 1.0*inch, 2.05*inch])
    scope_t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 4),
    ]))
    s += [scope_t, blank(0.05)]

    s += [Paragraph("DELIVERABLES — Pages / Features Included", sty("dl_hdr", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GRAY))]
    for _ in range(3):
        s += [Paragraph("_" * 105, FIELD)]
    s += [blank(0.05), hr()]

    # ── FEES & PAYMENT ────────────────────────────────────────────────────────
    s += [Paragraph("FEES & PAYMENT", LABEL)]
    fee_hdr = ["BUILD FEE (ONE-TIME)", "DEPOSIT DUE NOW (50%)", "BALANCE DUE AT LAUNCH (50%)", "MONTHLY RETAINER"]
    fee_val = ["$__________", "$__________", "$__________", "$__________"]
    fee_t = Table(
        [[Paragraph(c, sty(f"fh{i}", fontSize=7.5, fontName="Helvetica-Bold", textColor=GS_GRAY, alignment=TA_CENTER)) for i, c in enumerate(fee_hdr)],
         [Paragraph(c, sty(f"fv{i}", fontSize=14, fontName="Helvetica-Bold", textColor=GS_DARK, alignment=TA_CENTER)) for i, c in enumerate(fee_val)]],
        colWidths=[1.5*inch, 1.6*inch, 1.7*inch, 1.45*inch]
    )
    fee_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), GS_LIGHT),
        ("BOX", (0,0), (-1,-1), 0.75, GS_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.5, GS_BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    s += [fee_t, blank(0.06)]
    s += [Paragraph(
        "Work begins upon receipt of the 50% deposit. Balance is due on launch day before the site goes live. "
        "Monthly retainer begins on the first of the month following launch. "
        "Invoices unpaid after 14 days incur a 1.5% monthly late fee. "
        "Payments may be made via invoice (Wave), check, or ACH.",
        BODY), hr()]

    # ── TERMS & CONDITIONS ────────────────────────────────────────────────────
    s += [Paragraph("TERMS & CONDITIONS", LABEL)]

    terms = [
        ("1. Revisions",
         "The build fee includes two (2) rounds of revisions. A revision round is a single consolidated list of changes "
         "submitted at one time via email. Additional revision rounds are billed at $75/hour, invoiced separately."),
        ("2. Client Content",
         "Client is responsible for providing all text, photos, logos, and other content required for the project. "
         "Content must be delivered within 14 days of signing. If content is not received within 14 days, a $200 delay "
         "fee will be invoiced and the project timeline will be adjusted accordingly."),
        ("3. Hosting & Ownership",
         "The completed website will be hosted on Groundwork Studio AZ LLC's infrastructure and covered under the monthly "
         "retainer. Client owns all website content (text, images, copy authored by client). Groundwork Studio AZ LLC retains "
         "ownership of the underlying code, structure, and design until the build fee is paid in full. Upon cancellation of "
         "the monthly retainer, client may request a site migration for a one-time $250 migration fee."),
        ("4. Intellectual Property",
         "Client warrants they own or have licensed rights to all content provided. Unless client opts out in writing at "
         "signing, client grants Groundwork Studio AZ LLC permission to display the completed website in its portfolio, "
         "case studies, and marketing materials."),
        ("5. 35-Day Satisfaction Guarantee",
         "If client is not satisfied with the completed website, or the site has not generated measurable results, "
         "client may request a full refund of the build fee within 35 days of the site going live. "
         "To invoke this guarantee, client must submit a written refund request via email to evan@teamground.work "
         "within the 35-day window. Upon receipt, Groundwork Studio AZ LLC will process the full build fee refund "
         "within 5 business days. The website will be taken offline upon refund. "
         "Any monthly retainer fees paid during the live period are also refunded in full under this clause. "
         "This guarantee applies to the build fee only and does not apply if cancellation is requested before launch."),
        ("6. Pre-Launch Cancellation",
         "If client cancels after work has begun but before the site goes live, the deposit is non-refundable. "
         "Any work completed beyond the deposit value will be invoiced at $75/hour. "
         "Groundwork Studio AZ LLC may suspend or cancel this agreement with 14 days written notice if client is "
         "unresponsive for 30+ consecutive days or if payment is outstanding beyond 30 days."),
        ("7. Warranties & Liability",
         "Groundwork Studio AZ LLC will build the site to professional standards and maintain it under the monthly retainer. "
         "We warrant the site will function as designed on major current browsers (Chrome, Safari, Firefox, Edge) at launch. "
         "Groundwork Studio AZ LLC is not liable for losses resulting from website downtime, third-party service outages "
         "(including hosting providers, domain registrars, or payment processors), or errors in content provided by the client. "
         "Total liability under this agreement is limited to fees paid in the 30 days prior to the claim."),
        ("8. Termination of Monthly Retainer",
         "Either party may terminate the monthly retainer by providing 30 days written notice via email. The retainer fee "
         "for the final 30-day notice period is non-refundable. The website will remain live through the end of the notice "
         "period. Upon termination, the site will be taken offline unless client has paid the migration fee ($250) in advance. "
         "All outstanding balances must be settled before any migration or handoff."),
        ("9. Confidentiality",
         "Both parties agree to keep confidential any proprietary business information shared during the course of this "
         "engagement and not to disclose it to third parties without prior written consent, except as required by law."),
        ("10. Governing Law",
         "This agreement is governed by the laws of the State of Arizona. Groundwork Studio AZ LLC is a registered Arizona "
         "Limited Liability Company. Any disputes shall be resolved in Maricopa County, Arizona. The parties agree to attempt "
         "good-faith resolution before initiating formal proceedings."),
        ("11. Entire Agreement",
         "This document constitutes the entire agreement between the parties and supersedes all prior communications, "
         "proposals, or representations. Modifications must be made in writing and signed by both parties. "
         "This agreement is valid when signed by both parties, including via electronic signature (DocuSign or equivalent)."),
    ]

    for title, text in terms:
        s += [
            Paragraph(title, H2),
            Paragraph(text, BODY),
        ]

    s.append(PageBreak())

    # ── SIGNATURES ────────────────────────────────────────────────────────────
    s += [
        blank(0.1),
        Paragraph("SIGNATURES", LABEL),
        hr(GS_GREEN, 1.5),
        blank(0.1),
        Paragraph(
            "By signing below, both parties agree to the terms of this Web Design Services Agreement. "
            "Electronic signatures via DocuSign or equivalent platforms are legally binding.",
            BODY),
        blank(0.15),
    ]

    sig_data = [
        [Paragraph("SERVICE PROVIDER", sty("sphdr", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GREEN, letterSpacing=1.5)),
         Paragraph("CLIENT", sty("clhdr", fontSize=8, fontName="Helvetica-Bold", textColor=GS_GREEN, letterSpacing=1.5))],
        [Paragraph("Signature: " + "_" * 26, FIELD), Paragraph("Signature: " + "_" * 26, FIELD)],
        [Paragraph("Printed Name: Evan Baukol", FIELD), Paragraph("Printed Name: " + "_" * 22, FIELD)],
        [Paragraph("Title: Owner, Groundwork Studio AZ LLC", FIELD), Paragraph("Title: " + "_" * 28, FIELD)],
        [Paragraph("Date: " + "_" * 30, FIELD), Paragraph("Date: " + "_" * 30, FIELD)],
    ]
    sig_t = Table(sig_data, colWidths=[3.0*inch, 3.25*inch])
    sig_t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LINEAFTER", (0,0), (0,-1), 0.5, LINE),
        ("LEFTPADDING", (1,0), (1,-1), 20),
    ]))
    s += [sig_t, blank(0.25)]
    s += [
        hr(GS_BORDER),
        Paragraph(
            "Groundwork Studio AZ LLC · teamground.work · evan@teamground.work · (480) 452-6473 · Phoenix, AZ<br/>"
            "<i>This is a template — consult a licensed attorney before use. Compatible with DocuSign and electronic signature platforms.</i>",
            SMALL),
    ]

    return s


def build():
    os.makedirs(os.path.dirname(OUT_REPO), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT_REPO, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
        title="Groundwork Studio AZ LLC — Web Design Services Agreement",
        author="Groundwork Studio AZ LLC",
    )
    doc.build(story())
    shutil.copy(OUT_REPO, OUT_DESK)
    print(f"✓ Contract saved to:\n  {OUT_REPO}\n  {OUT_DESK}")


if __name__ == "__main__":
    build()
