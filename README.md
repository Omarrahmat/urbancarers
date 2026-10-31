# urbancarers

Static website for Urban Carers Ltd (www.urbancarers.co.uk), built from plain
content files with one Python script and hosted on GitHub Pages.

**Nothing in this repository changes the live website until the domain's DNS is
pointed at GitHub Pages.** Until then www.urbancarers.co.uk keeps serving the old
host, and this site is only visible at the GitHub Pages preview address.

## Build

```
python3 build.py
```

Python 3 (standard library only), no Node, no npm, no other dependencies.
The script reads `content/*.py`, renders every page through the shared layout in
`build.py` and writes to the repository root:

- `index.html`, `about.html`, `accommodation.html`, ... (one file per page;
  GitHub Pages serves `/accommodation` from `accommodation.html`, so the public
  URLs are the same extensionless URLs as today)
- `404.html`, `sitemap.xml`, `robots.txt`, `.nojekyll`

The generated HTML files are committed, because GitHub Pages serves the
repository as it is. Always run the build and commit the output together.

Preview locally with `python3 serve.py` (then open http://127.0.0.1:8000/).
It resolves the extensionless page URLs the same way GitHub Pages does;
`python3 -m http.server` also works but only with the `.html` extensions.

## How the content works

Each page is one file in `content/` that defines a `PAGE` dictionary:

| key           | meaning                                                      |
|---------------|--------------------------------------------------------------|
| `path`        | the public URL path, e.g. `/accommodation`                   |
| `title`       | the `<title>` and `og:title`                                 |
| `description` | the meta description and `og:description`                    |
| `breadcrumb`  | the page name used in the BreadcrumbList structured data     |
| `hero`        | `eyebrow`, `h1` and `lead` for the page header (inner pages)  |
| `sections`    | the page body, a list of sections made of blocks (see below) |
| `faq`         | optional list of `[question, answer]` pairs; also emits FAQPage structured data |

Section types: `section` (title, optional `intro`, `muted`, `badge`, and
`blocks`), `home_hero`, `strip`, `cta`, `referral_form`, `enquiry_form`,
`article`. Block types inside a section: `cards`, `feature_cards`, `pros_cons`,
`steps`, `icon_list`, `boundaries`, `faq`, `rooms`, `p`, `h3`, `buttons`, and for
the privacy notice `h2`, `ul`, `callout`, `table`. Look at an existing page
(for example `content/accommodation.py`) and copy the pattern.

Links inside content are written as site paths (`href="/referrals"`); the build
turns them into links relative to each page so the site works both at the root
domain and at the GitHub Pages preview sub-path. Text is escaped automatically
except in `p`, `ul`, `callout` and `privacy_note` values, which may contain
inline HTML such as links.

### Adding a page

1. Create `content/<slug>.py` with a `PAGE` dictionary (`path` = `/<slug>`).
2. Add the slug to `PAGE_ORDER` in `build.py` (this is also the sitemap order)
   and, if it should be in the menu, to `NAV`.
3. Run `python3 build.py`, check the result with `python3 serve.py`, commit.

### Adding a guide (a page under a folder)

The same steps, with `path` set to `/guides/<slug>` in a content file named
`content/guides-<slug>.py` (any file name works; the public URL comes from
`path`). The output file is derived from the path (`guides/<slug>.html`, served
at `/guides/<slug>`). Relative links and the stylesheet path are computed per
page, so nested pages need no other changes.

## What is fixed in `build.py`

Contact details, the navigation, the footer, the Organization and WebSite
structured data, the sitemap order and the fallback line shown next to the
forms all live at the top of `build.py`.

## Images, fonts and icons

- `assets/logo.png` and `assets/favicon.png` are **not in the repository yet**.
  Until they are added the pages reference the logo at the address the current
  site serves it from, and no favicon is emitted. Drop the real files into
  `assets/` and rebuild: the build switches to the self-hosted files
  automatically (including the logo URL in the structured data).
- Fonts (Manrope and Sora, SIL Open Font License) are self-hosted in `fonts/`;
  no requests go to Google Fonts.
- Icons in `assets/icons/` are from Lucide (ISC licence) and are inlined at
  build time.

## Forms

The referral and contact forms are plain `mailto:` forms addressed to
info@urbancarers.co.uk (the visitor's own email app opens with the details).
There is no form service, no JavaScript and no third-party script anywhere on
the site. A line next to each form gives the email address and phone number for
anyone whose computer has no email app set up.

## Going live (later, by the owner)

See the DNS notes handed over with the build. In short: in the domain's DNS,
point `www` (CNAME) at `omarrahmat.github.io` and the bare domain (four A
records) at GitHub Pages, add a `CNAME` file containing
`www.urbancarers.co.uk` to this repository, enter the custom domain in the
repository's Pages settings and tick "Enforce HTTPS".
