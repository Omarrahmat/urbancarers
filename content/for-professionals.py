"""For professionals: https://www.urbancarers.co.uk/for-professionals  (source: src/routes/for-professionals.tsx)"""

SUPPORT = [
    ["Independent living skills", "The everyday skills needed to run a home and live independently."],
    ["Budgeting and money", "Managing money, bills and benefits."],
    ["Education, employment and training", "College and ESOL enrolment, CVs, job searches, interview preparation and attendance."],
    ["Health and wellbeing", "Managing health appointments, accessing services and looking after emotional wellbeing."],
    ["Tenancy readiness and move-on", "Understanding tenancy responsibilities and planning the next home."],
    ["Support for asylum-seeking young people", "Orientation, cultural adjustment, ESOL access, help navigating UK systems, and links to faith and cultural communities."],
]

PAGE = {
    "path": "/for-professionals",
    "title": "For Social Workers and Personal Advisers | Urban Carers",
    "description": "How to refer a care leaver or asylum-seeking young person aged 18–25 to our supported accommodation in South London: what to include, response times, support and safeguarding.",
    "breadcrumb": "For professionals",
    "hero": {
        "eyebrow": "For professionals",
        "h1": "For social workers and personal advisers",
        "lead": "Everything you need to refer a care leaver or asylum-seeking young person aged 18–25 to Urban Carers: what we need from you, how quickly we respond, the support we provide and how we keep young people safe.",
    },
    "sections": [
        {
            "type": "section",
            "title": "Who we can accept",
            "intro": "Urban Carers Ltd provides non-regulated 18+ supported accommodation and housing-related support in South London. We work with leaving care teams, asylum-seeking young people's teams and placements teams from any local authority, in London or beyond. We accept young adults aged 18 to 25 only. We don't accept 16 and 17 year olds.",
            "blocks": [
                {"type": "pros_cons", "cols": [
                    {"title": "We can usually help", "kind": "check", "items": [
                        "Care leavers aged 18–25 who need supported accommodation",
                        "Unaccompanied asylum-seeking young people (UASC) and former UASC aged 18–25",
                        "Young adults with low to medium support needs who are ready to build towards living independently",
                        "Young people stepping down from a more intensive placement as a planned move",
                    ]},
                    {"title": "We're not the right placement for", "kind": "x", "items": [
                        "Young people who need personal, intimate or nursing care",
                        "Young people who need 24-hour supervision or regulated care",
                        "High risk to self or others that can't be managed safely in a shared home",
                        "Active needs that call for a clinical or therapeutic placement",
                    ]},
                ]},
                {"type": "p", "text": 'Referring an unaccompanied asylum-seeking young person? See <a href="/asylum-seeking-young-people" class="link">our support for asylum-seeking young people</a>.', "style": "note"},
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "What to include in a referral",
            "intro": "The more we have at the start, the faster we can give you a decision. Please send:",
            "blocks": [
                {"type": "icon_list", "icon": "check", "items": [
                    "An up-to-date risk assessment",
                    "The pathway plan or support plan",
                    "Key contacts: the social worker or personal adviser, and any other professionals involved",
                    "Any restrictions or conditions that affect where or how the young person can live",
                    "For asylum-seeking young people, their immigration status",
                    "The move-in date you're hoping for, and whether it's a planned move or an emergency",
                ]},
                {"type": "p", "text": "You can use our online referral form or call us on 07342 045712. Please don't put the young person's name in the website form. We'll agree a secure way to receive their details.", "style": "note", "narrow": True},
                {"type": "buttons", "items": [{"label": "Make a referral", "href": "/referrals", "variant": "primary", "size": "sm"}]},
            ],
        },
        {
            "type": "section",
            "title": "How quickly we respond",
            "blocks": [
                {"type": "steps", "cols": 4, "items": [
                    "Acknowledged within 2 working hours",
                    "A placement decision within 24 hours of full referral information",
                    "Emergencies prioritised: please call us as well as sending the form",
                    "Move-in planned with you",
                ]},
                {"type": "h3", "text": "Matching with the household"},
                {"type": "p", "text": "Our house is a shared home, so before we say yes we think carefully about the young people already living there. We look at each young person's needs, routines and risks alongside the current household, and we only offer a room when we're confident the placement can work for everyone. Our current house is for young men aged 18–25. If we don't think a placement is right, we'll tell you quickly so you can keep searching.", "style": "after-h3"},
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Support we provide",
            "intro": "Every young person has at least 5 hours of structured key-work support a week, including weekly key-work sessions, with management on call around the clock. Extra hours or night support can be arranged.",
            "blocks": [{"type": "cards", "cols": 3, "items": [{"title": t, "text": d} for t, d in SUPPORT]}],
        },
        {
            "type": "section",
            "title": "Working with you on the pathway plan",
            "blocks": [{"type": "p", "text": "We work alongside the young person's social worker or personal adviser, not in place of them. Key work is planned around the goals in the pathway plan, so the time a young person spends with us moves them towards the next step you've agreed together. The placing local authority receives a written weekly key-work report, and we'll contact you promptly if anything changes or if we have a concern.", "style": "first"}],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Safeguarding and staff",
            "blocks": [{"type": "icon_list", "icon": "shield-check", "items": [
                "Enhanced DBS checks and safer recruitment for all staff.",
                "A Designated Safeguarding Lead.",
                "Written policies on safeguarding, health and safety, complaints and data protection.",
                "Gas Safety Record (February 2026) and electrical safety report (EICR, 2026) in place.",
                "A licence agreement, move-in pack and house guide for each resident.",
            ]}],
        },
        {
            "type": "section",
            "title": "Clear boundaries",
            "blocks": [{"type": "p", "text": "We provide housing-related support only. We don't provide personal or intimate care, medical or nursing services, or therapy and clinical treatment, and we're not registered to deliver regulated care activities. Where a young person needs any of these, they should be arranged through appropriate regulated providers.", "style": "first"}],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Documents and monitoring visits",
            "blocks": [
                {"type": "p", "text": "Our Statement of Purpose and policies are available on request. Monitoring visits and quality checks are welcome: just get in touch to arrange one.", "style": "first"},
                {"type": "buttons", "items": [{"label": "Contact us", "href": "/contact", "variant": "outline", "size": "sm"}]},
            ],
        },
        {
            "type": "section",
            "title": "Ready to make a referral?",
            "blocks": [
                {"type": "p", "text": "Send us the details through our referral form, or call 07342 045712 to talk it through. We'll acknowledge your referral within 2 working hours.", "style": "first"},
                {"type": "buttons", "items": [
                    {"label": "Make a referral", "href": "/referrals", "variant": "primary", "size": "sm"},
                    {"label": "See our accommodation", "href": "/accommodation", "variant": "outline", "size": "sm"},
                ]},
            ],
        },
    ],
}
