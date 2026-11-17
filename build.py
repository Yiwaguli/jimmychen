#!/usr/bin/env python3
"""Builds the static site from content.py.  Usage: python3 build.py

Needs Python 3 and Pillow (pip install pillow). Writes index.html, about/ and works/<slug>/.
"""
import html, os, re, shutil
from PIL import Image
from content import SITE, ABOUT, WORKS

ROOT = os.path.dirname(os.path.abspath(__file__))
esc = html.escape


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def size(slug, name, suffix=""):
    p = os.path.join(ROOT, "assets", "works", slug, f"{name}{suffix}.jpg")
    if not os.path.exists(p):
        return None
    with Image.open(p) as im:
        return im.size


def picture(root, slug, im, sizes, lazy=True):
    big, small = size(slug, im["name"]), size(slug, im["name"], "-900")
    if not big:
        print(f"  ! missing image: {slug}/{im['name']}.jpg (skipped)")
        return None, 1
    base = f"{root}assets/works/{slug}/{im['name']}"
    srcset = f"{base}-900.jpg {small[0]}w, {base}.jpg {big[0]}w" if small and small[0] < big[0] else f"{base}.jpg {big[0]}w"
    lazy_attr = ' loading="lazy"' if lazy else ""
    alt = esc(im["alt"])
    tag = (f'<img src="{base}.jpg" srcset="{srcset}" sizes="{sizes}" width="{big[0]}" height="{big[1]}" '
           f'alt="{alt}"{lazy_attr} decoding="async">')
    return tag, big[0] / big[1]


def figure(root, slug, im, sizes, lazy=True, style=""):
    tag, ar = picture(root, slug, im, sizes, lazy)
    if not tag:
        return "", ar
    cap = f"<figcaption>{im['cap']}</figcaption>" if im.get("cap") else ""
    return f"<figure{style}>{tag}{cap}</figure>", ar


def prose(paras, cls="prose"):
    return f'<div class="{cls}">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def page(root, title, description, body, current="", image=None):
    nav = ""
    for label, href in SITE["nav"]:
        cur = ' aria-current="page"' if href == current else ""
        nav += f'<li><a href="{root}{href}"{cur}>{label}</a></li>'
    og = f'\n<meta property="og:image" content="{image}">' if image else ""
    name = SITE["name"]
    home = root or "./"
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
</body>
</html>
"""


def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


def render_block(root, slug, b, first):
    lazy = not first
    t = b["t"]
    if t == "image":
        pos = b.get("pos", "full")
        sizes = "(min-width: 1560px) 1400px, 92vw" if pos == "full" else "(min-width: 740px) 62vw, 92vw"
        fig, _ = figure(root, slug, b["img"], sizes, lazy)
        txt = prose(b["text"]) if b.get("text") else ""
        return f'<section class="block block--{pos}">{fig}{txt}</section>' if fig else ""
    if t == "split":
        a, c = b.get("ratio", (62, 38))
        fig, _ = figure(root, slug, b["img"], f"(min-width: 740px) {a}vw, 92vw", lazy)
        flip = " flip" if b.get("flip") else ""
        return (f'<section class="block block--split{flip}" style="--img:{a}fr;--txt:{c}fr">'
                f'{fig}{prose(b["text"])}</section>')
    if t == "row":
        n = len(b["imgs"])
        figs = []
        for im in b["imgs"]:
            tag, ar = picture(root, slug, im, f"(min-width: 740px) {round(92 / n)}vw, 92vw", lazy)
            if not tag:
                continue
            cap = f"<figcaption>{im['cap']}</figcaption>" if im.get("cap") else ""
            figs.append(f'<figure style="flex:{ar:.4f} 1 0%;--ar:{ar:.4f}">{tag}{cap}</figure>')
        cls = "block block--row" + (" tight" if b.get("tight") else "") + (" keep" if b.get("keep") else "")
        return f'<section class="{cls}">{"".join(figs)}</section>'
    if t == "text":
        pos = b.get("pos", "inset")
        return f'<section class="block block--{pos}">{prose(b["text"])}</section>'
    if t == "videos":
        out = []
        for vid, cap in b["items"]:
            c = f"<figcaption>{cap}</figcaption>" if cap else ""
            out.append(
                f'<figure><div class="frame"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0" '
                f'title="Video" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" '
                f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>{c}</figure>')
        return f'<section class="block block--videos">{"".join(out)}</section>'
    raise ValueError(t)


def build():
    # home
    items = []
    for i, w in enumerate(WORKS):
        tag, _ = picture("", w["slug"], w["cover"], "(min-width: 990px) 28vw, (min-width: 740px) 44vw, 92vw", lazy=i > 2)
        items.append(
            f'<li class="work"><a href="works/{w["slug"]}/">{tag}'
            f'<h2 class="work__title">{w["title"]}</h2>'
            f'<p class="work__year">{w["year"]}</p><p class="work__summary">{w["summary"]}</p></a></li>')
    write("index.html", page("", SITE["name"], SITE["description"],
                             f'<h1 class="skip">Works</h1>\n<ul class="works">\n' + "\n".join(items) + "\n</ul>", current=""))

    # works
    for i, w in enumerate(WORKS):
        root, slug = "../../", w["slug"]
        meta = f'<span>{w["year"]}. {w["medium"]}</span>'
        if w.get("where"):
            meta += f'<span class="where">{w["where"]}</span>'
        parts = [f'<header class="piece__head"><h1 class="piece__title">{w["title"]}</h1>'
                 f'<p class="piece__meta">{meta}</p></header>']
        for k, b in enumerate(w["blocks"]):
            parts.append(render_block(root, slug, b, first=k == 0))
        if w.get("credits"):
            rows = "".join(f"<dt>{r}</dt><dd>{n}</dd>" for r, n in w["credits"])
            parts.append(f'<section class="block colophon"><h2>Credits</h2><dl>{rows}</dl></section>')
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
        write(f"works/{slug}/index.html",
              page(root, f'{title} | {SITE["name"]}', plain(w["summary"]),
                   f'<article class="piece">\n' + "\n".join(p for p in parts if p) + f"\n{pager}\n</article>", current=""))

    # about
    lists = ""
    for heading, rows in ABOUT["lists"]:
        dl = "".join(f"<dt>{y}</dt><dd>{t}</dd>" for y, t in rows)
        lists += f'<section class="colophon"><h2>{heading}</h2><dl>{dl}</dl></section>'
    body = (f'<article class="about"><h1 class="skip">About</h1><p class="about__lede">{ABOUT["lede"]}</p>'
            f'{prose(ABOUT["text"])}{lists}</article>')
    write("about/index.html", page("../", f'About | {SITE["name"]}', SITE["description"], body, current="about/"))

    write("404.html", page("/jimmychen/", f'Page not found | {SITE["name"]}', "Page not found",
                           '<article class="about"><p class="about__lede">This page does not exist. '
                           '<a href="/jimmychen/">Return to the works.</a></p></article>'))
    open(os.path.join(ROOT, ".nojekyll"), "w").close()


if __name__ == "__main__":
    build()
