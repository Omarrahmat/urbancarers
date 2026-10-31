"""Privacy notice: https://www.urbancarers.co.uk/privacy  (source: src/routes/privacy.tsx)"""

MAIL = '<a href="mailto:omar@urbancarers.co.uk" class="link">omar@urbancarers.co.uk</a>'

ROWS = [
    ["Assess referrals, provide accommodation and support, and plan and review support with the young person and their local authority", "Our legitimate interests in providing a safe, effective service commissioned by local authorities, and our licence agreement with each resident. For health and other special category information: providing social care and support, and safeguarding individuals at risk"],
    ["Keep people safe, including sharing information when someone is at risk of harm", "Protecting someone's vital interests, safeguarding individuals at risk, and our legitimate interests"],
    ["Meet our legal duties, such as health and safety, tax and accounting, and lawful requests from public authorities", "Legal obligation"],
    ["Work with councils and other professionals, answer enquiries and referrals, and tell organisations about our services", "Our legitimate interests. You can ask us to stop contacting you at any time"],
    ["Recruit staff safely, including DBS checks", "Taking steps to enter a contract and legal obligation. For criminal record information: the employment and safeguarding conditions in the Data Protection Act 2018"],
    ["Deal with complaints and legal claims", "Our legitimate interests, and establishing, exercising or defending legal claims"],
]

PAGE = {
    "path": "/privacy",
    "title": "Privacy notice | Urban Carers",
    "description": "How Urban Carers Ltd collects, uses and protects personal information.",
    "breadcrumb": "Privacy notice",
    "hero": {
        "eyebrow": "Privacy",
        "h1": "Privacy notice",
        "lead": "How Urban Carers Ltd collects, uses and protects personal information. Last updated 23 October 2026.",
    },
    "sections": [
        {
            "type": "article",
            "blocks": [
                {"type": "callout", "title": "In short", "items": [
                    "We're Urban Carers Ltd. We provide supported accommodation in London for care leavers aged 18–25.",
                    "We use personal information to assess referrals, keep residents safe, provide support, and work with councils and other professionals.",
                    "We share information only when we need to: mainly with the young person's local authority, and with health services, the police or emergency services if someone is at risk.",
                    "We keep information secure and only for as long as we need it.",
                    "You have rights over your information, including the right to see it. Email " + MAIL + ".",
                ]},

                {"type": "h2", "text": "1. Who we are"},
                {"type": "p", "text": 'Urban Carers Ltd ("we", "us") decides how and why the personal information in this notice is used. That makes us the "controller" under UK data protection law.'},
                {"type": "ul", "items": [
                    "Company number 15419139, registered in England and Wales",
                    "Registered office: 3rd Floor, 45 Albemarle Street, Mayfair, London W1S 4JL",
                    "Responsible for data protection: Omar Rahmat, Managing Director",
                    "Email " + MAIL + " · Phone 07342 045712",
                ]},

                {"type": "h2", "text": "2. Who this notice covers"},
                {"type": "ul", "items": [
                    "young people referred to us, and residents of our accommodation",
                    "social workers, personal advisers and other professionals we work with, including council staff who place young people with us or whom we contact about our services",
                    "people who contact us or use our website, including its referral and contact forms",
                    "people who apply to work with us",
                ]},

                {"type": "h2", "text": "3. The information we collect"},
                {"type": "h3", "text": "About young people referred to us or living with us"},
                {"type": "ul", "items": [
                    "name, date of birth, contact details and the local authority responsible for your care",
                    "information in referral documents, such as your pathway plan or support plan, risk assessments and key contacts",
                    "information about your health and wellbeing, including mental health, where it's relevant to your support",
                    "for unaccompanied asylum-seeking young people, your immigration status and related details",
                    "information about offending or risks to you or others, where it's needed to keep people safe",
                    "records of the support we give, including key-work notes, support plans and reviews, incidents and safeguarding concerns",
                    "information needed to manage your licence agreement and your stay, such as move-in and move-out dates",
                ]},
                {"type": "p", "text": 'Some of this is "special category" information (for example about health, religion or ethnicity) or information about criminal offences. The law protects it more strongly, and we only collect it where we need to.'},
                {"type": "h3", "text": "About professionals and other contacts"},
                {"type": "ul", "items": [
                    "your name, job title, organisation, and work email address and phone number",
                    "our emails with you, and notes of calls and meetings",
                ]},
                {"type": "p", "text": "We get these details from you, from your colleagues, from your organisation's public website, or from other professionals and organisations in our sector who share work contact details with us."},
                {"type": "h3", "text": "From our website"},
                {"type": "ul", "items": [
                    "what you send us using our referral or contact forms, such as your name, organisation, role, email, phone number and details about the referral. The forms send this to us by email",
                    "please don't put a young person's name or other identifying details in a website form. If we can help, we'll ask for referral documents by a secure route",
                    "our website host may record technical information, such as your IP address and browser type, to keep the site working and secure",
                ]},
                {"type": "h3", "text": "About job applicants"},
                {"type": "ul", "items": ["your application, CV and references, right-to-work documents and, for roles that need one, an enhanced DBS check"]},

                {"type": "h2", "text": "4. Where we get information"},
                {"type": "p", "text": "Most information about young people comes from the local authority that refers or places them, and from the young person. We may also receive information from health services, education providers, the police or other agencies involved in their care and safety."},

                {"type": "h2", "text": "5. Why we use it, and our legal basis"},
                {"type": "p", "text": "UK data protection law says we must have a valid reason, called a lawful basis, for using personal information."},
                {"type": "table", "head": ["What we do", "Our lawful basis"], "rows": ROWS},
                {"type": "p", "text": "For information governance teams: we rely on UK GDPR Articles 6(1)(b), (c), (d) and (f); Article 9(2)(c), (f), (g) and (h); and the Data Protection Act 2018, Schedule 1, paragraphs 1, 2 and 18."},
                {"type": "p", "text": "We don't make decisions about people based only on automated processing. A person makes every decision about referrals and placements."},

                {"type": "h2", "text": "6. Who we share it with"},
                {"type": "ul", "items": [
                    "the local authority responsible for the young person, such as their social worker or personal adviser, and other professionals involved in their care",
                    "health services, the police, emergency services and safeguarding partners, when it's needed to protect someone or the law requires it",
                    "companies that provide services to us under contract, such as our IT, email, website and document storage providers, and professional advisers such as accountants, lawyers and insurers",
                    "an AI assistant (Claude, provided by Anthropic) that helps us manage email and records. It works only on our instructions, and a person makes every decision about referrals and placements",
                    "anyone else where the law requires it, or with your consent",
                ]},
                {"type": "p", "text": "We never sell personal information."},

                {"type": "h2", "text": "7. Information sent outside the UK"},
                {"type": "p", "text": "Some of our service providers, including our email and AI providers, may store or process information outside the UK, for example in the USA. When they do, we make sure the safeguards UK law requires are in place, such as the UK–US data bridge or the ICO's international data transfer agreement or addendum."},

                {"type": "h2", "text": "8. How long we keep it"},
                {"type": "ul", "items": [
                    "residents' records: 6 years after the placement ends, or longer if needed for safeguarding or legal reasons",
                    "referrals that don't lead to a placement: up to 12 months",
                    "emails and notes with professionals and enquirers: up to 2 years after our last contact",
                    "financial records: 6 years after the end of the financial year they relate to",
                    "applications from unsuccessful job applicants: 6 months after the decision",
                ]},
                {"type": "p", "text": "After that, we delete or securely destroy the information."},

                {"type": "h2", "text": "9. Keeping information secure"},
                {"type": "p", "text": "We use secure, password-protected systems and limit access to the people who need it. Our staff are trained in data protection and confidentiality. If a data breach happens, we act quickly and report it to the Information Commissioner's Office (ICO) where the law requires."},

                {"type": "h2", "text": "10. Your rights"},
                {"type": "p", "text": "You can ask us to:"},
                {"type": "ul", "items": [
                    "give you a copy of your information",
                    "correct information that's wrong or incomplete",
                    "delete your information, or limit how we use it, in some circumstances",
                    "stop using your information, including to contact you about our services",
                    "send information you gave us to another organisation, in some circumstances",
                ]},
                {"type": "p", "text": "Where we rely on your consent, you can withdraw it at any time."},
                {"type": "p", "text": "To make a request, email " + MAIL + " or call 07342 045712. We'll normally respond within one month. Young people can also ask their social worker or personal adviser to help them make a request."},

                {"type": "h2", "text": "11. Complaints"},
                {"type": "p", "text": "If you're unhappy with how we've handled your information, please tell us first by emailing " + MAIL + ". We'll acknowledge your complaint within 30 days and let you know the outcome without undue delay."},
                {"type": "p", "text": 'You can also complain to the Information Commissioner\'s Office at <a href="https://ico.org.uk/make-a-complaint" target="_blank" rel="noopener noreferrer" class="link">ico.org.uk/make-a-complaint</a> or on 0303 123 1113.'},

                {"type": "h2", "text": "12. Changes to this notice"},
                {"type": "p", "text": "We review this notice regularly and update it when the way we use information changes. The latest version is always on our website."},
            ],
        },
    ],
}
