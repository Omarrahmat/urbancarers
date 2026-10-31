"""Who we support: https://www.urbancarers.co.uk/who-we-support  (source: src/routes/who-we-support.tsx)"""

PAGE = {
    "path": "/who-we-support",
    "title": "Care Leavers & Asylum-Seeking Young People | Urban Carers",
    "description": "Who we support: care leavers aged 18–25 and unaccompanied asylum-seeking young people aged 18–25, with our referral and suitability criteria.",
    "breadcrumb": "Who we support",
    "hero": {
        "eyebrow": "Who we support",
        "h1": "Young adults ready for their next step.",
        "lead": "We work with local authorities to support young people transitioning to independent living in London.",
    },
    "sections": [
        {
            "type": "section",
            "title": "Referral profiles",
            "blocks": [
                {"type": "cards", "cols": 3, "items": [
                    {"title": "Care-experienced adults 18–25", "text": "Care leavers needing a stable home and support to build independence."},
                    {"title": "UASC young adults 18–25", "text": "Unaccompanied asylum-seeking young adults settling into life in London."},
                    {"title": "Planned move-on", "text": "Young people stepping down from more intensive placements."},
                ]},
                {"type": "p", "text": 'Read more about <a href="/asylum-seeking-young-people" class="link">our support for unaccompanied asylum-seeking young people aged 18–25</a>.', "style": "note"},
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Suitability criteria",
            "intro": "Every referral is assessed individually. These criteria guide our decisions.",
            "blocks": [
                {"type": "pros_cons", "cols": [
                    {"title": "Inclusion", "kind": "check", "items": [
                        "Aged 18–25 and care-experienced, or UASC aged 18–25",
                        "Assessed low to medium support needs",
                        "Motivated to develop independent living skills",
                        "Able to live safely in shared accommodation",
                        "Willing to engage with key-working sessions",
                    ]},
                    {"title": "Exclusion", "kind": "x", "items": [
                        "Requires personal, intimate or nursing care",
                        "Needs 24-hour supervision or regulated care",
                        "High risk to self or others that cannot be safely managed",
                        "Active needs requiring clinical or therapeutic placement",
                        "Recent arson or serious violent offences without risk plan",
                    ]},
                ]},
                {"type": "buttons", "items": [{"label": "Make a Referral", "href": "/referrals", "variant": "primary"}]},
            ],
        },
    ],
}
