# CLAUDE.md

Documentation site for the Soeteman Software Umbraco packages (CMSImport, MediaProtect, MemberExport,
SEOChecker), built with MkDocs + Material and published to https://docs.soetemansoftware.nl via GitHub Pages.
See `README.md` for layout and build commands.

## Project rules
- Every change goes on its own branch prefixed `claude/` (`git switch -c claude/...`). NEVER commit directly to
  `main`; always merge via a Pull Request. Merging to `main` deploys the site automatically.
- NEVER use git worktrees (no `git worktree add`, no EnterWorktree, no `isolation: "worktree"` agents).
- Keep shell commands simple: one plain command per call, no loops or long chains.
- Run `python scripts/build.py` before opening a PR; it builds with `--strict` and must pass without warnings.
- Update `README.md` whenever a change affects the repo layout, build, deployment or how to add a product/version.
- This repo is public: never add EULAs, licence keys, customer data or internal notes.

## Repository layout (short)
- `products/<product>/product.yml` — product name and the versions shown in the version selector (first = default).
- `products/<product>/<version>/mkdocs.yml` + `docs/` — one MkDocs project per version; inherits `shared/base.yml`.
- `landing/` — site root page with product cards.
- `source-pdfs/` — original PDF manuals, used only as conversion source.

## Writing style guide
- Audience: Umbraco developers and editors. Address the reader as "you"; use short, active sentences.
- One topic per page. Start each page with one sentence saying what the page covers.
- Use Umbraco terminology as in https://docs.umbraco.com/umbraco-cms/17.latest (Document Type, Backoffice,
  Content section, Media section, Member Group, etc.). Spell product names exactly: CMSImport, MediaProtect,
  MemberExport, SEOChecker.
- Headings: sentence case; one `#` title per page; don't skip levels.
- Procedures: numbered lists, one action per step. UI labels in **bold**, keys with `++ctrl+s++`.
- Use admonitions instead of bold "Note:" text: `!!! note`, `!!! tip`, `!!! warning` (data loss / breaking).
- Code and config: fenced blocks with a language (`csharp`, `json`, `xml`, `bash`), complete and copy-pasteable.
- Images: PNG in `docs/assets/images/`, named `<page>-<n>.png`, always with meaningful alt text. Crop to the
  relevant UI area; no screenshots of text that could be written as text.
- Version differences: write `latest` first, then copy to `17/` and change only what differs.
- Links: relative links to `.md` files inside a version; never hard-code another version's URL.
