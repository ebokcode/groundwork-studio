#!/usr/bin/env python3
"""Generate Groundwork Studio Cold Calling Sales Guide PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os, shutil

OUT_REPO = "/Users/evanbaukol/Sites/groundwork-studio/docs/Groundwork_Cold_Calling_Guide.pdf"
OUT_DESK = "/Users/evanbaukol/Desktop/Groundwork Studio \u2014 Docs/Groundwork_Cold_Calling_Guide.pdf"

# ── Colors ────────────────────────────────────────────────────────────────────
GS_GREEN  = colors.HexColor("#16a34a")
GS_DARK   = colors.HexColor("#111827")
GS_GRAY   = colors.HexColor("#6b7280")
GS_LIGHT  = colors.HexColor("#f0fdf4")
GS_BORDER = colors.HexColor("#d1fae5")
GS_RED    = colors.HexColor("#dc2626")
GS_AMBER  = colors.HexColor("#d97706")

# ── Styles ────────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def style(name, **kw):
    s = ParagraphStyle(name, **kw)
    return s

H1 = style("H1", fontSize=22, fontName="Helvetica-Bold", textColor=GS_DARK,
           spaceAfter=4, spaceBefore=16)
H2 = style("H2", fontSize=13, fontName="Helvetica-Bold", textColor=GS_GREEN,
           spaceAfter=6, spaceBefore=14)
H3 = style("H3", fontSize=11, fontName="Helvetica-Bold", textColor=GS_DARK,
           spaceAfter=4, spaceBefore=10)
BODY = style("BODY", fontSize=9.5, fontName="Helvetica", textColor=GS_DARK,
             spaceAfter=4, leading=14)
SMALL = style("SMALL", fontSize=8.5, fontName="Helvetica", textColor=GS_GRAY,
              spaceAfter=3, leading=13)
MONO = style("MONO", fontSize=9, fontName="Courier", textColor=GS_DARK,
             spaceAfter=3, leading=14, backColor=colors.HexColor("#f9fafb"),
             leftIndent=8, rightIndent=8)
LABEL = style("LABEL", fontSize=8, fontName="Helvetica-Bold",
              textColor=GS_GREEN, spaceAfter=2, spaceBefore=8,
              letterSpacing=1.5)

def div(color=GS_BORDER, thickness=1): return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=2)

def story():
    s = []

    # ── COVER ──────────────────────────────────────────────────────────────────
    s += [
        Spacer(1, 0.5*inch),
        Paragraph("GROUNDWORK STUDIO", style("cov_label", fontSize=9, fontName="Helvetica-Bold",
                  textColor=GS_GREEN, alignment=TA_CENTER, letterSpacing=3)),
        Spacer(1, 0.1*inch),
        Paragraph("Cold Calling<br/>Sales Guide", style("cov_h1", fontSize=32, fontName="Helvetica-Bold",
                  textColor=GS_DARK, alignment=TA_CENTER, leading=38)),
        Spacer(1, 0.15*inch),
        Paragraph("Scripts · Pipeline · Objection Handling · Question Answers",
                  style("cov_sub", fontSize=11, fontName="Helvetica", textColor=GS_GRAY,
                        alignment=TA_CENTER)),
        Spacer(1, 0.3*inch),
        div(GS_GREEN, 2),
        Spacer(1, 0.15*inch),
        Paragraph("teamground.work · evan@teamground.work · (480) 452-6473",
                  style("cov_contact", fontSize=9, fontName="Helvetica", textColor=GS_GRAY,
                        alignment=TA_CENTER)),
        PageBreak(),
    ]

    # ── SECTION 1: THE MINDSET ─────────────────────────────────────────────────
    s += [
        Paragraph("SECTION 1", LABEL),
        Paragraph("The Mindset", H1),
        div(),
        Paragraph(
            "Cold calling is not about selling a website on the first call. It's about "
            "opening a conversation with a business owner who doesn't know you exist yet. "
            "Your only job on call #1 is to get them curious enough to look at a demo.",
            BODY),
        Spacer(1, 0.1*inch),
        Paragraph("Three rules before you dial:", H3),
    ]

    rules = [
        ["1.", "You are solving a real problem.", "Most local businesses leave money on the table because their online presence is weak or nonexistent. You are not bothering them — you are offering a solution."],
        ["2.", "Every no is just missing information.", "They said no because they don't have enough context. Your job is to figure out what's missing and fill that gap."],
        ["3.", "The demo does the selling.", "You don't need to close on the call. Get them to a demo link. The work speaks for itself."],
    ]
    tdata = [[Paragraph(c, BODY if i > 0 else style(f"num_{i}_{j}", fontSize=11, fontName="Helvetica-Bold", textColor=GS_GREEN)) for i, c in enumerate(row)] for j, row in enumerate(rules)]
    t = Table(tdata, colWidths=[0.35*inch, 1.4*inch, 4.5*inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
    ]))
    s += [t, Spacer(1, 0.15*inch)]

    # ── SECTION 2: THE SCRIPTS ────────────────────────────────────────────────
    s += [
        Paragraph("SECTION 2", LABEL),
        Paragraph("The Scripts", H1),
        div(),

        Paragraph("Cold Open (No Website)", H2),
        Paragraph(
            "<i>Use when the business has no website or a very outdated one.</i>", SMALL),
        Paragraph(
            '"Hi, is this [Name]? Hey — this is Evan calling from Groundwork Studio. '
            'We build websites for [industry] businesses here in Phoenix. I actually '
            'pulled up your business online and noticed you don\'t have a website set up '
            'yet — is that something you\'ve thought about? ... [pause] ... '
            'Yeah totally — I\'d love to just shoot you a quick link to a demo site I built '
            'for another [industry] company. Takes about 30 seconds to look at. '
            'What\'s the best email to send it to?"',
            MONO),
        Spacer(1, 0.1*inch),

        Paragraph("Cold Open (Has a Website)", H2),
        Paragraph(
            "<i>Use when the business has a site but it looks dated or underperforming.</i>", SMALL),
        Paragraph(
            '"Hi [Name], this is Evan with Groundwork Studio — we build custom websites '
            'for service businesses in Phoenix. I checked out your site and I think we '
            'could make it a lot more effective for you — like getting more calls coming '
            'in from Google. I\'m not trying to do a big pitch — I just want to send you '
            'a quick demo so you can see the difference. What\'s a good email?"',
            MONO),
        Spacer(1, 0.1*inch),

        Paragraph("The Voicemail", H2),
        Paragraph(
            '"Hey [Name], this is Evan from Groundwork Studio — we build websites for '
            '[industry] businesses in Phoenix. I was going to send you a quick demo '
            'but wanted to make sure I had the right contact first. '
            'Give me a call back at (480) 452-6473, or I\'ll try you again in a couple '
            'days. Thanks."',
            MONO),
        Spacer(1, 0.1*inch),

        Paragraph("The Follow-Up (2nd Contact)", H2),
        Paragraph(
            '"Hey [Name], Evan from Groundwork Studio again — I sent over a demo site '
            'a few days ago, just wanted to make sure you had a chance to see it. '
            'I know it\'s busy — even just 30 seconds on it would be worth your time. '
            'Happy to jump on a quick call if you have questions. '
            'You can reach me at (480) 452-6473."',
            MONO),
    ]

    s.append(PageBreak())

    # ── SECTION 3: PIPELINE ───────────────────────────────────────────────────
    s += [
        Paragraph("SECTION 3", LABEL),
        Paragraph("Pipeline View", H1),
        div(),
        Paragraph("Track every prospect through these stages. One row per lead.", BODY),
        Spacer(1, 0.1*inch),
    ]

    pipeline_header = ["Stage", "Definition", "Your Action", "Move Forward When..."]
    pipeline_rows = [
        ["PROSPECT",
         "Found the lead, not yet contacted",
         "Research: do they have a site? What industry? Find a name.",
         "You have a name and phone number."],
        ["CONTACTED",
         "Left voicemail or spoke briefly",
         "Log call date. Schedule follow-up in 2-3 days.",
         "They expressed any interest or asked a question."],
        ["INTERESTED",
         "Engaged in conversation, wants to know more",
         "Send the most relevant demo link. Confirm email received.",
         "They opened/clicked the demo or responded."],
        ["DEMO SENT",
         "Demo link has been sent",
         "Follow up 2 days later. Ask: 'Did you get a chance to check it out?'",
         "They want to talk pricing or next steps."],
        ["IN CONVERSATION",
         "Active back-and-forth happening",
         "Answer questions. Send tier options. Keep momentum.",
         "They ask 'how do we move forward?' or agree to a proposal."],
        ["CLOSED / WON",
         "Deposit received, contract signed",
         "Send contract + invoice. Begin intake process.",
         "—"],
        ["CLOSED / LOST",
         "Said no or gone dark",
         "Note the reason. Re-queue in 60 days.",
         "—"],
    ]

    pdata = [[Paragraph(c, style(f"pt_{i}_{j}", fontSize=8.5, fontName="Helvetica-Bold" if i==0 else "Helvetica",
                                  textColor=colors.white if hdr else GS_DARK,
                                  leading=13))
              for i, c in enumerate(row)]
             for j, (hdr, row) in enumerate([(True, pipeline_header)] + [(False, r) for r in pipeline_rows])]

    col_w = [1.15*inch, 1.45*inch, 1.9*inch, 1.75*inch]
    pt = Table(pdata, colWidths=col_w)
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), GS_GREEN),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f9fafb")]),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#e5e7eb")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    s += [pt, Spacer(1, 0.2*inch)]

    s.append(PageBreak())

    # ── SECTION 4: OBJECTION HANDLING ─────────────────────────────────────────
    s += [
        Paragraph("SECTION 4", LABEL),
        Paragraph("Turning No's Into Yes's", H1),
        div(),
        Paragraph(
            "Every objection is a request for more information. "
            "Don't argue — agree, empathize, then redirect.", BODY),
        Spacer(1, 0.1*inch),
    ]

    objections = [
        ("We already have a website.",
         "Totally — is it currently getting you new customers? ... "
         "A lot of businesses have a site but it's not actually working for them. "
         "I'd love to show you what a site built specifically to convert looks like. "
         "Can I send you a demo?"),
        ("We can't afford it right now.",
         "I hear that a lot — what does your timeline look like for the year? "
         "... Our builds are one-time, no ongoing platform fees. "
         "We also structure payment in two halves so it doesn't hit all at once. "
         "What would a realistic number look like for you?"),
        ("I'm not interested.",
         "Fair enough — can I ask what's holding you back? Is it timing, budget, "
         "or you're just not thinking about a website right now? "
         "... [if timing] When would be a better time to circle back?"),
        ("Call me back later.",
         "Of course — what day works? I'll put it in my calendar right now. "
         "... [confirm day/time and name] Perfect, I'll call you [day] at [time]. "
         "I'll shoot you a quick text so you have my number."),
        ("We handle our marketing in-house.",
         "Smart — does that include the website too? "
         "I only ask because a lot of in-house teams prefer to outsource the development "
         "side to keep things clean. We build it, you own it, your team manages the content."),
        ("How do I know you're legit?",
         "Great question — we're a registered LLC in Arizona, and I can send you our "
         "business registration, contract, and a few demo sites right now. "
         "Everything's documented. Want me to shoot that over?"),
        ("We use [Wix / Squarespace / GoDaddy].",
         "Those are great for getting something up fast. The difference with us is "
         "we hand-code everything — no templates, no platform lock-in, no $30/month fees. "
         "Your site is faster, unique, and you own it outright. "
         "Can I send you a quick comparison?"),
    ]

    for idx, (obj, resp) in enumerate(objections):
        block = [
            [Paragraph(f'"{obj}"',
                       style(f"obj_q_{idx}", fontSize=9.5, fontName="Helvetica-Bold",
                             textColor=GS_DARK, leading=14)),
             Paragraph(f'"{resp}"',
                       style(f"obj_a_{idx}", fontSize=9, fontName="Helvetica",
                             textColor=GS_DARK, leading=14))],
        ]
        bt = Table(block, colWidths=[2.6*inch, 3.65*inch])
        bt.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,0), GS_LIGHT),
            ("BACKGROUND", (1,0), (1,0), colors.white),
            ("BOX", (0,0), (-1,-1), 0.5, GS_BORDER),
            ("LINEAFTER", (0,0), (0,-1), 0.5, GS_BORDER),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 9),
            ("BOTTOMPADDING", (0,0), (-1,-1), 9),
            ("LEFTPADDING", (0,0), (-1,-1), 10),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ]))
        s += [bt, Spacer(1, 0.06*inch)]

    s.append(PageBreak())

    # ── SECTION 5: QUESTION ANSWERS ───────────────────────────────────────────
    s += [
        Paragraph("SECTION 5", LABEL),
        Paragraph("Answering Specific Questions", H1),
        div(),
        Paragraph(
            "These are the questions prospects ask most. Know these cold — "
            "you should be able to answer without thinking.", BODY),
        Spacer(1, 0.15*inch),
    ]

    qas = [
        (
            "How do you build these sites?",
            "We hand-code everything from scratch — no Wix, no WordPress, no templates. "
            "Every site is written in clean HTML, CSS, and JavaScript specifically for "
            "that business. That means it loads faster, looks completely unique, and you're "
            "not paying $30-40 a month to some platform forever. "
            "You own the site outright once it's paid off.",
        ),
        (
            "Who hosts it?",
            "We host it on a professional platform called Netlify — it's what major tech "
            "companies use. It's included in your monthly retainer. "
            "If you ever want to move it somewhere else, we can do that too for a small "
            "one-time migration fee.",
        ),
        (
            "What's the monthly fee for?",
            "The retainer covers hosting, security, any content updates you send us, "
            "and having someone to call when something needs to change. "
            "You're not just paying for the site to stay online — "
            "you're paying for a developer on call.",
        ),
        (
            "What if I want to cancel?",
            "No problem — 30 days written notice and you're done. "
            "If you want to keep the site, we migrate it to your own hosting for a one-time fee. "
            "Nothing gets deleted without your say-so.",
        ),
        (
            "How long does it take?",
            "Most sites are live within 2-3 weeks from when we receive your content. "
            "The biggest delay is usually getting photos and text from the client — "
            "the build itself is fast.",
        ),
        (
            "Can I see examples?",
            "Absolutely — I'll send you the demo most relevant to your industry. "
            "We have sites built for HVAC, plumbing, landscaping, pest control, "
            "electrical, cleaning, pool service, painting, and more. "
            "Which one fits your business closest?",
        ),
        (
            "Do you do SEO?",
            "Every site we build is SEO-ready out of the box — proper meta tags, fast load times, "
            "mobile-first design, and Google-readable structure. That gives you a stronger foundation "
            "than most agencies start with. We also offer a one-time Local SEO Setup add-on for $250. "
            "That covers Google Business Profile setup and optimization, schema markup so Google knows "
            "exactly what your business is, citation submissions to Yelp, BBB, and Apple Maps, "
            "and a keyword research doc for your top 5 search terms. Done once, no monthly fees. "
            "Most clients add it on — it's the fastest way to start showing up locally.",
        ),
        (
            "What's your LLC or business registration?",
            "We're registered as Groundwork Studio AZ LLC in the state of Arizona. "
            "I can send you our business registration, a signed contract template, "
            "and references from current clients. Whatever you need to feel comfortable.",
        ),
    ]

    for q, a in qas:
        s += [
            Paragraph(f"Q: {q}", H3),
            Paragraph(f"A: {a}", BODY),
            div(colors.HexColor("#e5e7eb"), 0.5),
        ]

    # ── FOOTER PAGE ───────────────────────────────────────────────────────────
    s += [
        PageBreak(),
        Spacer(1, 1*inch),
        Paragraph("Quick Reference", style("qr_h", fontSize=18, fontName="Helvetica-Bold",
                  textColor=GS_DARK, alignment=TA_CENTER)),
        Spacer(1, 0.2*inch),
        div(GS_GREEN, 2),
        Spacer(1, 0.2*inch),
    ]

    ref = [
        ["First call goal:", "Get them to accept a demo link or give their email"],
        ["Second contact:", "2-3 days after first call"],
        ["Demo follow-up:", "2 days after sending the link"],
        ["Voicemail rule:", "Max 2 voicemails — then email"],
        ["Never say:", '"I\'m just calling to check in" — always have a purpose'],
        ["Always end with:", "A specific next action (email, callback day, demo link)"],
        ["Answer to any tech Q:", '"We hand-code it from scratch — no templates, no platform fees"'],
        ["Local SEO add-on:", "$250 one-time — GBP setup, schema markup, citations, keyword doc"],
        ["LLC name on contract:", "Groundwork Studio AZ LLC"],
        ["Contact:", "evan@teamground.work · (480) 452-6473 · teamground.work"],
    ]

    rdata = [[Paragraph(c, style(f"r{i}_{j}", fontSize=9.5,
                                  fontName="Helvetica-Bold" if i==0 else "Helvetica",
                                  textColor=GS_GREEN if i==0 else GS_DARK,
                                  leading=14)) for i, c in enumerate(row)] for j, row in enumerate(ref)]
    rt = Table(rdata, colWidths=[2*inch, 4.25*inch])
    rt.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [colors.white, colors.HexColor("#f9fafb")]),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#e5e7eb")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
    ]))
    s += [rt]

    return s


def build():
    os.makedirs(os.path.dirname(OUT_REPO), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT_REPO, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
        title="Groundwork Studio Cold Calling Guide",
        author="Groundwork Studio AZ LLC",
    )
    doc.build(story())
    shutil.copy(OUT_REPO, OUT_DESK)
    print(f"✓ Sales guide saved to:\n  {OUT_REPO}\n  {OUT_DESK}")


if __name__ == "__main__":
    build()
