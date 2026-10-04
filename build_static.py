"""Export the availability figure as a standalone page for GitHub Pages (docs/index.html)."""
from pathlib import Path

from app import fig, tabtitle

out = Path(__file__).parent / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
fig.write_html(out, include_plotlyjs="cdn", full_html=True, config={"displaylogo": False})
html = out.read_text(encoding="utf-8").replace("<head>", f"<head><title>{tabtitle}</title>", 1)
out.write_text(html, encoding="utf-8")
print(f"wrote {out}")
