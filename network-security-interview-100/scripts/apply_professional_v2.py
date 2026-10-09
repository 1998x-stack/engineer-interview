from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
index = json.loads((ROOT/'data/question-index.json').read_text(encoding='utf-8'))
by_id = {q['id']: q for q in index}

BEGIN='<!-- BEGIN PROFESSIONAL_V2 -->'
END='<!-- END PROFESSIONAL_V2 -->'

def bullets(items):
    return '\n'.join(f'- {x}' for x in items)

def numbered(items):
    return '\n'.join(f'{i}. {x}' for i,x in enumerate(items,1))

all_data={}
for p in sorted((ROOT/'data/enrichment').glob('chapter-*.json')):
    d=json.loads(p.read_text(encoding='utf-8'))
    all_data.update(d)

missing=[q for q in by_id if q not in all_data]
if missing:
    raise SystemExit(f'missing enrichment data: {missing}')

for qid, spec in all_data.items():
    q=by_id[qid]
    path=ROOT/q['path']
    text=path.read_text(encoding='utf-8')
    section=f'''{BEGIN}
## 专业深化 v2：面向高级工程师的题解

> 这一节是在 PDF 基线与第一轮扩展之上的第二层深化，重点补齐 **机制、边界、工程决策、证据、验证与追问树**。它不是利用手册，而是面向合法授权的安全工程与面试表达。

### A. 机制模型：先把问题抽象对

{bullets(spec['model'])}

### B. 成立条件、边界与典型失效模式

{bullets(spec['boundary'])}

### C. 工程设计：从“修一个点”到“设计控制面”

{bullets(spec['design'])}

### D. Detection & Evidence：如何证明你的判断

{bullets(spec['evidence'])}

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

{bullets(spec['validation'])}

### F. 面试追问树：把一题答成一棵知识树

{numbered(spec['deep_questions'])}

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

{spec['deliverable']}

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | {spec['summary']['root']} |
| 边界 | {spec['summary']['boundary']} |
| 主要控制 | {spec['summary']['control']} |
| 关键证据 | {spec['summary']['evidence']} |
| 验证 | {spec['summary']['verify']} |

{END}
'''
    if BEGIN in text:
        text=re.sub(re.escape(BEGIN)+r'.*?'+re.escape(END), section.strip(), text, flags=re.S)
    else:
        marker='\n## 复习卡片\n'
        if marker not in text:
            raise SystemExit(f'marker missing {path}')
        text=text.replace(marker, '\n'+section+'\n'+marker,1)
    text=re.sub(r'^status:\s*"?[^\n"]+"?\s*$', 'status: expanded-2026-v2', text, count=1, flags=re.M)
    path.write_text(text,encoding='utf-8')

print(f'applied professional v2 to {len(all_data)} questions')
