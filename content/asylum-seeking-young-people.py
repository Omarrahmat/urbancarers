"""Asylum-seeking young people: https://www.urbancarers.co.uk/asylum-seeking-young-people  (source: src/routes/asylum-seeking-young-people.tsx)"""

SUPPORT = [
    ["Orientation", "Getting to know the house, the local area, public transport and how everyday things work, from shopping and bills to registering with services."],
    ["Cultural adjustment", "Time and space to adjust to a new culture and way of life, at the young person's own pace, with a key worker they can talk to."],
    ["ESOL and education", "Help finding and enrolling on ESOL (English for Speakers of Other Languages) courses and college, and support to keep attending."],
    ["Navigating UK systems", "Help understanding letters, forms and appointments, and keeping track of what needs to happen and when."],
    ["Faith and cultural communities", "Links to faith and cultural communities and to local services, so young people can build connections beyond the house."],
    ["Independent living skills", "Cooking, budgeting, managing money and benefits, and looking after a home: the everyday skills needed for the next step."],
]

PAGE = {
    "path": "/asylum-seeking-young-people",
    "title": "Supported Accommodation for Asylum-Seeking Young People 18–25 | Urban Carers",
    "description": "18+ supported accommodation in South London for unaccompanied asylum-seeking young people (UASC) and former UASC aged 18–25, with key-work support, ESOL access and help settling into life in the UK.",
    "breadcrumb": "Asylum-seeking young people",
    "hero": {
        "eyebrow": "Asylum-seeking young people",
        "h1": "Supported accommodation for unaccompanied asylum-seeking young people aged 18–25",
        "lead": "Urban Carers provides 18+ supported accommodation in South London for young people who came to the UK as unaccompanied asylum-seeking children (UASC), and for former UASC who are now care leavers. Each young person has a furnished double room of their own in a shared house, at least 5 hours of structured key-work support every week, and management on call around the clock.",
    },
    "sections": [
        {
            "type": "section",
            "title": "A settled home after a long journey",
            "blocks": [
                {"type": "p", "text": "Many young people who arrived in the UK alone have already lived through a great deal of change: a new country, a new language and new systems, often while waiting for decisions about their future. Turning 18 brings more change again. A stable home, with people who understand that journey, can make the next step far easier.", "style": "first"},
                {"type": "p", "text": "UASC and former UASC aged 18–25 are welcome at Urban Carers, and we have experience supporting them. Our support is practical and patient. We help each young person settle in, understand how things work in the UK, keep up with education and appointments, and build the skills they'll need to live independently."},
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Support for asylum-seeking young people",
            "intro": "Alongside the key work every resident receives, we offer support shaped around the needs of young people who are new to the UK.",
            "blocks": [{"type": "cards", "cols": 3, "items": [{"title": t, "text": d} for t, d in SUPPORT]}],
        },
        {
            "type": "section",
            "title": "Key work and the pathway plan",
            "blocks": [
                {"type": "p", "text": "Every young person has at least 5 hours of structured key-work support a week, including weekly key-work sessions, with management on call around the clock. Extra hours or night support can be arranged. Key work is planned around the goals in the young person's pathway plan, and we work alongside their social worker or personal adviser, not in place of them. The placing local authority receives a written weekly key-work report, and we'll be in touch promptly if anything changes.", "style": "first"},
                {"type": "p", "text": "We provide housing-related support. We're not immigration advisers, so legal and immigration advice should come from the young person's solicitor or a qualified adviser. We can help the young person keep track of their appointments and stay in touch with the professionals supporting them."},
            ],
        },
        {
            "type": "section",
            "muted": True,
            "title": "Our home in South London",
            "blocks": [
                {"type": "p", "text": "Our current house is a three-bedroom shared home in South London for young men aged 18–25. Each young person has a large, furnished, lockable double room. The house has two bathrooms, a study for college work and calls, a lounge, a kitchen/dining room opening onto a private rear garden, high-speed Wi-Fi and a washing machine, with good transport links across London.", "style": "first"},
                {"type": "p", "text": "We match every placement carefully with the young people already living in the house, so that the home works for everyone."},
                {"type": "buttons", "items": [{"label": "See our accommodation", "href": "/accommodation", "variant": "outline", "size": "sm"}]},
            ],
        },
        {
            "type": "section",
            "title": "Referring an asylum-seeking young person",
            "blocks": [
                {"type": "p", "text": "We work with leaving care teams, asylum-seeking young people's teams and placements teams from any local authority, in London or beyond. We accept young adults aged 18 to 25 only, and we don't accept 16 and 17 year olds. When you refer, please include the young person's immigration status along with the usual referral information. Our page for professionals explains everything we ask for.", "style": "first"},
                {"type": "p", "text": "We acknowledge referrals within 2 working hours and aim to make a placement decision within 24 hours of receiving full referral information. Emergencies are prioritised: please call 07342 045712 as well as sending the form."},
                {"type": "buttons", "items": [
                    {"label": "Make a referral", "href": "/referrals", "variant": "primary", "size": "sm"},
                    {"label": "For professionals", "href": "/for-professionals", "variant": "outline", "size": "sm"},
                ]},
            ],
        },
    ],
}
