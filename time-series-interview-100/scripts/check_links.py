from pathlib import Path
import re
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
md_files = list(root.rglob("*.md"))
errors=[]
pat=re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for f in md_files:
    text=f.read_text(encoding="utf-8")
    for raw in pat.findall(text):
        link=raw.strip().split()[0]
        if link.startswith(("http://","https://","mailto:","#")):
            continue
        link=unquote(link).split('#',1)[0]
        if not link:
            continue
        target=(f.parent/link).resolve()
        if not target.exists():
            errors.append(f"{f.relative_to(root)} -> {raw}")
if errors:
    raise SystemExit("Broken local links:\n"+"\n".join(errors))
print(f"OK: checked local links in {len(md_files)} markdown files")
