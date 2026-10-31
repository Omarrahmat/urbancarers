"""Referrals: https://www.urbancarers.co.uk/referrals  (source: src/routes/referrals.tsx + src/components/forms.tsx)"""

PAGE = {
    "path": "/referrals",
    "title": "Make a Referral: 18+ Supported Accommodation | Urban Carers",
    "description": "Referral form for local authorities and partner agencies placing care leavers aged 18–25 in supported accommodation in South London.",
    "breadcrumb": "Referrals",
    "hero": {
        "eyebrow": "Referrals",
        "h1": "Local Authority & Partner Agency Referral",
        "lead": "Complete the form below. We acknowledge referrals within 2 working hours and aim to make a placement decision within 24 hours of receiving full referral information. For emergency placements, please also call us.",
    },
    "sections": [
        {"type": "referral_form", "aside_title": "Referral team"},
    ],
}

# The referral form, field for field as in the source (forms.tsx ReferralForm).
REFERRAL_FORM = {
    "subject": "Website referral",
    "submit": "Send referral by email",
    "fields": [
        {"name": "Local authority / agency", "label": "Local authority / agency *", "id": "organisation", "required": True},
        {"name": "Referrer name", "label": "Referrer name *", "id": "name", "required": True},
        {"name": "Job role", "label": "Job role", "id": "role", "placeholder": "e.g. Personal Adviser"},
        {"name": "Email", "label": "Email *", "id": "email", "type": "email", "required": True},
        {"name": "Phone", "label": "Phone *", "id": "phone", "type": "tel", "required": True},
        {"name": "Young person's age", "label": "Young person's age", "id": "age", "inputmode": "numeric"},
        {"name": "Referral type", "label": "Referral type *", "id": "referralType", "required": True, "select": [
            "Care leaver (18–25)", "Unaccompanied asylum-seeking young adult (18–25)", "Planned move-on / step-down", "Other",
        ]},
        {"name": "Placement urgency", "label": "Placement urgency *", "id": "urgency", "required": True, "select": [
            "Emergency (within 48 hours)", "Urgent (within 1–2 weeks)", "Planned (2+ weeks)",
        ]},
        {"name": "Referral notes", "label": "Referral notes", "id": "notes", "textarea": True, "rows": 5, "wide": True,
         "placeholder": "Support needs, risks, preferred area and move-in date. Please don't include the young person's name or identifying details."},
    ],
    "privacy_note": 'Please don\'t include the young person\'s name or other identifying details here. We\'ll ask for referral documents by a secure route. Read our <a href="/privacy" class="link-plain">privacy notice</a>.',
}
