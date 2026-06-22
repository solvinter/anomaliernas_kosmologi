from pathlib import Path
from html import escape

src = Path("notes/fragments")
dst = Path("fragments_html")

dst.mkdir(exist_ok=True)

for f in src.iterdir():
    if not f.is_file():
        continue

    text = f.read_text(encoding="utf-8", errors="ignore")

    html = f"""<!doctype html>
<html lang="sv">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{f.name}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <main>
    <header class="site-header">
      <h1>{f.name}</h1>
    </header>

    <section>
      <pre>{escape(text)}</pre>
    </section>

    <section>
      <p><a href="../library.html">← Tillbaka till Library of Fragments</a></p>
    </section>
  </main>
</body>
</html>
"""

    (dst / f"{f.name}.html").write_text(html, encoding="utf-8")

print(f"Generated {len(list(src.iterdir()))} HTML files in {dst}")
