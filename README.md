# Soeteman Software documentation

Source for https://docs.soetemansoftware.nl — the documentation of CMSImport, MediaProtect, MemberExport and
SEOChecker, built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Layout

```
landing/                          site root page (product cards)
products/<product>/product.yml    product name + versions in the version selector (first = default)
products/<product>/<version>/     one MkDocs project per version (mkdocs.yml + docs/)
shared/base.yml                   shared MkDocs config, inherited by every version
scripts/build.py                  builds everything into site/
source-pdfs/                      original PDF manuals (conversion source only)
.github/workflows/                pr-check.yml (build on PR), deploy.yml (deploy on merge to main)
```

Published URLs: `/<product>/<version>/`, e.g. `/cmsimport/latest/` and `/cmsimport/17/`.
`/<product>/` redirects to the first version listed in `product.yml`.

## Build and preview locally

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows (bash: source .venv/Scripts/activate)
pip install -r requirements.txt

# Live preview of one product/version while writing
mkdocs serve -f products/cmsimport/latest/mkdocs.yml

# Full site, exactly as deployed (version selector works here)
python scripts/build.py
python -m http.server -d site 8000   # open http://localhost:8000
```

## Contributing

1. Create a branch (`claude/...` for Claude-made changes), never commit to `main`.
2. Edit Markdown under `products/<product>/<version>/docs/`. Add new pages to `nav` in that version's `mkdocs.yml`.
3. Open a Pull Request. The **PR check** workflow builds the whole site with `--strict`.
4. Merge. The **Deploy docs** workflow publishes the site to GitHub Pages.

See `CLAUDE.md` for the writing style guide.

## Adding a version

1. Copy the newest version folder, e.g. `products/cmsimport/latest` → `products/cmsimport/18`.
2. Update `site_url` in the copied `mkdocs.yml`.
3. Add the folder to `versions` in `products/cmsimport/product.yml` (order = order in the selector).

## One-time GitHub setup

- **Settings → Pages → Build and deployment → Source:** GitHub Actions.
- **Settings → Pages → Custom domain:** `docs.soetemansoftware.nl`, then tick **Enforce HTTPS**.
- **DNS:** `CNAME` record `docs` → `soeteman-software.github.io`.
- **Branch protection on `main`:** require a pull request and the `PR check / build` status.
