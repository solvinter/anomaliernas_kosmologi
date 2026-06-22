from pathlib import Path
from html import escape

src = Path("notes/fragments")
dst = Path("fragments_html")

dst.mkdir(exist_ok=True)

links = []

for f in sorted(src.iterdir()):
    if not f.is_file():
        continue

    text = f.read_text(encoding="utf-8", errors="ignore")
    title = f.name
    output_file = dst / f"{f.name}.html"

    html = f"""<!doctype html>
<html lang="sv">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <main>
    <header class="site-header">
      <h1>{escape(title)}</h1>
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

    output_file.write_text(html, encoding="utf-8")
    links.append(f'        <li><a href="fragments_html/{f.name}.html">{escape(title)}</a></li>')

library_html = f"""<!doctype html>
<html lang="sv">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Library of Fragments</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <main>
    <header class="site-header">
      <p class="label">fragment archive / source material</p>
      <h1>Library of Fragments</h1>
      <p class="lead">
        En samling av textfragment som utgör byggstenarna i verket.
      </p>
    </header>

    <section aria-labelledby="fragments">
      <h2 id="fragments">Fragments</h2>

      <ul class="links">
{chr(10).join(links)}
      </ul>
    </section>

    <section aria-labelledby="home">
      <h2 id="home">Back</h2>
      <p><a href="index.html">Tillbaka till Anomalierna</a></p>
    </section>
  </main>
</body>
</html>
"""

Path("library.html").write_text(library_html, encoding="utf-8")

print(f"Generated {len(links)} fragment HTML files and library.html")
