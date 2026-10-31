"""Accommodation page: https://www.urbancarers.co.uk/accommodation  (source: src/routes/accommodation.tsx)"""

SUPPORT = [
    ["Independent living skills", "The everyday skills needed to run a home and live independently."],
    ["Budgeting and money", "Managing money, bills and benefits."],
    ["Education, employment and training", "College and ESOL enrolment, CVs, job searches, interview preparation and attendance."],
    ["Health and wellbeing", "Managing health appointments, accessing services and emotional wellbeing."],
    ["Tenancy readiness and move-on", "Understanding tenancy responsibilities and planning the next home."],
    ["Pathway plan support", "Working closely with social workers and personal advisers."],
    ["Support for asylum-seeking young people", "Orientation, cultural adjustment, ESOL access and help navigating UK systems."],
    ["Community", "Links to local services and to faith and cultural communities."],
]

FAQS = [
    ["Where is the house?", "In South London. We share the full address with referring professionals."],
    ["Do you accept 16 and 17 year olds?", "No. We provide non-regulated supported accommodation for young adults aged 18–25 only."],
    ["Is this semi-independent accommodation?", "Yes. It's semi-independent living for 18–25 year olds: each young person has their own room and builds independent living skills, with at least 5 hours of key-work support a week and management on call around the clock."],
    ["Which councils can refer?", "Any placing local authority, in London or beyond."],
    ["How quickly do you respond to referrals?", "We acknowledge referrals within 2 working hours and aim to make a placement decision within 24 hours of receiving full referral information."],
]

PAGE = {
    "path": "/accommodation",
    "title": "18+ Supported Accommodation in South London | Urban Carers",
    "description": "18+ supported, semi-independent accommodation in South London: furnished double rooms and weekly key-work support for care leavers aged 18–25.",
    "breadcrumb": "Accommodation",
    "faq": FAQS,
    "hero": {
        "eyebrow": "Supported accommodation",
        "h1": "18+ supported accommodation in South London",
        "lead": "A three-bedroom shared house in South London for care leavers and unaccompanied asylum-seeking young people (UASC) aged 18–25. Each young person has a large, furnished double room of their own and at least 5 hours of structured key-work support every week, with management on call around the clock.",
    },
    "sections": [
        {
            "type": "section",
            "badge": "2 rooms available now",
            "title": "Our home in South London",
            "intro": "The house is set up for three young adults sharing: one young person per room, two bathrooms, a study for college work and calls, and shared space downstairs opening onto a private rear garden, with good transport links across London.",
            "blocks": [
                {
                    "type": "rooms",
                    "items": [
                        {"name": "Bedroom 2", "kind": "Large double, first floor", "size": "Approx. 5.20 × 3.40 m (17.7 m²)", "status": "Available now"},
                        {"name": "Bedroom 3", "kind": "Large double, first floor", "size": "Approx. 4.00 × 3.40 m (13.6 m²)", "status": "Available now"},
                    ],
                    "note": "Room sizes are approximate, taken from the floor plan.",
                },
                {"type": "p", "text": "Each bedroom has a double bed, a double wardrobe with a full-length mirror, a bedside table, and a desk and chair.", "style": "body"},
                {"type": "p", "text": "Shared spaces: a lounge, a kitchen/dining room opening onto the private rear garden, a first-floor study, a ground-floor shower room and a first-floor bathroom. High-speed Wi-Fi and a washing machine, and furnished throughout."},
                {"type": "buttons", "items": [
                    {"label": "Make a referral", "href": "/referrals", "variant": "primary", "size": "sm"},
                    {"label": "Ask about this house", "href": "/contact", "variant": "outline", "size": "sm"},
                ]},
            ],
        },
        {
            "type": "section",
            "title": "What's included",
            "blocks": [{"type": "cards", "cols": 4, "items": [
                {"icon": "bed-double", "title": "Private bedrooms", "text": "A large, furnished, lockable double room of your own. One young person per room."},
                {"icon": "wifi", "title": "High-speed Wi-Fi", "text": "Reliable internet for study, work and staying connected."},
                {"icon": "cooking-pot", "title": "Shared kitchen & living", "text": "A kitchen/dining room, a lounge and a private rear garden."},
                {"icon": "washing-machine", "title": "Laundry facilities", "text": "A washing machine in the house."},
            ]}],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Structured key-working support",
            "intro": "At least 5 hours of structured support per resident each week, including weekly key-work sessions, with management on call around the clock. Extra hours or night support can be arranged.",
            "blocks": [{"type": "cards", "cols": 4, "items": [{"title": t, "text": d} for t, d in SUPPORT]}],
        },
        {
            "type": "section",
            "title": "Who the house suits",
            "blocks": [
                {"type": "pros_cons", "cols": [
                    {"title": "The house suits", "kind": "check", "items": [
                        "Care leavers and unaccompanied asylum-seeking young people aged 18–25",
                        "Young adults with low to medium support needs",
                        "Young people ready to live semi-independently with regular support",
                        "Any placing local authority, in London or beyond",
                    ]},
                    {"title": "Not suitable for", "kind": "x", "items": [
                        "Intensive or clinical mental health support, or personal care",
                        "Constant supervision",
                        "High-risk behaviour that can't be managed safely in a shared home",
                    ]},
                ]},
                {"type": "p", "text": "We match every placement carefully with the current household.", "style": "note"},
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Making a referral",
            "intro": "Use our referral page or call 07342 045712. Please include a risk assessment, the pathway or support plan, key contacts, any restrictions and, for asylum-seeking young people, their immigration status.",
            "blocks": [
                {"type": "steps", "cols": 3, "items": [
                    "Acknowledged within 2 working hours",
                    "Placement decision within 24 hours of full referral information. Emergencies are prioritised.",
                    "Move-in planned with you",
                ]},
                {"type": "buttons", "items": [{"label": "Make a referral", "href": "/referrals", "variant": "primary", "size": "sm"}]},
            ],
        },
        {
            "type": "section",
            "title": "Safety and standards",
            "blocks": [{"type": "icon_list", "icon": "shield-check", "items": [
                "Non-regulated 18+ supported accommodation. We don't provide personal care.",
                "Enhanced DBS checks and safer recruitment for all staff.",
                "A Designated Safeguarding Lead.",
                "Gas Safety Record (February 2026) and electrical safety report (EICR, 2026) in place.",
                "A licence agreement, move-in pack and house guide for each resident.",
                "Monitoring visits and quality checks are welcome. Our Statement of Purpose and policies are available on request.",
            ]}],
        },
        {
            "type": "section",
            "title": "Clear boundaries",
            "intro": "We provide housing-related support only. The following are not part of our service and should be arranged through appropriate regulated providers where needed.",
            "blocks": [{"type": "boundaries", "items": ["No personal or intimate care", "No medical or nursing services", "No therapy or clinical treatment"]}],
        },
        {
            "type": "section",
            "title": "Questions from professionals",
            "blocks": [{"type": "faq", "items": FAQS}],
        },
    ],
}
