"""Contact: https://www.urbancarers.co.uk/contact  (source: src/routes/contact.tsx + src/components/forms.tsx)"""

PAGE = {
    "path": "/contact",
    "title": "Contact Urban Carers | Supported Accommodation, London",
    "description": "Contact Urban Carers about 18+ supported accommodation for care leavers in London. Call 07342 045712 or email info@urbancarers.co.uk.",
    "breadcrumb": "Contact",
    "hero": {
        "eyebrow": "Contact",
        "h1": "Get in touch.",
        "lead": "General enquiries from young people, families and professionals are welcome.",
    },
    "sections": [
        {"type": "enquiry_form"},
    ],
}

# The enquiry form, field for field as in the source (forms.tsx EnquiryForm).
ENQUIRY_FORM = {
    "subject": "Website enquiry",
    "submit": "Send enquiry by email",
    "fields": [
        {"name": "Name", "label": "Name *", "id": "e-name", "required": True},
        {"name": "Email", "label": "Email *", "id": "e-email", "type": "email", "required": True},
        {"name": "Message", "label": "Message *", "id": "e-message", "textarea": True, "rows": 5, "required": True},
    ],
    "privacy_note": 'We\'ll only use your details to reply to you. Read our <a href="/privacy" class="link-plain">privacy notice</a>.',
}
