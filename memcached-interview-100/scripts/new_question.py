#!/usr/bin/env python3
"""Print a skeleton for a future interview question."""
import sys
num=int(sys.argv[1]); title=' '.join(sys.argv[2:]) or 'New question'
print(f"# 第 {num:03d} 题 · {title}\n\n## 题目\n\n## 30-90 秒标准回答\n\n## 深度机制\n\n## 源码导航\n\n## 常见易错点\n\n## 高频追问\n\n## 动手验证\n\n## 官方参考\n")
