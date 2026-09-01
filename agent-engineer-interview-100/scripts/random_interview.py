#!/usr/bin/env python3
"""Sample questions for mock interviews."""
from pathlib import Path
import argparse,json,random
ROOT=Path(__file__).resolve().parents[1]
qs=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
ap=argparse.ArgumentParser(description='Random Agent interview question sampler')
ap.add_argument('--count',type=int,default=5)
ap.add_argument('--chapter',type=int,choices=range(1,11))
ap.add_argument('--difficulty',choices=['易','中','难'])
ap.add_argument('--frequency')
ap.add_argument('--priority20',action='store_true')
ap.add_argument('--seed',type=int)
args=ap.parse_args()
if args.chapter: qs=[q for q in qs if q['chapter_no']==args.chapter]
if args.difficulty: qs=[q for q in qs if q['diff']==args.difficulty]
if args.frequency: qs=[q for q in qs if q['freq']==args.frequency]
if args.priority20: qs=[q for q in qs if q['priority20']]
r=random.Random(args.seed)
for q in r.sample(qs,min(args.count,len(qs))):
    print(f"{q['id'].upper()} | {q['freq']} | {q['diff']} | {q['chapter']}")
    print(q['q'])
    print(q['path'])
    print('-'*72)
