# jimmychen

Portfolio website of Jimmy Chen. A plain static site, served by GitHub Pages from the `main` branch.

## Editing

All text and picture choices live in `content.py`. After changing it, rebuild the pages:

```
pip install pillow
python3 build.py
```

Then commit and push. The generated pages (`index.html`, `about/`, `works/`) are committed alongside the source, so GitHub Pages needs no build step.

- `content.py`: site text, the list of works, and the blocks on each work page
- `build.py`: turns `content.py` into HTML
- `assets/css/style.css`: the design
- `assets/works/<work>/`: images, each saved at 1800px and 900px wide (`name.jpg`, `name-900.jpg`)
- `assets/fonts/`: Newsreader, licensed under the SIL Open Font License (`OFL.txt`)

## Publishing

In the repository settings, open Pages and choose "Deploy from a branch", branch `main`, folder `/ (root)`.
The site then appears at https://yiwaguli.github.io/jimmychen/
