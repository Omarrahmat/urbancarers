#!/usr/bin/env python3
"""Static site builder for www.urbancarers.co.uk.

Usage:  python3 build.py            (Python 3 standard library only)

Reads one content module per page from content/ (content/<slug>.py, each
defining PAGE, see README.md), renders every page through the shared layout
below and writes, at the repository root:

    index.html, <slug>.html ...   one file per page (GitHub Pages serves
                                  /accommodation from accommodation.html)
    404.html, sitemap.xml, robots.txt, .nojekyll

Internal links are written relative to each page so the site works both at
https://www.urbancarers.co.uk/ and at the GitHub Pages preview sub-path.
Canonical, Open Graph, sitemap and JSON-LD URLs are always absolute.
"""
from __future__ import annotations

import datetime as _dt
import html
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(ROOT, "content")
ICON_DIR = os.path.join(ROOT, "assets", "icons")

SITE_URL = "https://www.urbancarers.co.uk"
SITE_NAME = "Urban Carers"
LANG = "en-GB"
TODAY = _dt.date.today().isoformat()
YEAR = _dt.date.today().year

# Order of the sitemap and of the build (same as the live sitemap.xml).
PAGE_ORDER = [
    "index", "about", "accommodation", "who-we-support", "for-professionals",
    "asylum-seeking-young-people", "referrals", "contact", "privacy",
]

CONTACT = {
    "phone": "07342 045712",
    "tel": "+447342045712",
    "email": "info@urbancarers.co.uk",
    "hours": "Monday – Friday: 9:00am – 5:00pm",
    "address": ["3rd Floor, 45 Albemarle Street", "Mayfair, London", "W1S 4JL"],
}

NAV = [
    ("/about", "About"),
    ("/accommodation", "Accommodation"),
    ("/who-we-support", "Who we support"),
    ("/for-professionals", "For professionals"),
    ("/contact", "Contact"),
]

# Logo: if assets/logo.png exists in the repository it is used (self-hosted);
# until then the page references the file the live site serves today.
LOGO_LOCAL = "assets/logo.png"
LOGO_REMOTE = SITE_URL + "/__l5e/assets-v1/17e47ad8-12ed-4505-8971-14a2e98ddae2/logo.png"
FAVICON_LOCAL = "assets/favicon.png"

ORGANIZATION = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Urban Carers Ltd",
    "logo": None,  # filled in build()
    "description": "Supported accommodation and housing-related support for care leavers aged 18–25 in London.",
    "url": SITE_URL,
    "telephone": "+44 7342 045712",
    "email": "info@urbancarers.co.uk",
    "address": {"@type": "PostalAddress", "streetAddress": "3rd Floor, 45 Albemarle Street", "addressLocality": "London", "postalCode": "W1S 4JL", "addressCountry": "GB"},
    "areaServed": [{"@type": "City", "name": "London"}, {"@type": "AdministrativeArea", "name": "South East England"}],
}

FORM_FALLBACK = (
    'If the button does nothing on your computer, email us directly at '
    '<a href="mailto:{email}">{email}</a> or call <a href="tel:{tel}">{phone}</a>.'
)

# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def esc(s: str) -> str:
    return html.escape(s, quote=True)


def load_icons() -> dict[str, str]:
    icons = {}
    if not os.path.isdir(ICON_DIR):
        return icons
    for fn in os.listdir(ICON_DIR):
        if not fn.endswith(".svg"):
            continue
        with open(os.path.join(ICON_DIR, fn), encoding="utf-8") as f:
            svg = f.read()
        svg = re.sub(r"\s+", " ", svg).replace("> <", "><").strip()
        svg = svg.replace("<svg ", '<svg class="ic" aria-hidden="true" focusable="false" ', 1)
        icons[fn[:-4]] = svg
    return icons


ICONS = load_icons()


def icon(name: str) -> str:
    return ICONS.get(name, "")


def load_pages() -> list[dict]:
    pages = []
    for slug in PAGE_ORDER:
        path = os.path.join(CONTENT_DIR, slug + ".py")
        spec = importlib.util.spec_from_file_location("content_" + slug.replace("-", "_"), path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        page = dict(mod.PAGE)
        page["slug"] = slug
        page["file"] = public_path_to_file(page["path"])
        os.makedirs(os.path.dirname(os.path.join(ROOT, page["file"])) or ROOT, exist_ok=True)
        page["module"] = mod
        pages.append(page)
    return pages


def public_path_to_file(path: str) -> str:
    """'/about' -> 'about.html', '/' -> 'index.html', '/guides/x' -> 'guides/x.html'."""
    if path in ("/", ""):
        return "index.html"
    return path.strip("/") + ".html"


def relative_link(target: str, from_file: str, base: str | None = None) -> str:
    """Site-absolute path ('/about', '/styles.css') -> link relative to from_file.

    Pages are addressed without the .html extension (GitHub Pages serves
    about.html at /about). Files with an extension are linked as they are.
    """
    if base is not None:  # absolute links (used by 404.html)
        return base + target
    from_dir = os.path.dirname(from_file)
    tgt = target.strip("/")
    if tgt == "":
        rel = os.path.relpath(".", from_dir or ".")
        return "./" if rel == "." else rel + "/"
    rel = os.path.relpath(tgt, from_dir or ".")
    return rel.replace(os.sep, "/")


LINK_RE = re.compile(r'\b(href|src)="(/[^"/][^"]*|/)"')


def relativise(html_text: str, from_file: str, base: str | None = None) -> str:
    def sub(m):
        return '%s="%s"' % (m.group(1), relative_link(m.group(2), from_file, base))
    return LINK_RE.sub(sub, html_text)


def jsonld(obj) -> str:
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


# ----------------------------------------------------------------------------
# shared layout
# ----------------------------------------------------------------------------

def render_header(current_path: str, logo_src: str) -> str:
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current_path else ""
        links.append('<a href="%s"%s>%s</a>' % (href, cur, esc(label)))
    mobile = "".join('<a href="%s">%s</a>' % (h, esc(l)) for h, l in NAV)
    return f"""<header class="site-header">
  <div class="topbar">
    <div class="container topbar-inner">
      <a href="tel:{CONTACT['tel']}">{icon('phone')}{esc(CONTACT['phone'])}</a>
      <a href="mailto:{CONTACT['email']}">{icon('mail')}{esc(CONTACT['email'])}</a>
    </div>
  </div>
  <div class="container navbar">
    <a href="/" class="brand" aria-label="Urban Carers home"><img src="{logo_src}" alt="Urban Carers Ltd" width="1334" height="334"></a>
    <nav class="nav" aria-label="Main">{''.join(links)}</nav>
    <div class="actions">
      <a href="tel:{CONTACT['tel']}" class="btn btn-outline btn-sm">Call us</a>
      <a href="/referrals" class="btn btn-sm">Make a Referral</a>
    </div>
    <details class="menu">
      <summary aria-label="Toggle menu"><span class="menu-open">{icon('menu')}</span><span class="menu-close">{icon('x')}</span></summary>
      <div class="menu-panel container">
        {mobile}
        <a href="tel:{CONTACT['tel']}" class="menu-call">Call {esc(CONTACT['phone'])}</a>
        <a href="/referrals" class="btn">Make a Referral</a>
      </div>
    </details>
  </div>
</header>"""


def render_footer(logo_src: str) -> str:
    addr = "".join("<p>%s</p>" % esc(l) for l in CONTACT["address"])
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="{logo_src.replace('logo.png', 'logo-white.png')}" alt="Urban Carers Ltd" width="1334" height="334">
      <p>Safe, stable supported accommodation and housing-related support for care leavers aged 18–25 across London.</p>
    </div>
    <div class="footer-col">
      <p class="footer-title">Head Office</p>
      {addr}
    </div>
    <div class="footer-col">
      <p class="footer-title">Contact</p>
      <p><a href="tel:{CONTACT['tel']}">{esc(CONTACT['phone'])}</a></p>
      <p><a href="mailto:{CONTACT['email']}">{esc(CONTACT['email'])}</a></p>
      <p>{esc(CONTACT['hours'])}</p>
    </div>
  </div>
  <div class="footer-legal">
    <div class="container">
      <p><strong>Disclaimer:</strong> Urban Carers Ltd provides non-regulated supported accommodation and housing-related support. We do not provide personal or intimate care, medical or nursing services, or therapeutic services, and are not registered to deliver regulated care activities.</p>
      <p>Urban Carers Ltd is registered in England and Wales at Companies House under company number 15419139. Registered office: {esc(', '.join(CONTACT['address']))}.</p>
      <p>© {YEAR} Urban Carers Ltd. All rights reserved.</p>
      <p><a href="/privacy">Privacy notice</a></p>
    </div>
  </div>
</footer>"""


def render_contact_details() -> str:
    return f"""<ul class="contact-details">
  <li>{icon('map-pin')}<span>{esc(', '.join(CONTACT['address']))}</span></li>
  <li>{icon('phone')}<a href="tel:{CONTACT['tel']}">{esc(CONTACT['phone'])}</a></li>
  <li>{icon('mail')}<a href="mailto:{CONTACT['email']}">{esc(CONTACT['email'])}</a></li>
  <li>{icon('clock')}<span>{esc(CONTACT['hours'])}</span></li>
</ul>"""


# ----------------------------------------------------------------------------
# blocks
# ----------------------------------------------------------------------------

def render_button(b: dict) -> str:
    cls = "btn"
    if b.get("variant") == "outline":
        cls += " btn-outline"
    elif b.get("variant") == "ink":
        cls += " btn-ink"
    if b.get("size") == "sm":
        cls += " btn-sm"
    ic = icon(b["icon"]) if b.get("icon") else ""
    return '<a href="%s" class="%s">%s%s</a>' % (b["href"], cls, esc(b["label"]), ic)


def render_cards(block: dict) -> str:
    out = []
    for it in block["items"]:
        ic = '<div class="card-icon">%s</div>' % icon(it["icon"]) if it.get("icon") else ""
        out.append('<div class="card">%s<h3>%s</h3><p>%s</p></div>' % (ic, esc(it["title"]), esc(it["text"])))
    return '<div class="cards cols-%d">%s</div>' % (block.get("cols", 3), "".join(out))


def render_feature_cards(block: dict) -> str:
    out = []
    for it in block["items"]:
        out.append(
            '<div class="feature">'
            '<span class="feature-n" aria-hidden="true">%s</span>'
            '<div class="feature-icon">%s</div>'
            '<h3>%s</h3><p>%s</p><span class="tag">%s</span>'
            '</div>' % (esc(it["n"]), icon(it["icon"]), esc(it["title"]), esc(it["text"]), esc(it["tag"]))
        )
    return '<div class="features">%s</div>' % "".join(out)


def render_pros_cons(block: dict) -> str:
    cols = []
    for col in block["cols"]:
        ic = icon("check") if col["kind"] == "check" else icon("x")
        items = "".join('<li class="%s">%s%s</li>' % (col["kind"], ic, esc(i)) for i in col["items"])
        cols.append('<div class="panel"><h3>%s</h3><ul class="icon-items">%s</ul></div>' % (esc(col["title"]), items))
    return '<div class="two-col">%s</div>' % "".join(cols)


def render_steps(block: dict) -> str:
    items = "".join(
        '<li><span class="num" aria-hidden="true">%d</span><p>%s</p></li>' % (i + 1, esc(s)) for i, s in enumerate(block["items"])
    )
    return '<ol class="steps cols-%d">%s</ol>' % (block.get("cols", 3), items)


def render_icon_list(block: dict) -> str:
    ic = icon(block.get("icon", "check"))
    items = "".join('<li>%s%s</li>' % (ic, esc(s)) for s in block["items"])
    return '<ul class="icon-grid">%s</ul>' % items


def render_boundaries(block: dict) -> str:
    items = "".join('<div class="boundary">%s%s</div>' % (icon("x"), esc(s)) for s in block["items"])
    return '<div class="boundaries">%s</div>' % items


def render_faq(block: dict) -> str:
    items = "".join('<details class="faq-item"><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in block["items"])
    return '<div class="faq">%s</div>' % items


def render_rooms(block: dict) -> str:
    rooms = "".join(
        '<div class="room"><div class="room-head"><h3>%s</h3><span class="badge badge-secondary">%s</span></div>'
        '<p class="room-type">%s</p><p class="room-size">%s</p></div>' % (esc(r["name"]), esc(r["status"]), esc(r["kind"]), esc(r["size"]))
        for r in block["items"]
    )
    note = '<p class="room-note">%s</p>' % esc(block["note"]) if block.get("note") else ""
    return '<div class="rooms">%s</div>%s' % (rooms, note)


def render_p(block: dict) -> str:
    style = block.get("style", "muted")
    cls = {"muted": "p-muted", "body": "p-body", "note": "p-note", "first": "p-first", "after-h3": "p-after-h3"}.get(style, "p-muted")
    if block.get("narrow"):
        cls += " narrow"
    return '<p class="%s">%s</p>' % (cls, block["text"])


def render_block(block: dict) -> str:
    t = block["type"]
    if t == "cards":
        return render_cards(block)
    if t == "feature_cards":
        return render_feature_cards(block)
    if t == "pros_cons":
        return render_pros_cons(block)
    if t == "steps":
        return render_steps(block)
    if t == "icon_list":
        return render_icon_list(block)
    if t == "boundaries":
        return render_boundaries(block)
    if t == "faq":
        return render_faq(block)
    if t == "rooms":
        return render_rooms(block)
    if t == "p":
        return render_p(block)
    if t == "h3":
        return '<h3 class="sub">%s</h3>' % esc(block["text"])
    if t == "buttons":
        return '<div class="btn-row">%s</div>' % "".join(render_button(b) for b in block["items"])
    # article blocks (privacy notice)
    if t == "h2":
        return "<h2>%s</h2>" % esc(block["text"])
    if t == "ul":
        return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in block["items"])
    if t == "callout":
        return '<div class="callout"><h2>%s</h2><ul>%s</ul></div>' % (esc(block["title"]), "".join("<li>%s</li>" % i for i in block["items"]))
    if t == "table":
        head = "".join('<th scope="col">%s</th>' % esc(h) for h in block["head"])
        rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (esc(a), esc(b)) for a, b in block["rows"])
        return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, rows)
    raise ValueError("unknown block type: %s" % t)


# ----------------------------------------------------------------------------
# forms (plain mailto: forms, no JavaScript)
# ----------------------------------------------------------------------------

def render_form(spec: dict, kind: str) -> str:
    action = "mailto:%s?subject=%s" % (CONTACT["email"], spec["subject"].replace(" ", "%20"))
    fields = []
    for f in spec["fields"]:
        req = " required" if f.get("required") else ""
        attrs = ' id="%s" name="%s"%s' % (f["id"], esc(f["name"]), req)
        if f.get("placeholder"):
            attrs += ' placeholder="%s"' % esc(f["placeholder"])
        if f.get("inputmode"):
            attrs += ' inputmode="%s"' % f["inputmode"]
        if f.get("select"):
            opts = '<option value="" disabled selected>Select…</option>' + "".join("<option>%s</option>" % esc(o) for o in f["select"])
            control = "<select%s>%s</select>" % (attrs, opts)
        elif f.get("textarea"):
            control = '<textarea%s rows="%d"></textarea>' % (attrs, f.get("rows", 5))
        else:
            control = '<input%s type="%s">' % (attrs, f.get("type", "text"))
        wide = ' class="wide"' if f.get("wide") else ""
        fields.append('<div%s><label for="%s">%s</label>%s</div>' % (wide, f["id"], esc(f["label"]), control))
    btn_cls = "btn" if kind == "referral" else "btn btn-ink"
    return (
        '<form class="form form-%s" method="post" action="%s" enctype="text/plain">%s'
        '<p class="form-note wide">%s</p>'
        '<div class="wide"><button type="submit" class="%s">%s</button></div>'
        '</form>'
        '<p class="form-fallback">%s</p>'
    ) % (kind, action, "".join(fields), spec["privacy_note"], btn_cls, esc(spec["submit"]),
         FORM_FALLBACK.format(email=CONTACT["email"], tel=CONTACT["tel"], phone=CONTACT["phone"]))


# ----------------------------------------------------------------------------
# sections
# ----------------------------------------------------------------------------

def render_section(sec: dict, page: dict) -> str:
    t = sec["type"]
    if t == "home_hero":
        buttons = "".join(render_button(b) for b in sec["buttons"])
        return f"""<section class="hero">
  <div class="container hero-grid">
    <div class="hero-text">
      <p class="eyebrow">{esc(sec['eyebrow'])}</p>
      <h1>{esc(sec['h1'])}</h1>
      <p class="lead">{esc(sec['lead'])}</p>
      <div class="btn-row">{buttons}</div>
    </div>
    <div class="hero-panel">
      <div class="stat">
        <p class="stat-big">{esc(sec['stat']['big'])}</p>
        <p class="stat-small">{esc(sec['stat']['small'])}</p>
      </div>
    </div>
  </div>
</section>"""
    if t == "strip":
        items = "".join('<div class="strip-item"><p class="strip-title">%s</p><p>%s</p></div>' % (esc(a), esc(b)) for a, b in sec["items"])
        return '<div class="strip"><div class="container strip-grid">%s</div></div>' % items
    if t == "section":
        cls = "section muted" if sec.get("muted") else "section"
        badge = '<span class="badge">%s</span>' % esc(sec["badge"]) if sec.get("badge") else ""
        intro = '<p class="intro">%s</p>' % esc(sec["intro"]) if sec.get("intro") else ""
        body = "".join(render_block(b) for b in sec.get("blocks", []))
        return '<section class="%s"><div class="container">%s<h2>%s</h2>%s<div class="section-body">%s</div></div></section>' % (cls, badge, esc(sec["title"]), intro, body)
    if t == "cta":
        return (
            '<section class="cta"><div class="container cta-inner"><div><h2>%s</h2><p>%s</p></div>%s</div></section>'
            % (esc(sec["title"]), esc(sec["text"]), render_button(sec["button"]))
        )
    if t == "referral_form":
        form = render_form(page["module"].REFERRAL_FORM, "referral")
        return (
            '<div class="container form-layout form-layout-referral"><div class="form-main">%s</div>'
            '<aside class="aside"><h2>%s</h2>%s</aside></div>' % (form, esc(sec["aside_title"]), render_contact_details())
        )
    if t == "enquiry_form":
        form = render_form(page["module"].ENQUIRY_FORM, "enquiry")
        return '<div class="container form-layout form-layout-enquiry"><div class="form-main">%s</div><div class="aside-plain">%s</div></div>' % (form, render_contact_details())
    if t == "article":
        return '<article class="container article">%s</article>' % "".join(render_block(b) for b in sec["blocks"])
    raise ValueError("unknown section type: %s" % t)


def render_page_hero(hero: dict) -> str:
    lead = '<div class="lead">%s</div>' % esc(hero["lead"]) if hero.get("lead") else ""
    return '<section class="page-hero"><div class="container"><p class="eyebrow">%s</p><h1>%s</h1>%s</div></section>' % (esc(hero["eyebrow"]), esc(hero["h1"]), lead)


# ----------------------------------------------------------------------------
# page
# ----------------------------------------------------------------------------

def head_html(page: dict, logo_url: str, favicon_src: str | None) -> str:
    url = SITE_URL + page["path"]
    org = dict(ORGANIZATION, logo=logo_url)
    scripts = [jsonld(org)]
    if page.get("website_jsonld"):
        scripts.append(jsonld({"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL + "/"}))
    if page.get("faq"):
        scripts.append(jsonld({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faq"]],
        }))
    if page["path"] != "/":
        scripts.append(jsonld({
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": page["breadcrumb"], "item": url},
            ],
        }))
    fav = ('<link rel="icon" type="image/png" href="/%s">\n<link rel="apple-touch-icon" href="/%s">\n' % (favicon_src, favicon_src)) if favicon_src else ""
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page['title'])}</title>
<meta name="description" content="{esc(page['description'])}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="en_GB">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['description'])}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/styles.css">
{fav}{chr(10).join(scripts)}"""


def render_page(page: dict, logo_src: str, logo_url: str, favicon_src: str | None) -> str:
    body = []
    if page.get("hero"):
        body.append(render_page_hero(page["hero"]))
    for sec in page["sections"]:
        body.append(render_section(sec, page))
    doc = f"""<!doctype html>
<html lang="{LANG}">
<head>
{head_html(page, logo_url, favicon_src)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{render_header(page['path'], logo_src)}
<main id="main">
{chr(10).join(body)}
</main>
{render_footer(logo_src)}
</body>
</html>
"""
    return relativise(doc, page["file"])


def render_404(logo_src: str, logo_url: str, favicon_src: str | None) -> str:
    page = {"path": "/404", "title": "Page not found | Urban Carers", "description": "The page you're looking for doesn't exist or has been moved.", "breadcrumb": "Page not found"}
    head = head_html(page, logo_url, favicon_src)
    head = "\n".join(l for l in head.splitlines() if "canonical" not in l and "og:url" not in l and "BreadcrumbList" not in l)
    head = head.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1)
    doc = f"""<!doctype html>
<html lang="{LANG}">
<head>
{head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{render_header('/404', logo_src)}
<main id="main">
<section class="not-found"><div class="container"><h1>404</h1><h2>Page not found</h2><p>The page you're looking for doesn't exist or has been moved.</p><div class="btn-row"><a href="/" class="btn btn-sm">Go home</a></div></div></section>
</main>
{render_footer(logo_src)}
</body>
</html>
"""
    # 404.html is served for any missing path, at any depth, so its links are absolute.
    return relativise(doc, "404.html", base=SITE_URL)


def write(name: str, text: str) -> None:
    with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", name)


def build() -> int:
    if os.path.exists(os.path.join(ROOT, LOGO_LOCAL)):
        logo_src, logo_url = "/" + LOGO_LOCAL, SITE_URL + "/" + LOGO_LOCAL
    else:
        logo_src = logo_url = LOGO_REMOTE
    favicon_src = FAVICON_LOCAL if os.path.exists(os.path.join(ROOT, FAVICON_LOCAL)) else None

    pages = load_pages()
    for page in pages:
        write(page["file"], render_page(page, logo_src, logo_url, favicon_src))
    write("404.html", render_404(logo_src, logo_url, favicon_src))

    urls = "".join("  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (SITE_URL, p["path"], TODAY) for p in pages)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    write("robots.txt", "User-agent: Googlebot\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\nUser-agent: Twitterbot\nAllow: /\n\nUser-agent: facebookexternalhit\nAllow: /\n\nUser-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE_URL)
    write(".nojekyll", "")

    # sanity: every JSON-LD block must parse
    for p in pages:
        with open(os.path.join(ROOT, p["file"]), encoding="utf-8") as f:
            doc = f.read()
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
            json.loads(m.group(1).replace("<\\/", "</"))
    print("built %d pages (%s)" % (len(pages), TODAY))
    return 0


if __name__ == "__main__":
    sys.exit(build())
