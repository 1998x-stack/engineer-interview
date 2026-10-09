# -*- coding: utf-8 -*-
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from enrichment_v2_data import PACKS

START = '<!-- V2-ENRICHMENT-START -->'
END = '<!-- V2-ENRICHMENT-END -->'

qfiles = [p for p in ROOT.glob('questions/*/*.md') if p.name != 'README.md']
assert len(qfiles) == 100, len(qfiles)
for p in qfiles:
    txt = p.read_text(encoding='utf-8')
    m = re.search(r'^id:\s*(\d+)\s*$', txt, re.M)
    if not m:
        raise RuntimeError(f'missing id: {p}')
    qid = int(m.group(1))
    if qid not in PACKS:
        raise RuntimeError(f'missing enrichment for Q{qid:03d}')

    # Remove previous V2 block if rerunning.
    txt = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n*', '', txt, flags=re.S)

    # Version metadata.
    if not re.search(r'^edition:', txt, re.M):
        txt = txt.replace('source: "计算机网络面试100题_专业详解版_2026.pdf"\n',
                          'source: "计算机网络面试100题_专业详解版_2026.pdf"\nedition: "2.0-deep"\nupdated: "2026-09-02"\n')
    else:
        txt = re.sub(r'^edition:.*$', 'edition: "2.0-deep"', txt, flags=re.M)
        txt = re.sub(r'^updated:.*$', 'updated: "2026-09-02"', txt, flags=re.M)

    marker = '\n## 面试现场推荐回答结构\n'
    if marker not in txt:
        raise RuntimeError(f'anchor missing: {p}')
    block = f'\n{START}\n{PACKS[qid].strip()}\n{END}\n'
    txt = txt.replace(marker, block + marker, 1)
    p.write_text(txt, encoding='utf-8')

print(f'enriched {len(qfiles)} question files')
