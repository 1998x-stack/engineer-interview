#!/usr/bin/env python3
import argparse, json, random
from pathlib import Path
p=argparse.ArgumentParser(description='Random macroeconomics interview sampler')
p.add_argument('--count',type=int,default=10)
p.add_argument('--seed',type=int)
p.add_argument('--module',type=int,choices=range(1,11))
a=p.parse_args()
items=json.loads((Path(__file__).resolve().parents[1]/'data/questions.json').read_text(encoding='utf-8'))
if a.module: items=[x for x in items if x['module']==a.module]
r=random.Random(a.seed)
for x in r.sample(items,min(a.count,len(items))):
    print(f"{x['qid']}  {x['title']}  [{x['module_title']}] -> {x['path']}")
