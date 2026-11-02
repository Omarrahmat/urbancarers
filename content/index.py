"""Home page: https://www.urbancarers.co.uk/  (source: src/routes/index.tsx)"""

FAQS = [
    ["What is supported accommodation for care leavers?", "Supported accommodation is housing with support for care leavers aged 18–25 only. Residents have their own room in shared housing and receive housing-related support such as key-working, budgeting and tenancy skills."],
    ["Is supported accommodation the same as semi-independent accommodation?", "The two terms are often used for the same kind of home. What we provide is 18+ supported accommodation for young men aged 18–25 only: each young person has their own room in a shared house and builds the skills to live independently, with at least 5 hours of key-work support a week."],
    ["Which areas of London do you cover?", "Our house is in South London. We accept referrals from London boroughs and from local authorities outside London placing young people in the capital."],
    ["Do you accept UASC referrals?", "Yes. We support unaccompanied asylum-seeking young adults aged 18 to 25 who are ready to live in supported accommodation."],
    ["How quickly can a placement start?", "We acknowledge referrals within 2 working hours and aim to make a placement decision within 24 hours of receiving full referral information. We can consider emergency placements subject to availability and assessment."],
    ["Is Urban Carers a regulated care provider?", "No. We provide non-regulated supported accommodation and housing-related support. We do not provide personal care, medical or nursing services, or therapy."],
]

PAGE = {
    "path": "/",
    "title": "Supported Accommodation for Care Leavers 18–25 | Urban Carers",
    "description": "18+ supported accommodation in South London for care leavers and asylum-seeking young people aged 18–25. Referrals acknowledged within 2 working hours.",
    "breadcrumb": "Home",
    "website_jsonld": True,
    "faq": FAQS,
    "sections": [
        {
            "type": "home_hero",
            "eyebrow": "Supported accommodation · London",
            "h1": "Supported accommodation in London for care leavers aged 18–25",
            "lead": "Safe, stable 18+ supported accommodation with structured key-work support for care leavers and asylum-seeking young people aged 18–25. Our home is in South London, and we take referrals from councils across London and beyond.",
            "buttons": [
                {"label": "Make a Referral", "href": "/referrals", "variant": "primary", "icon": "arrow-right"},
                {"label": "Our accommodation", "href": "/accommodation", "variant": "outline"},
            ],
            "stat": {"big": "2 working hours", "small": "To acknowledge local authority and partner referrals"},
        },
        {
            "type": "strip",
            "items": [
                ["South London", "A shared house in South London, with good transport links across the capital."],
                ["Local authority partners", "Working alongside leaving care teams and social workers."],
                ["Structured, non-regulated support", "Clear boundaries, robust governance."],
            ],
        },
        {
            "type": "section",
            "title": "How we support young adults",
            "intro": "Every young person receives a structured, person-centred support plan built around their goals.",
            "blocks": [
                {
                    "type": "feature_cards",
                    "items": [
                        {"n": "01", "icon": "users", "title": "Key-working sessions", "text": "Regular one-to-one sessions with a dedicated key worker to set goals and track progress.", "tag": "Weekly 1:1"},
                        {"n": "02", "icon": "book-open", "title": "Life & tenancy skills", "text": "Budgeting, cooking, bills and the skills needed to hold a tenancy.", "tag": "Move-on ready"},
                        {"n": "03", "icon": "briefcase", "title": "Education & employment", "text": "Support into college, training, volunteering and work.", "tag": "EET focused"},
                        {"n": "04", "icon": "house", "title": "Safe shared housing", "text": "A well-maintained shared house in South London, with large private bedrooms.", "tag": "South London"},
                    ],
                }
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Supported accommodation across London for care leavers 18–25",
            "intro": "Urban Carers provides 18+ supported accommodation for local authority leaving care teams, personal advisers and social workers across London boroughs. Our placements combine safe shared housing with structured housing-related support, helping young adults prepare for and sustain their own tenancy.",
            "blocks": [
                {
                    "type": "cards",
                    "cols": 3,
                    "items": [
                        {"title": "For local authority commissioners", "text": "Clear Statement of Purpose, transparent service boundaries and regular progress reporting on pathway plan goals."},
                        {"title": "For social workers & PAs", "text": "Fast referral responses, emergency and planned placements, and a named key worker for every young person."},
                        {"title": "For young adults", "text": "Your own room in a safe London home, with support to manage money, study, work and move on."},
                    ],
                }
            ],
        },
        {
            "type": "section",
            "title": "Frequently asked questions",
            "blocks": [{"type": "faq", "items": FAQS}],
        },
        {
            "type": "cta",
            "title": "Referring a young person?",
            "text": "We acknowledge local authority and partner referrals within 2 working hours.",
            "button": {"label": "Start a referral", "href": "/referrals", "variant": "primary"},
        },
    ],
}
