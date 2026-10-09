#!/usr/bin/env python3
from pathlib import Path
import re, statistics
ROOT = Path(__file__).resolve().parents[1]
qs = sorted((ROOT/"questions").glob("*/Q[0-9][0-9][0-9].md"))
required = [
    "## PDF 母版题解",
    "## GitHub 增强版：深度展开",
    "## 专业增强版 V2：从面试答案到 AppSec 工程",
    "### 8.1 威胁建模：先定义资产、主体与边界",
    "### 8.2 关键安全不变量：把最佳实践变成可测试规则",
    "### 8.3 失败链（Failure Chain）分析",
    "### 8.4 代码审计：从关键词搜索升级为数据流与控制流审计",
    "### 8.5 架构设计：控制应该放在哪里",
    "### 8.6 安全验证矩阵：如何证明“真的修好了”",
    "### 8.8 设计权衡：Senior/Staff 面试应该说什么",
    "### 8.10 面试回答分层",
]
issues=[]
sizes=[]
for p in qs:
    text=p.read_text(encoding="utf-8")
    sizes.append(len(text.encode("utf-8")))
    for h in required:
        if h not in text:
            issues.append(f"{p.relative_to(ROOT)} missing {h}")
    if "TODO" in text or "TBD" in text:
        issues.append(f"{p.relative_to(ROOT)} contains TODO/TBD")
    if text.count("```text") < 1:
        issues.append(f"{p.relative_to(ROOT)} missing conceptual diagram")
print(f"questions={len(qs)}")
print(f"bytes_total={sum(sizes):,}")
print(f"bytes_min={min(sizes):,}")
print(f"bytes_median={int(statistics.median(sizes)):,}")
print(f"bytes_max={max(sizes):,}")
if issues:
    print("QUALITY CHECK FAILED")
    for x in issues: print(" -", x)
    raise SystemExit(1)
print("QUALITY CHECK OK")
