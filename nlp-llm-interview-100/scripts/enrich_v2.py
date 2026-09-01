from pathlib import Path
import json, re, math, os
ROOT=Path(__file__).resolve().parents[1]
ITEMS=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
PACK=(ROOT/'data/deepdives_v2.mdpack').read_text(encoding='utf-8')
TODAY='2026-09-01'

# Parse @@Q001 blocks.
parts=re.split(r'(?m)^@@(Q\d{3})\s*$', PACK)
DEEP={}
for i in range(1,len(parts),2):
    DEEP[parts[i]]=parts[i+1].strip()

CHAPTER_ENG={
1:['写清随机变量、概率模型与 loss/metric 的区别。','涉及梯度时检查数值尺度、饱和、方差与优化器交互。','实验上至少做多 seed、slice 和 calibration/threshold 检查。'],
2:['给出状态/标签空间、独立性假设和训练/解码复杂度。','区分局部 score、全局归一化与解码约束。','真实 NLP 数据要考虑 OOV、标注规范、领域词典和 span 对齐。'],
3:['把表示学习与共现统计、上下文依赖和梯度路径联系起来。','比较时同时讨论参数量、并行性、长期依赖和数据效率。','用小型可控任务验证“长依赖/低频词/一词多义”等具体假设。'],
4:['明确 `[B,T,H,D]` 等 tensor shape、softmax axis、mask broadcast 与 dtype。','区分训练全序列、prefill 与 decode；后两者的资源瓶颈不同。','用 reference implementation 对拍 fused/optimized kernel，确保优化不改变语义。'],
5:['把训练目标与数据分布联系起来：哪些 token 产生监督、模型实际最大化什么。','比较 tokenizer/架构时给出序列长度、FLOPs、唯一 token、显存和推理代价。','预训练决策最终需要固定 compute/token 预算下的消融，而不是只看局部 loss。'],
6:['先明确 demonstration、preference、reward、rollout 分别来自哪里。','所有 reward/judge 都是代理目标，要讨论偏差、KL、reward hacking 和覆盖。','比较方法时同时算训练稳定性、采样成本、显存和在线数据需求。'],
7:['拆成 recall→rerank→generation，各层用不同指标和延迟预算。','检索系统必须同时考虑 index freshness、长尾实体、ANN recall 与线上 latency。','任何更强 reranker 都要回答每个 query 需要多少次模型前向。'],
8:['为每次过滤保留 reason code、score、阈值、版本和 provenance。','质量信号不是 ground truth，必须估计误删/漏删和长尾分布损失。','最终用 proxy training/downstream utility 验证数据决策。'],
9:['把 prefill/decode 分开做 FLOPs、显存、HBM bandwidth 和通信量账本。','系统优化需同时报告 TTFT、TPOT、throughput、峰值显存和质量损失。','先定位瓶颈是 compute-bound、memory-bound 还是 communication-bound，再选优化。'],
10:['先写 reference 版本和不变量，再写向量化/缓存/融合优化。','测试 shape、axis、dtype、device、极端值、padding/mask 与 cached/full consistency。','“代码能跑”不是正确性标准；必须有可自动化的数值对拍。']}


def split_sections(txt):
    m=re.search(r'(?m)^## 1\. 题目\s*$',txt)
    if not m: raise ValueError('section 1 missing')
    prefix=txt[:m.start()]
    body=txt[m.start():]
    ms=list(re.finditer(r'(?m)^## (\d+)\. ([^\n]+)\s*$',body))
    sec={}
    for i,x in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(body)
        sec[int(x.group(1))]=body[x.start():end].rstrip()
    return prefix,sec

def update_fm(prefix,minutes):
    if not prefix.startswith('---\n'): return prefix
    end=prefix.find('\n---\n',4)
    fm=prefix[4:end]; rest=prefix[end+5:]
    drop={'version','last_updated','reading_time','answer_depth'}
    lines=[]
    for ln in fm.splitlines():
        k=ln.split(':',1)[0].strip() if ':' in ln and not ln.startswith('  ') else ''
        if k not in drop: lines.append(ln)
    lines += ['version: "2.0"',f'last_updated: "{TODAY}"',f'reading_time: "{minutes} min"','answer_depth: "professional"']
    return '---\n'+'\n'.join(lines)+'\n---\n'+rest

def chapter_impl(ch):
    lines=['## 7. 实现、复杂度与工程验证','']
    for b in CHAPTER_ENG[ch]: lines.append(f'- {b}')
    lines += ['','### 推荐验证清单','',
              '- **Correctness**：与最小 reference/手算结果对拍。',
              '- **Numerics**：加入极端输入、低精度与长序列测试。',
              '- **Complexity**：同时写时间、空间以及关键系统资源。',
              '- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。',
              '- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。']
    return '\n'.join(lines)

def enrich_followup(sec9):
    # Keep original specific questions, remove generic v1 additions.
    lines=sec9.splitlines(); out=[]
    for ln in lines:
        if '如果把本题放到真实大规模系统里' in ln or '与本章相邻方法相比' in ln: continue
        out.append(ln)
    out += ['', '### 回答追问时的升级原则','',
            '1. 先给结论，再写一个关键公式 / shape / 数据流。',
            '2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。',
            '3. 给出一个“不适用”的条件，证明不是机械背诵。',
            '4. 若追问工程实现，优先说明验证方法和可观测指标。']
    return '\n'.join(out).rstrip()

def related(item):
    q=int(item['id'][1:]); qs=[]
    for z in [q-1,q+1]:
        if 1<=z<=100: qs.append(f'Q{z:03d}')
    # add concept jumps by chapter
    extras={1:['Q009','Q012'],2:['Q015','Q021'],3:['Q031','Q034'],4:['Q035','Q043','Q050'],5:['Q056','Q060'],6:['Q066','Q070','Q074'],7:['Q075','Q084'],8:['Q085','Q088'],9:['Q091','Q096'],10:['Q097','Q100']}[item['chapter']]
    for x in extras:
        if x!=item['id'] and x not in qs: qs.append(x)
    lookup={x['id']:x for x in ITEMS}
    lines=['## 12. 关联题目与知识网络','']
    for qid in qs[:5]:
        t=lookup[qid]
        rp=os.path.relpath(ROOT/t['path'],(ROOT/item['path']).parent).replace('\\','/')
        lines.append(f'- [{qid} {t["title"]}]({rp})')
    return '\n'.join(lines)

if set(DEEP)!=set(x['id'] for x in ITEMS):
    missing=sorted(set(x['id'] for x in ITEMS)-set(DEEP)); extra=sorted(set(DEEP)-set(x['id'] for x in ITEMS))
    raise SystemExit(f'deep dive pack mismatch missing={missing} extra={extra}')

for item in ITEMS:
    p=ROOT/item['path']; txt=p.read_text(encoding='utf-8'); prefix,sec=split_sections(txt)
    # section 6 is fully bespoke from pack
    s6='## 6. 专业深挖：原理、边界与工程\n\n'+DEEP[item['id']]
    s7=chapter_impl(item['chapter'])
    s8='\n'.join(ln for ln in sec[8].splitlines() if '回答只停留在名词解释' not in ln).rstrip()
    s9=enrich_followup(sec[9])
    s10=sec[10]
    s11=sec[11].split('\n---\n',1)[0].rstrip()
    s12=related(item)
    body='\n\n'.join([sec[i] for i in range(1,6)]+[s6,s7,s8,s9,s10,s11,s12])
    headline=next((ln[4:].strip() for ln in DEEP[item['id']].splitlines() if ln.startswith('### ')), item['title'])
    body += f'\n\n## 13. 一句话收束\n\n> **{headline}**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。\n'
    body += '\n---\n\n**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。\n'
    minutes=max(5,math.ceil(len(re.findall(r'[A-Za-z0-9_]+|[\u4e00-\u9fff]',body))/650))
    p.write_text(update_fm(prefix,minutes)+body,encoding='utf-8')

stats={'version':'2.0','questions':100,'deepdives':len(DEEP),'last_updated':TODAY,
       'total_question_chars':sum(len((ROOT/x['path']).read_text(encoding='utf-8')) for x in ITEMS)}
(ROOT/'data/build_stats_v2.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False,indent=2))
