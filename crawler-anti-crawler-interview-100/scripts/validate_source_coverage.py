from pathlib import Path
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
import sys
root=Path(__file__).resolve().parents[1]
src=root/'assets/source/爬虫与反爬虫面试100题_剑指Offer式详解.docx'
baseline=(root/'docs/PDF-BASELINE.md').read_text(encoding='utf-8')
doc=Document(src)
missing=[]; n=0
for child in doc.element.body.iterchildren():
    if isinstance(child,CT_P):
        t=Paragraph(child,doc).text.strip()
        if t:
            n+=1
            # markdown conversions may add formatting only; paragraph text should remain literal.
            if t not in baseline: missing.append(t[:120])
    elif isinstance(child,CT_Tbl):
        table=Table(child,doc)
        for r in table.rows:
            for c in r.cells:
                for line in c.text.splitlines():
                    t=line.strip()
                    if t:
                        n+=1
                        if t not in baseline: missing.append(t[:120])
if missing:
    print('Missing source fragments:',len(missing))
    print('\n'.join(missing[:20])); sys.exit(1)
print(f'OK: {n} non-empty source fragments mirrored in docs/PDF-BASELINE.md')
