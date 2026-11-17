# jimmychen

Portfolio website of Jimmy Chen. A plain static site, served by GitHub Pages from the `main` branch.

## Editing

All text and picture choices live in `content.py`. After changing it, rebuild the pages:

```
pip install pillow
python3 build.py
```

Then commit and push. The generated pages (`index.html`, `about/`, `cv/`, `contact/`, `works/`) are committed alongside the source, so GitHub Pages needs no build step.

- `content.py`: site text, CV, contact details, the list of works, and the blocks on each work page
- `build.py`: turns `content.py` into HTML
- `assets/css/style.css`: the design
- `assets/works/<work>/`: images as WebP, each saved up to 1800px wide plus 1200px and 700px versions (`name.webp`, `name-1200.webp`, `name-700.webp`); `share.jpg` is the link-preview image
- `assets/fonts/`: Newsreader, licensed under the SIL Open Font License (`OFL.txt`)

## Publishing

In the repository settings, open Pages and choose "Deploy from a branch", branch `main`, folder `/ (root)`.
The site then appears at https://yiwaguli.github.io/jimmychen/
