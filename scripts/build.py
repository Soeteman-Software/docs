"""Build the complete documentation site into ./site.

Layout of the output:
    site/                       landing page (landing/mkdocs.yml)
    site/<product>/index.html   redirect to the first (newest) version
    site/<product>/versions.json  feeds the Material version selector
    site/<product>/<version>/   one MkDocs build per products/<product>/<version>/mkdocs.yml

Usage:
    python scripts/build.py            # build everything
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOMAIN = "docs.soetemansoftware.nl"

REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Redirecting…</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
</head><body><a href="{target}">Continue to the documentation</a></body></html>
"""


def mkdocs_build(config: Path, out: Path) -> None:
    print(f"Building {config.relative_to(ROOT)} -> {out.relative_to(ROOT)}", flush=True)
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(config), "--site-dir", str(out)],
        check=True,
    )


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)

    mkdocs_build(ROOT / "landing" / "mkdocs.yml", SITE)

    for product_file in sorted((ROOT / "products").glob("*/product.yml")):
        product_dir = product_file.parent
        product = yaml.safe_load(product_file.read_text(encoding="utf-8"))
        versions = []
        for v in product["versions"]:
            folder = str(v["folder"])
            mkdocs_build(product_dir / folder / "mkdocs.yml", SITE / product_dir.name / folder)
            versions.append({"version": folder, "title": v["title"], "aliases": []})

        out = SITE / product_dir.name
        (out / "versions.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
        (out / "index.html").write_text(REDIRECT.format(target=f"{versions[0]['version']}/"), encoding="utf-8")

    (SITE / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")
    print(f"Done: {SITE}")


if __name__ == "__main__":
    main()
