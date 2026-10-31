"""About: https://www.urbancarers.co.uk/about  (source: src/routes/about.tsx)"""

PAGE = {
    "path": "/about",
    "title": "About Urban Carers | 18+ Supported Accommodation, London",
    "description": "Urban Carers Ltd provides supported accommodation and housing-related support for care leavers aged 18–25 in London: our mission, aims and governance.",
    "breadcrumb": "About",
    "hero": {
        "eyebrow": "About Urban Carers",
        "h1": "Helping care leavers build independent, settled lives.",
        "lead": "Urban Carers Ltd is a London-based provider of supported accommodation and housing-related support for young adults leaving care.",
    },
    "sections": [
        {
            "type": "section",
            "title": "Mission, aims & objectives",
            "blocks": [{"type": "cards", "cols": 3, "items": [
                {"title": "Our mission", "text": "To provide safe, stable homes and consistent support so every young person can move confidently into independent living."},
                {"title": "Our aims", "text": "Promote independence, build life and tenancy skills, and support education, training and employment."},
                {"title": "Our objectives", "text": "Successful planned move-on, sustained tenancies, and strong links with local community services."},
            ]}],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Governance & Statement of Purpose",
            "intro": "We operate under a published Statement of Purpose with clear policies on safeguarding, health and safety, complaints and data protection, reviewed regularly by our management team.",
            "blocks": [{"type": "pros_cons", "cols": [
                {"title": "What we provide", "kind": "check", "items": ["Supported accommodation", "Housing-related support & key-working", "Life skills and tenancy sustainment", "Signposting to specialist services"]},
                {"title": "What we do not provide", "kind": "x", "items": ["Personal or intimate care", "Medical or nursing services", "Clinical or therapeutic interventions", "Any regulated care activity"]},
            ]}],
        },
    ],
}
