#!/usr/bin/env python3
"""Randomly sample Redis interview questions from docs/question-index.json."""
from pathlib import Path
import argparse, json, random

ROOT = Path(__file__).resolve().parents[1]
INDEX = json.loads((ROOT / 'docs/question-index.json').read_text(encoding='utf-8'))

p = argparse.ArgumentParser(description='Random Redis interview quiz generator')
p.add_argument('-n', '--count', type=int, default=10)
p.add_argument('-c', '--chapter', type=int, choices=range(1, 11))
p.add_argument('-d', '--difficulty', help='substring match, e.g. 高级 / 基础 / 新版')
p.add_argument('--seed', type=int)
args = p.parse_args()

rows = INDEX
if args.chapter:
    rows = [x for x in rows if x['chapter'] == args.chapter]
if args.difficulty:
    rows = [x for x in rows if args.difficulty in x['difficulty']]
if not rows:
    raise SystemExit('No questions matched the filters.')

rng = random.Random(args.seed)
for x in rng.sample(rows, min(args.count, len(rows))):
    print(f"{x['id']}  {x['title']}  [{x['difficulty']}]  {x['path']}")
