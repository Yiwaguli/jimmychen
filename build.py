#!/usr/bin/env python3
"""Builds the static site from content.py.  Usage: python3 build.py

Needs Python 3 and Pillow (pip install pillow).
Writes index.html, about/, cv/, contact/, works/<slug>/ and, if research.py exists, research/.
"""
import html, os, re
from PIL import Image
from content import SITE, ABOUT, CV, CONTACT, WORKS

try:
    from research import RESEARCH
except ImportError:
    RESEARCH = None

ROOT = os.path.dirname(os.path.abspath(__file__))
esc = html.escape

PLAY_SCRIPT = """<script>
document.addEventListener('click', function (e) {
  var a = e.target.closest('a[data-yt]');
  if (!a) return;
  e.preventDefault();
  var f = document.createElement('iframe');
  f.src = 'https://www.youtube-nocookie.com/embed/' + a.dataset.yt + '?autoplay=1&rel=0';
  f.title = 'Video';
  f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; web-share';
  f.referrerPolicy = 'strict-origin-when-cross-origin';
  f.allowFullscreen = true;
  a.replaceWith(f);
});
</script>"""


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def variants(folder, name):
    """Every width a picture was saved at: [(width, height, filename)], smallest first."""
    out = []
    base = os.path.join(ROOT, "assets", folder)
    for suffix in ("-700", "-1200", ""):
        fn = f"{name}{suffix}.webp"
        p = os.path.join(base, fn)
        if os.path.exists(p):
            with Image.open(p) as im:
                out.append((im.size[0], im.size[1], fn))
    return out


def picture(root, folder, im, sizes, lazy=True):
    v = variants(folder, im["name"])
    if not v:
        print(f"  ! missing image: {folder}/{im['name']}.webp (skipped)")
        return None, 1
    base = f"{root}assets/{folder}/"
    w, h, fn = v[-1]
    srcset = ", ".join(f"{base}{f} {vw}w" for vw, _, f in v)
    extra = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    alt = esc(im["alt"])
    tag = (f'<img src="{base}{fn}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" '
           f'alt="{alt}"{extra} decoding="async">')
    return tag, w / h


def figure(root, folder, im, sizes, lazy=True):
    tag, ar = picture(root, folder, im, sizes, lazy)
    if not tag:
        return "", ar
    cap = f"<figcaption>{im['cap']}</figcaption>" if im.get("cap") else ""
    return f"<figure>{tag}{cap}</figure>", ar


def prose(paras, cls="prose"):
    return f'<div class="{cls}">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def nav_items():
    items = list(SITE["nav"])
    if RESEARCH:
        items.insert(1, ("Research", "research/"))
    return items


def page(root, title, description, body, current=None, image=None, script=False):
    nav = ""
    for label, href in nav_items():
        cur = ' aria-current="page"' if href == current else ""
        nav += f'<li><a href="{root}{href}"{cur}>{label}</a></li>'
    og = f'\n<meta property="og:image" content="{SITE["url"]}{image}">' if image else ""
    name = SITE["name"]
    home = root or "./"
    tail = PLAY_SCRIPT if script else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">{og}
<link rel="preload" href="{root}assets/fonts/newsreader-roman.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/newsreader-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
<p class="masthead__name"><a href="{home}">{name}</a></p>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</header>
<main id="main">
{body}
</main>
<footer class="foot"><p>&copy; {name}. All works and images belong to the artist and collaborators.</p></footer>
{tail}
</body>
</html>
"""


def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


def video(vid, cap):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return (f'<figure><div class="frame"><a class="play" href="https://www.youtube.com/watch?v={vid}" data-yt="{vid}">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" decoding="async">'
            f'<span class="play__btn" aria-hidden="true"></span><span class="skip">Play video</span></a></div>{c}</figure>')


def render_block(root, folder, b, first):
    lazy = not first
    t = b["t"]
    if t == "image":
        pos = b.get("pos", "full")
        sizes = "(min-width: 1560px) 1400px, 92vw" if pos == "full" else "(min-width: 740px) 62vw, 92vw"
        fig, _ = figure(root, folder, b["img"], sizes, lazy)
        txt = prose(b["text"]) if b.get("text") else ""
        return f'<section class="block block--{pos}">{fig}{txt}</section>' if fig else ""
    if t == "split":
        a, c = b.get("ratio", (62, 38))
        fig, _ = figure(root, folder, b["img"], f"(min-width: 740px) {round(a * 0.9)}vw, 92vw", lazy)
        flip = " flip" if b.get("flip") else ""
        return (f'<section class="block block--split{flip}" style="--img:{a}fr;--txt:{c}fr">'
                f'{fig}{prose(b["text"])}</section>')
    if t == "row":
        n = len(b["imgs"])
        figs = []
        for im in b["imgs"]:
            tag, ar = picture(root, folder, im, f"(min-width: 740px) {round(92 / n)}vw, 92vw", lazy)
            if not tag:
                continue
            cap = f"<figcaption>{im['cap']}</figcaption>" if im.get("cap") else ""
            figs.append(f'<figure style="flex:{ar:.4f} 1 0%;--ar:{ar:.4f}">{tag}{cap}</figure>')
        cls = "block block--row" + (" tight" if b.get("tight") else "") + (" keep" if b.get("keep") else "")
        return f'<section class="{cls}">{"".join(figs)}</section>'
    if t == "text":
        pos = b.get("pos", "inset")
        head = f'<h2 class="block__head">{b["head"]}</h2>' if b.get("head") else ""
        return f'<section class="block block--{pos}">{head}{prose(b["text"])}</section>'
    if t == "videos":
        return f'<section class="block block--videos">{"".join(video(v, c) for v, c in b["items"])}</section>'
    raise ValueError(t)


def colophon(heading, rows, cls=""):
    dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
    return f'<section class="colophon{cls}"><h2>{heading}</h2><dl>{dl}</dl></section>'


def build():
    # home
    items = []
    for i, w in enumerate(WORKS):
        tag, _ = picture("", f'works/{w["slug"]}', w["cover"],
                         "(min-width: 990px) 28vw, (min-width: 740px) 44vw, 92vw", lazy=i > 2)
        items.append(
            f'<li class="work"><a href="works/{w["slug"]}/">{tag}'
            f'<h2 class="work__title">{w["title"]}</h2>'
            f'<p class="work__year">{w["year"]}</p><p class="work__summary">{w["summary"]}</p></a></li>')
    write("index.html", page("", SITE["name"], SITE["description"],
                             '<h1 class="skip">Works</h1>\n<ul class="works">\n' + "\n".join(items) + "\n</ul>",
                             current="", image=f'assets/works/{WORKS[0]["slug"]}/share.jpg'))

    # works
    for i, w in enumerate(WORKS):
        root, slug = "../../", w["slug"]
        meta = f'<span>{w["year"]}. {w["medium"]}</span>'
        if w.get("where"):
            meta += f'<span class="where">{w["where"]}</span>'
        parts = [f'<header class="piece__head"><h1 class="piece__title">{w["title"]}</h1>'
                 f'<p class="piece__meta">{meta}</p></header>']
        for k, b in enumerate(w["blocks"]):
            parts.append(render_block(root, f"works/{slug}", b, first=k == 0))
        if w.get("credits"):
            parts.append(colophon("Credits", w["credits"], " block"))
        if w.get("links"):
            rows = "".join(f'<li><a href="{esc(u)}" rel="noopener">{t}</a></li>' for t, u in w["links"])
            parts.append(f'<section class="block colophon"><h2>Links</h2><ul>{rows}</ul></section>')
        prev_w, next_w = WORKS[i - 1] if i else None, WORKS[i + 1] if i + 1 < len(WORKS) else None
        pager = '<nav class="pager" aria-label="More works">'
        if prev_w:
            pager += f'<a class="prev" href="../{prev_w["slug"]}/"><small>Previous</small><em>{prev_w["title"]}</em></a>'
        if next_w:
            pager += f'<a class="next" href="../{next_w["slug"]}/"><small>Next</small><em>{next_w["title"]}</em></a>'
        pager += "</nav>"
        title = w.get("plain_title") or plain(w["title"])
        has_video = any(b["t"] == "videos" for b in w["blocks"])
        write(f"works/{slug}/index.html",
              page(root, f'{title} | {SITE["name"]}', plain(w["summary"]),
                   '<article class="piece">\n' + "\n".join(p for p in parts if p) + f"\n{pager}\n</article>",
                   image=f"assets/works/{slug}/share.jpg", script=has_video))

    # research (only when research.py is present)
    if RESEARCH:
        r = RESEARCH
        parts = [f'<header class="piece__head"><h1 class="piece__title">{r["title"]}</h1>'
                 f'<p class="piece__sub">{r["subtitle"]}</p><p class="piece__meta"><span>{r["meta"]}</span></p></header>']
        for k, b in enumerate(r["blocks"]):
            parts.append(render_block("../", "research", b, first=k == 0))
        for heading, rows in r.get("lists", []):
            parts.append(colophon(heading, rows, " block"))
        if r.get("references"):
            refs = "".join(f"<li>{x}</li>" for x in r["references"])
            parts.append(f'<section class="block colophon refs"><h2>References</h2><ul>{refs}</ul></section>')
        write("research/index.html",
              page("../", f'Research | {SITE["name"]}', plain(r["summary"]),
                   '<article class="piece">\n' + "\n".join(p for p in parts if p) + "\n</article>", current="research/"))

    # about
    body = (f'<article class="about"><h1 class="skip">About</h1><p class="about__lede">{ABOUT["lede"]}</p>'
            f'{prose(ABOUT["text"])}</article>')
    write("about/index.html", page("../", f'About | {SITE["name"]}', SITE["description"], body, current="about/"))

    # cv
    lists = "".join(colophon(h, rows) for h, rows in CV)
    body = f'<article class="about cv"><h1 class="about__lede">Curriculum vitae</h1>{lists}</article>'
    write("cv/index.html", page("../", f'CV | {SITE["name"]}', f'Curriculum vitae of {SITE["name"]}.', body, current="cv/"))

    # contact
    rows = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in CONTACT["rows"])
    body = (f'<article class="about contact"><h1 class="skip">Contact</h1><p class="about__lede">{CONTACT["lede"]}</p>'
            f'<dl class="contact__list">{rows}</dl></article>')
    write("contact/index.html", page("../", f'Contact | {SITE["name"]}', f'Contact {SITE["name"]}.', body, current="contact/"))

    write("404.html", page("/jimmychen/", f'Page not found | {SITE["name"]}', "Page not found",
                           '<article class="about"><p class="about__lede">This page does not exist. '
                           '<a href="/jimmychen/">Return to the works.</a></p></article>'))
    open(os.path.join(ROOT, ".nojekyll"), "w").close()


if __name__ == "__main__":
    build()
