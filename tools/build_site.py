"""Build the deployable site in docs/ from the single-page prototype.

The prototype (prototype/index.html) is written as a page body for the Claude artifact viewer,
which adds the <!doctype>, <head> and a small reset at publish time. GitHub Pages serves files
as they are, so this script wraps the prototype in a full HTML document and writes it, plus the
files GitHub Pages needs, to docs/.

Usage (from the project root):
    python3 tools/build_site.py
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "prototype" / "index.html"
OUT = ROOT / "docs"

DOMAIN = "teresayun.me"
TITLE = "Teresa Wong"
DESCRIPTION = (
    "Teresa Wong, MIT '30, studying AI and math. Generative models from scratch, "
    "avionics and controls for the MIT Rocket Team"
)

HEAD = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESCRIPTION}">
<meta name="author" content="Teresa Wong">
<meta name="theme-color" content="#F1F3F2">
<link rel="canonical" href="https://{DOMAIN}/">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:url" content="https://{DOMAIN}/">
<meta name="twitter:card" content="summary">
<style>
/* the reset the artifact viewer used to provide */
:root {{ color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
body {{ margin: 0; font: 14px system-ui, -apple-system, sans-serif; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
</style>
"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#15171C"/>
<g fill="#1F77B4">
<circle cx="18" cy="18" r="4"/><circle cx="32" cy="18" r="4"/><circle cx="46" cy="18" r="4"/>
<circle cx="32" cy="31" r="4"/><circle cx="32" cy="44" r="4"/>
</g>
<circle cx="46" cy="46" r="5" fill="#FF7F0E"/>
</svg>
"""

NOT_FOUND = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>loss = NaN · Teresa Wong</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
:root { --bg: #F1F3F2; --ink: #101418; --muted: #5B6470; --accent: #1F77B4; --accent2: #FF7F0E; color-scheme: light; }
body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: var(--bg); color: var(--ink);
       font: 16px ui-monospace, Menlo, Consolas, monospace; padding: 0 max(16px, env(safe-area-inset-left, 0px)); }
main { max-width: 34rem; }
h1 { margin: 0 0 12px; font-size: 40px; color: var(--accent2); }
p { margin: 0 0 10px; color: var(--muted); line-height: 1.6; }
a { color: var(--accent); }
</style>
</head>
<body>
<main>
<h1>loss = NaN</h1>
<p>404: this page diverged during training.</p>
<p>Try lowering the learning rate, or <a href="/">go back to the home page</a>.</p>
</main>
</body>
</html>
"""


def build() -> None:
    body = SRC.read_text(encoding="utf-8")
    # the artifact-only lines: its own <title> and the viewer's side-gutter promise
    body = re.sub(r"^<title>.*?</title>\s*\n", "", body, count=1)
    body = re.sub(r'^<meta name="claude:viewport-fit-sides"[^>]*>\s*\n', "", body, count=1, flags=re.M)
    # everything up to the first </style> belongs in <head>; the rest is the page body
    split = body.index("</style>") + len("</style>")
    head_part, body_part = body[:split], body[split:]

    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(
        HEAD + head_part + "\n</head>\n<body>\n" + body_part.lstrip("\n") + "\n</body>\n</html>\n",
        encoding="utf-8",
    )
    (OUT / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (OUT / "404.html").write_text(NOT_FOUND, encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)}/ from {SRC.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
