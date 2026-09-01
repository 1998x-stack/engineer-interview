#!/usr/bin/env python3
from pathlib import Path
import re, sys, statistics
root=Path(__file__).resolve().parents[1]
qs=sorted(p for p in (root/'docs').glob('[0-9][0-9]-*/*.md') if p.name!='README.md')
err=[]; sizes=[]
required=['## 专家级展开（V2）','### A. 从第一性原理推导','### B. 关键源码符号与阅读顺序','### C. 边界条件与反例','### D. 生产故障推演','### E. 定量分析 / 可验证指标']
for p in qs:
    t=p.read_text(encoding='utf-8'); sizes.append(len(t))
    for h in required:
        if h not in t: err.append(f'{p}: missing {h}')
    if len(t)<5000: err.append(f'{p}: too thin ({len(t)} chars)')
# Detect the worst old generic boilerplate.
bad='先定义失败语义。 Memcached 是 Cache'
for p in qs:
    if bad in p.read_text(encoding='utf-8'): err.append(f'{p}: old generic production boilerplate remains')
if err:
    print('\n'.join('ERROR: '+e for e in err)); sys.exit(1)
print(f'OK: V2 expert sections present in {len(qs)} questions.')
print(f'Chars/question min={min(sizes)}, median={int(statistics.median(sizes))}, mean={int(statistics.mean(sizes))}, max={max(sizes)}')
