#!/usr/bin/env python3
"""Engineering Signal static-site generator.
Reads every interview question .md (frontmatter + body) across the monorepo and
emits a navigable static site: overview -> 36 collections -> ~3,500 questions.
Run:  python3 site/build.py   (outputs into site/)
"""
import os, re, shutil, datetime
from html import escape
from collections import OrderedDict
import yaml
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")

MD = markdown.Markdown(extensions=["extra", "sane_lists", "md_in_html", "toc"])

# ------------------------------------------------------------------ metadata
META = {
 "agent-engineer-interview-100": dict(name="Agent Engineer", latin="AGENT RELIABILITY", cn="智能体工程",
   tagline="生产级智能体工程：Agent Loop、Multi-Agent、Context、RAG、Durable Execution、Eval 与可信执行层。",
   chips=["Agent Loop","Multi-Agent","Tools / MCP","Context / Memory","RAG","Eval","Security","System Design"], domain="核心基础"),
 "algorithm-interview-100": dict(name="Algorithm", latin="LEETCODE · PATTERNS", cn="算法",
   tagline="100 道母题 + 25+ 模式 + 工程化追问，覆盖数组、图、树、DP、区间与系统设计。",
   chips=["Arrays / Hash","Two-Pointers","Linked List","Heap","Graph","DP","String","Design"], domain="核心基础"),
 "cv-algorithm-interview-handbook-v2": dict(name="Computer Vision", latin="VISION", cn="计算机视觉",
   tagline="传统 CV 到视觉基础模型：检测、分割、OCR、生成式视觉、视频与 3D 多模态。",
   chips=["Detection","Segmentation","OCR","Foundation","Generative","Video"], domain="核心基础"),
 "deep-learning-interview-100": dict(name="Deep Learning", latin="DEEP LEARNING", cn="深度学习",
   tagline="网络结构、优化与归一化、序列建模、多模态、分布式训练与推理优化。",
   chips=["Foundations","Optimization","CNN","Seq","LLM","Multimodal","Distributed","Inference"], domain="核心基础"),
 "nlp-llm-interview-100": dict(name="NLP / LLM", latin="NLP & LLM", cn="NLP 与 LLM",
   tagline="搜索 / RAG、序列建模、预训练、对齐、数据评估、推理服务与工程调试。",
   chips=["Classical NLP","Sequence","RAG","Alignment","Data","Infra"], domain="核心基础"),
 "llm-pretraining-interview-100": dict(name="LLM Pre-Training", latin="PRE-TRAINING", cn="LLM 预训练",
   tagline="Data、Scaling Law、Tokenizer、分布式训练、MoE、长上下文与训练稳定。",
   chips=["Data","Scaling","Tokenizer","Distributed","MoE","Long-Context"], domain="LLM 生命周期"),
 "llm-post-training-offer": dict(name="LLM Post-Training", latin="POST-TRAINING", cn="LLM 后训练",
   tagline="SFT 数据、Reward Model、PPO/DPO/GRPO、Verifier、RL 系统与 Agentic RL。",
   chips=["SFT","Reward","PPO","DPO","GRPO","Verifier","Eval","Agentic RL"], domain="LLM 生命周期"),
 "llm-inference-interview-100-pro": dict(name="LLM Inference", latin="INFERENCE & DEPLOY", cn="LLM 推理",
   tagline="推理性能、KV Cache、量化、Batching、推测解码、MoE 与生产级推理系统（Professional 版）。",
   chips=["KV Cache","Attention","Quantization","Batching","Speculative","MoE","Serving"], domain="LLM 生命周期"),
 "memcached-interview-100": dict(name="Memcached", latin="SOURCE · CACHING", cn="缓存与源代码",
   tagline="源码穿透版：slab、hashtable、LRU/TTL、线程模型、一致性与高可用。",
   chips=["Architecture","Slab","Hashtable","LRU / TTL","Protocol","HA"], domain="系统基础设施"),
 "transformer-interview-100": dict(name="Transformer", latin="TRANSFORMER", cn="Transformer 架构",
   tagline="Attention、位置编码、LayerNorm、训练稳定、推理优化与系统设计。",
   chips=["Attention","Position","LayerNorm","Multi-Head","Training","Inference","System Design"], domain="核心基础"),
 "recsys_interview_100_repo": dict(name="Recommender Systems", latin="RECOMMENDER", cn="推荐系统",
   tagline="召回、双塔、精排、序列、多任务、实验、偏差、几个与生成式推荐。",
   chips=["Retrieval","Embedding","Ranking","Sequential","Multitask","Bias","Frontier"], domain="应用系统与推荐"),
 "search-engine-interview-100": dict(name="Search Engine", latin="SEARCH · IR", cn="搜索引擎",
   tagline="检索、倒排索引、BM25、Learning to Rank、ANN、混合检索与搜索系统设计。",
   chips=["IR","Inverted Index","BM25","LTR","ANN","RAG","Rerank"], domain="应用系统与推荐"),
 "JianZhi-Quant-Offer": dict(name="Quant Finance", latin="QUANTITATIVE", cn="金融量化",
   tagline="因子、回测、风控、Alpha、市场微观结构、高频交易与量化工程。",
   chips=["Factor","Backtest","Risk","Alpha","Microstructure","HFT"], domain="加密 / 金融工程"),
 "rl-interview-100-v2": dict(name="Reinforcement Learning", latin="REINFORCEMENT", cn="强化学习",
   tagline="MDP、价值方法、PPO、连续控制、离线 RL、RL 对齐与工程系统设计。",
   chips=["MDP","DQN","PPO","Continuous","Offline","RLHF"], domain="AI 前沿"),
 "embodied-ai-interview-100": dict(name="Embodied AI", latin="EMBODIED", cn="具身智能",
   tagline="感知、SLAM、规划与控制、模仿学习、Sim2Real、VLM/VLA 与 World Model。",
   chips=["Robotics","SLAM","Manipulation","RL","Sim2Real","VLA"], domain="AI 前沿"),
 "game-engine-interview-100": dict(name="Game Engine", latin="GAME ENGINE · GRAPHICS", cn="游戏引擎 / 图形",
   tagline="游戏引擎 / Graphics / Engine Programmer：C++ 对象模型、渲染管线、内存、数学与性能工程。",
   chips=["C++","Rendering","Memory","Math","Performance","Architecture"], domain="图形与游戏引擎"),
 "Data-Structures-Interview-100": dict(name="Data Structures", latin="DATA STRUCTURES", cn="数据结构",
   tagline="数组、链表、栈、队列、堆、树、哈希、并查集与进阶数据结构的面试深化。",
   chips=["Array","Linked List","Stack / Queue","Heap","Tree","Graph","Hash"], domain="系统基础设施"),
 "agent-harness-interview-100": dict(name="Agent Harness", latin="AGENT HARNESS", cn="Agent 工程 (Harness)",
   tagline="Agent Harness 工程师：Agent 运行时、工具、状态、可观测性与生产 Agent 系统。",
   chips=["Agent Loop","Tools","State","Observability","Eval","Security"], domain="AI 前沿"),
 "can-interview-offer": dict(name="CAN BUS / Automotive", latin="CAN · AUTOSAR", cn="车载嵌入式 / CAN",
   tagline="车载嵌入式、AUTOSAR/BSW、ECU 端到端验证与车机/IVI 测试题库。",
   chips=["CAN / FD","物理层","协议层","AUTOSAR","ECU 验证","测试"], domain="车载 / 嵌入式 / 控制"),
 "computer-network-interview-100": dict(name="Computer Network", latin="NETWORKING", cn="计算机网络",
   tagline="从协议原理到 Linux 网络栈与线上故障定位：TCP、HTTP、TLS、路由、NAT 与调优。",
   chips=["TCP/IP","HTTP","TLS","路由 / 交换","Linux 网络栈","排障"], domain="计算机基础"),
 "computer-organization-interview-100": dict(name="Computer Organization", latin="COMP ORGANIZATION", cn="计算机组成",
   tagline="数据表示、ISA、流水线、乱序执行、Cache、MMU/TLB、多核一致性与性能分析。",
   chips=["数据表示","ISA","流水线","Cache","MMU / TLB","一致性"], domain="计算机基础"),
 "control-theory-interview-100-v1.1.0": dict(name="Control Theory", latin="CONTROL", cn="控制论",
   tagline="经典到现代控制：传递函数、状态空间、PID、稳定性、鲁棒控制与工程直觉。",
   chips=["传递函数","状态空间","PID","稳定性","鲁棒控制","离散"], domain="车载 / 嵌入式 / 控制"),
 "crawler-anti-crawler-interview-100": dict(name="Crawler & Anti-Crawler", latin="CRAWLER", cn="爬虫与反爬",
   tagline="从 HTTP 语义到亿级 URL Frontier：Scrapy、策略、Bot Detection 与系统设计。",
   chips=["HTTP","Scrapy","URL 调度","Bot 检测","限流","分布式"], domain="数据 / 数据工程"),
 "cuda-programming-optimization-interview-100": dict(name="CUDA / GPU", latin="CUDA · GPU", cn="CUDA 编程优化",
   tagline="CUDA/GPU Kernel、内存模型、优化、Profiler、LLM Inference 与 GPU Compiler。",
   chips=["Kernel","内存模型","优化","Warp","Profiler","Inference"], domain="AI 前沿"),
 "high-school-math-olympiad-coach-interview": dict(name="HS Math Olympiad Coach", latin="MATH OLYMPIAD", cn="高中数学竞赛教练",
   tagline="面向重点高中/竞赛机构的高中数学竞赛教练岗面试题库。",
   chips=["数论","组合","代数","几何","教练法","强基"], domain="教育 / 学科竞赛"),
 "jianzhi-web3-offer-100": dict(name="Web3", latin="WEB3 · SOLIDITY", cn="Web3 / Solidity",
   tagline="Web3/区块链：Solidity、EVM、Security、DeFi、L2、AA、Solana 与系统设计。",
   chips=["Solidity","EVM","Security","DeFi","L2","AA"], domain="加密 / 金融工程"),
 "junior-math-competition-teacher-interview-100": dict(name="Junior Math Coach", latin="MATH COMPETITION", cn="初中数学竞赛教师",
   tagline="面向初中数学竞赛/数学思维/拔尖创新教师岗的系统面试题库。",
   chips=["代数","几何","数论","教学法","追问","Rubric"], domain="教育 / 学科竞赛"),
 "macroeconomics-interview-100": dict(name="Macroeconomics", latin="MACROECONOMICS", cn="宏观经济学",
   tagline="经济学复试/保研与宏观岗位面试：宏观模型、政策、增长与金融市场。",
   chips=["GDP","IS-LM","货币","通胀","增长","金融"], domain="经济 / 金融"),
 "microeconomics-interview-100": dict(name="Microeconomics", latin="MICROECONOMICS", cn="微观经济学",
   tagline="从会背定义到能在陌生 Case 建模、推导、反事实：供需、博弈、市场结构与契约理论的剑指式训练。",
   chips=["供需","弹性","博弈","市场结构","契约","反事实"], domain="经济 / 金融"),
 "network-security-interview-100": dict(name="Network Security", latin="NETWORK SECURITY", cn="网络安全",
   tagline="网络安全面试：加密、认证、防火墙、安全协议、渗透测试与工程实践。",
   chips=["加密","认证","防火墙","安全协议","渗透","SOC"], domain="网络安全"),
 "operating-system-interview-100": dict(name="Operating System", latin="OPERATING SYSTEM", cn="操作系统",
   tagline="操作系统 100 题：进程、线程、内存、调度、同步、文件系统与 Linux 工程化。",
   chips=["进程 / 线程","内存","调度","同步","文件系统","Linux"], domain="系统基础设施"),
 "python-interview-100": dict(name="Python", latin="PYTHON", cn="Python",
   tagline="Python 3.14：语言机制、并发、GC、异步、性能与工程题解。",
   chips=["语法机制","并发","GC","异步","性能","工程化"], domain="系统基础设施"),
 "redis-interview-100-offer-style-v2": dict(name="Redis", latin="REDIS · OFFER", cn="Redis",
   tagline="100 道 Redis 高频真题：数据结构、持久化、集群与缓存一致性的 Offer 风格。",
   chips=["数据结构","持久化","集群","复制","缓存","Sentinel"], domain="系统基础设施"),
 "sqlite-interview-100": dict(name="SQLite", latin="SQLITE", cn="SQLite",
   tagline="SQLite 深入原理：事务、WAL、B-Tree/Pager、Query Planner、索引与系统设计。",
   chips=["事务","WAL","B-Tree","Query","索引","FTS5"], domain="系统基础设施"),
 "time-series-interview-100": dict(name="Time Series", latin="TIME SERIES", cn="时间序列",
   tagline="统计建模与时序基础模型：ARIMA、状态空间、DeepTS、TSFM 与系统化面试。",
   chips=["ARIMA","状态空间","深度学习","TSFM","预测","工程"], domain="数据 / 数据工程"),
 "web-security-interview-100": dict(name="Web Security", latin="WEB SECURITY · APP", cn="Web 安全",
   tagline="Web Security / AppSec：注入、认证、OAuth、CSRF、供应链与渗透测试。",
   chips=["注入","认证","OAuth","CSRF","供应链","渗透"], domain="网络安全"),
}

# Collections that are not yet ready for the site (no question-source files yet).
# Keep their META entry so re-enabling is a one-line change once content lands.
SKIP_SLUGS = {"can-interview-offer"}

GLYPH = {
 "agent-engineer-interview-100": "A<sub>g</sub>", "algorithm-interview-100": "{ }",
 "cv-algorithm-interview-handbook-v2": "◍", "deep-learning-interview-100": "∂",
 "nlp-llm-interview-100": "Σ", "llm-pretraining-interview-100": "∑",
 "llm-post-training-offer": "→", "llm-inference-interview-100-pro": "⚡",
 "memcached-interview-100": "◫", "transformer-interview-100": "T", "recsys_interview_100_repo": "◎",
 "search-engine-interview-100": "⌕", "JianZhi-Quant-Offer": "Δ",
 "rl-interview-100-v2": "π", "embodied-ai-interview-100": "⇄", "game-engine-interview-100": "▣",
 "Data-Structures-Interview-100": "◇", "agent-harness-interview-100": "⟳", "can-interview-offer": "∿",
 "computer-network-interview-100": "⇆", "computer-organization-interview-100": "⚙",
 "control-theory-interview-100-v1.1.0": "ζ", "crawler-anti-crawler-interview-100": "≋",
 "cuda-programming-optimization-interview-100": "▦", "high-school-math-olympiad-coach-interview": "∑",
 "jianzhi-web3-offer-100": "λ", "junior-math-competition-teacher-interview-100": "∏",
 "macroeconomics-interview-100": "¥", "microeconomics-interview-100": "§", "network-security-interview-100": "◬",
 "operating-system-interview-100": "✷", "python-interview-100": "≥", "redis-interview-100-offer-style-v2": "◉",
 "sqlite-interview-100": "⊞", "time-series-interview-100": "≈", "web-security-interview-100": "✖",
}

DOMAIN_ORDER = ["核心基础", "LLM 生命周期", "应用系统与推荐", "AI 前沿", "系统基础设施", "计算机基础", "数据 / 数据工程", "网络安全", "加密 / 金融工程", "经济 / 金融", "车载 / 嵌入式 / 控制", "教育 / 学科竞赛", "图形与游戏引擎"]


# ------------------------------------------------------------------ helpers
def esc(x):
    return escape(str(x))


def slugify_id(x):
    return re.sub(r"[^A-Za-z0-9]+", "", str(x)) or "q"


def _tags(t):
    if isinstance(t, list):
        return [str(x) for x in t]
    if isinstance(t, str):
        return [x.strip() for x in t.split(",") if x.strip()]
    return []


def _nat(s):
    m = re.search(r"\d+", s or "")
    return int(m.group()) if m else 1e9


def parse_fm(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text.strip("\ufeff\n"), re.S)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm, m.group(2)


def clean_body(body):
    """Strip the leading H1 title (duplicated by page header) + prev/next nav line."""
    out, seen_title = [], False
    for l in body.split("\n"):
        s = l.strip()
        if not seen_title and s.startswith("# "):
            seen_title = True
            continue
        seen_title = True
        if s and not s.startswith("#") and s.startswith("[") and "](" in s \
                and ("←" in s or "→" in s or "总索引" in s or "返回目录" in s):
            continue
        out.append(l)
    return "\n".join(out)


# ------------------------------------------------------ resource link fixing
COPIES = {}  # absolute out path -> source absolute
LINK_RE = re.compile(r'(!?\[[^\]]*\]\()([^()\s]+)([^)]*\))')


def _rewrite_links(slug, src_abs, text):
    proj = os.path.join(ROOT, slug) + os.sep
    def _repl(m):
        prefix, url, suffix = m.group(1), m.group(2), m.group(3)
        if url.startswith(("http", "#", "mailto", "tel", "javascript", "/")) or url == "":
            return m.group(0)
        tgt = os.path.normpath(os.path.join(os.path.dirname(src_abs), re.sub(r"[#?].*", "", url)))
        if not tgt.startswith(proj) or not os.path.isfile(tgt):
            return m.group(0)
        rel = os.path.relpath(tgt, os.path.join(ROOT, slug))
        dest = os.path.normpath(os.path.join(OUT, slug, rel))
        COPIES[dest] = tgt
        return prefix + rel + suffix
    return LINK_RE.sub(_repl, text)


def collect(slug):
    base = os.path.join(ROOT, slug)
    records = []
    for dirpath, _, files in os.walk(base):
        for fn in files:
            if not fn.lower().endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8", errors="replace") as f:
                    raw = f.read()
            except Exception:
                continue
            fm, body = parse_fm(raw)
            if not body.strip() or "title" not in fm:
                continue
            if "id" in fm:
                fid = str(fm["id"]).strip()
            else:
                m = re.match(r"^\s*([A-Za-z]*\d+)\b", str(fm["title"]))
                fid = m.group(1) if m else "q{}".format(len(records) + 1)
            records.append(dict(id=fid, src=p,
                title=str(fm["title"]).strip().split("\n")[0],
                chapter=fm.get("chapter", fm.get("chapter_title", "—")),
                difficulty=fm.get("difficulty", "") or str(fm.get("level", "") or "") or str(fm.get("priority", "") or ""),
                tags=_tags(fm.get("tags")) or _tags(fm.get("type")) or _tags(fm.get("topics")),
                must=bool(fm.get("must_do") in (True, "true", "Yes") or str(fm.get("priority", "")).upper() in ("S", "P0")),
                frequency=str(fm.get("frequency", "")),
                body=body))
    records.sort(key=lambda r: (_nat(str(r["chapter"])), _nat(r["id"])))
    return records


def collect_all():
    out = {}
    for slug in os.listdir(ROOT):
        if not os.path.isdir(os.path.join(ROOT, slug)) or slug.startswith(".") or slug == "site":
            continue
        if slug in SKIP_SLUGS:
            continue
        recs = collect(slug)
        if recs:
            out[slug] = recs
    return out


ALL = collect_all()
NCOLL = len(ALL)
TOTAL = sum(len(v) for v in ALL.values())
TOTAL_STR = f"{TOTAL:,}"
PDFS = {}

def collect_pdfs(slug):
    """Copy each project's handbook PDF into site/<slug>/pdf/ (dedup by name)."""
    proj = os.path.join(ROOT, slug)
    outdir = os.path.join(OUT, slug, "pdf")
    os.makedirs(outdir, exist_ok=True)
    found, seen = [], set()
    for dirpath, _, fns in os.walk(proj):
        for f in fns:
            if f.lower().endswith(".pdf") and f not in seen:
                seen.add(f)
                dest = os.path.join(outdir, f)
                if not os.path.exists(dest) or \
                        os.path.getsize(dest) != os.path.getsize(os.path.join(dirpath, f)):
                    shutil.copyfile(os.path.join(dirpath, f), dest)
                found.append(f)
    PDFS[slug] = found


# ------------------------------------------------------------------- shells
def head(title, active="", base=""):
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} · Engineer Interview 100</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Public+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/site.css">
<script>document.documentElement.className += ' js';</script>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}},options:{{skipHtmlTags:['script','noscript','style','textarea','code','pre']}}}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head><body>
<header class="masthead"><div class="container">
  <a class="brand" href="{base}index.html"><span class="logo">∫<b>engineer</b>/100</span><span class="meta">—— interview corpus</span></a>
  <nav><a href="{base}index.html" class="{ 'on' if active=='overview' else ''}"><span>Overview</span></a></nav>
  <span class="count">{NCOLL} fields · ~{TOTAL} questions</span>
</div></header>
"""


def footer(base=""):
    y = datetime.date.today().year
    return f"""
<footer class="footline"><div class="container">
  <span class="mono">{y} · engineer-interview</span>
  <div class="r"><a href="https://github.com/1998x-stack/engineer-interview">GitHub</a><span class="mono">design: Engineering Signal</span></div>
</div></footer>
<script src="{base}assets/site.js"></script>
</body></html>"""


# ------------------------------------------------------------------ overview
def dot_matrix():
    """35 rows, one element each: a scale-bar whose fill = relative question
    count (relative to the largest collection, so variation is visible)."""
    counts = [len(recs) for recs in ALL.values()]
    mx = max(counts) if counts else 1
    rows = []
    for slug, recs in ALL.items():
        meta = META.get(slug, {})
        n = len(recs)
        pct = n / mx * 100
        rows.append(
            f'<div class="rowlabel" data-name="{esc(meta.get("name", slug))}" data-n="{n}">'
            f'<span>{esc(meta.get("name", slug))} <i>{n}</i></span>'
            f'<div class="rowbar" style="--fill:{pct:.1f}%"></div></div>'
        )
    return "\n".join(rows)


def card(slug):
    meta = META.get(slug, {})
    n = len(ALL[slug])
    chips = "".join(f'<span class="chip">{esc(c)}</span>' for c in meta.get("chips", [])[:5])
    g = GLYPH.get(slug, "•")
    return f"""
<a class="card reveal" href="{slug}/index.html">
  <div class="top"><span class="glyph">{g}</span><span class="tag">{esc(meta.get("latin",""))}</span></div>
  <h4>{esc(meta.get("name", slug))}</h4>
  <span class="cn" style="font-family:var(--font-mono);font-size:11px;color:var(--slate)">{esc(meta.get("cn",""))}</span>
  <p>{esc(meta.get("tagline",""))}</p>
  <div class="chips">{chips}</div>
  <div class="foot"><span class="q">{n} questions</span><span class="go">Open →</span></div>
</a>"""


def overview_page():
    doms = OrderedDict((d, []) for d in DOMAIN_ORDER)
    loose = []
    for slug in ALL:
        d = META.get(slug, {}).get("domain")
        if d in doms:
            doms[d].append(slug)
        else:
            loose.append(slug)
    sections = []
    for d, slist in doms.items():
        if slist:
            sections.append(f'<div class="domain"><h3><span class="ch">{esc(d)}</span></h3>'
                            f'<div class="grid">{"".join(card(s) for s in slist)}</div></div>')
    if loose:
        sections.append(f'<div class="domain"><h3><span class="ch">其他</span></h3>'
                        f'<div class="grid">{"".join(card(s) for s in loose)}</div></div>')
    total = sum(len(v) for v in ALL.values())
    body = f"""
<section class="hero"><div class="container">
  <div class="kicker"><span class="dot"></span> ENGINEERING SIGNAL — {NCOLL} fields · full interview corpus</div>
  <h1>Interview prep as a <span class="sig">knowledge structure</span>.</h1>
  <p class="lede">{TOTAL_STR} real questions across <code>{NCOLL}</code> disciplines — every one a markdown file, every one navigable. Built for serious candidates: <code>Know-What → Know-Why → Know-How → Trade-off → Production</code>.</p>
  <div class="rails reveal">
    <div class="rail on"><span class="n">01</span><span class="t">Know-What</span><span class="d">the map</span></div>
    <div class="rail"><span class="n">02</span><span class="t">Know-Why</span><span class="d">the reasoning</span></div>
    <div class="rail"><span class="n">03</span><span class="t">Know-How</span><span class="d">the skill</span></div>
    <div class="rail"><span class="n">04</span><span class="t">Trade-off</span><span class="d">the decision</span></div>
    <div class="rail"><span class="n">05</span><span class="t">Production</span><span class="d">the default</span></div>
  </div>
  <div class="actions reveal">
    <a class="btn primary" href="#fields">Browse the fields <span class="k">↗</span></a>
    <a class="btn ghost" href="https://github.com/1998x-stack/engineer-interview">View on GitHub</a>
  </div>
</div></section>

<section class="heatband"><div class="hdwrap">
  <div class="hd"><h2>{TOTAL_STR} questions, drawn to scale</h2><span class="sub">each row = one field · fill = question count</span></div>
  <p class="legend"><b>{total}</b> real questions · {len(ALL)} fields · hover a row</p>
  {dot_matrix()}
</div></section>

<section class="section" id="fields"><div class="container">
  <div class="sec-head reveal"><span class="eyebrow">The corpus</span>
    <h2>The <strong>fields</strong>, grouped by intent</h2>
    <span class="side">{len(ALL)} collections · {total} questions</span></div>
  {"".join(sections)}
</div></section>
"""
    return head("Overview", "overview") + body + footer()


# ---------------------------------------------------------------- collection
def collection_page(slug):
    recs = ALL[slug]
    meta = META.get(slug, {})
    chs = OrderedDict()
    for r in recs:
        chs.setdefault(r["chapter"], []).append(r)
    chapters_html = []
    for ci, (ch, items) in enumerate(chs.items(), 1):
        rows = []
        for r in items:
            pill = '<span class="pill answer">must-do</span>' if r["must"] else ""
            diff = f'<span class="pill topic">{esc(str(r["difficulty"]))}</span>' if r["difficulty"] else ""
            rows.append(f'<a class="qrow" href="{r["q"]}"><span class="dir">{esc(r["id"])}</span>'
                        f'<span class="tt">{esc(r["title"])}</span>{pill}{diff}</a>')
        chapters_html.append(
            f'<div class="qgroup"><div class="chapbar"><span class="no">{ci:02d}</span>'
            f'<span class="t">{esc(str(ch))}</span><span class="cnt">{len(items)} questions</span></div>'
            f'<div class="qlist">{"".join(rows)}</div></div>')
    statbar = f"""
    <div class="statbar">
      <div class="stat"><div class="v">{len(recs)}</div><div class="l">questions</div></div>
      <div class="stat"><div class="v">{len(chs)}</div><div class="l">chapters</div></div>
      <div class="stat"><div class="v">{sum(1 for r in recs if r["must"])}</div><div class="l">must-do</div></div>
      <div class="stat"><div class="v" style="font-size:15px">{esc(meta.get("latin",""))}</div><div class="l">field</div></div>
    </div>"""
    body = f"""
<section class="detail-head"><div class="container">
  <nav class="crumbs"><a href="../index.html">overview</a><i>∕</i><span>{esc(meta.get("name", slug))}</span></nav>
  <div class="latin">{esc(meta.get("latin",""))}</div>
  <h1 class="h1">{esc(meta.get("name", slug))}</h1>
  <p class="lede">{esc(meta.get("tagline",""))}</p>
  {statbar}
  <div class="taglist" style="margin-top:16px">{"".join(f'<a href="#">{esc(c)}</a>' for c in meta.get("chips", [])[:8])}</div>
</div></section>
{pdf_section(slug)}
<section class="section section--questions" id="questions"><div class="container">
  {"".join(chapters_html)}
</div></section>
"""
    return head(meta.get("name", slug), base="../") + body + footer("../")


# ---------------------------------------------------------------- question
def pdf_section(slug):
    pdfs = PDFS.get(slug, [])
    if not pdfs:
        return ""
    pdf = pdfs[0]
    buttons = "".join(
        f'<a class="btn ghost" href="pdf/{esc(p)}" target="_blank" rel="noopener">下载 {esc(p)}</a>' for p in pdfs)
    return f"""
<section class="section pdfband" id="pdf"><div class="container">
  <div class="sec-head"><span class="eyebrow">Handbook</span><h2>PDF <strong>手册</strong>, 在站内阅读</h2></div>
  <div class="pdf-card">
    <div class="pdf-actions">
      <button class="btn primary pdf-btn" data-pdf="pdf/{esc(pdf)}">在线预览 PDF <span class="k">⇣</span></button>
      {buttons}
    </div>
    <div class="pdf-wrap" hidden></div>
  </div>
</div></section>
"""


def question_page(slug, r, idx, total):
    MD.reset()
    content = MD.convert(clean_body(r["body"]))
    content = re.sub(r'<a href="[^"]*\.md[^"]*"[^>]*>\s*(.*?)\s*</a>',
                     r'<span class="srcref">\1</span>', content, flags=re.S)
    meta = META.get(slug, {})
    tags = "".join(f'<a href="#">{esc(t)}</a>' for t in r["tags"][:14])
    ps = ALL[slug]
    prev_html = f'<a href="{ps[idx-1]["q"]}">← {esc(ps[idx-1]["id"])}</a>' if idx > 0 else "<span></span>"
    next_html = f'<a href="{ps[idx+1]["q"]}">{esc(ps[idx+1]["id"])} →</a>' if idx + 1 < total else "<span></span>"
    body = f"""
<section class="crumbs" style="margin-top:26px"><div class="container">
  <a href="../index.html">overview</a><i>∕</i><a href="index.html">{esc(meta.get("name", slug))}</a><i>∕</i><span>{esc(r["id"])}</span>
</div></section>
<div class="container"><div class="q-wrap">
  <aside class="rail-col">
    <div class="mpanel"><h5>Spec</h5><div class="kv">
      <div class="row"><span class="k">id</span><span class="v">{esc(r["id"])}</span></div>
      <div class="row"><span class="k">difficulty</span><span class="v">{esc(str(r["difficulty"]))}</span></div>
      <div class="row"><span class="k">frequency</span><span class="v">{esc(r["frequency"]) or "—"}</span></div>
      <div class="row"><span class="k">must-do</span><span class="v">{"yes" if r["must"] else "—"}</span></div>
    </div>
    <div class="prevnext">{prev_html}{next_html}</div></div>
    <div class="mpanel"><h5>Tags</h5><div class="taglist">{tags}</div></div>
  </aside>
  <article class="article">
    <div class="countlatin" style="font-family:var(--font-mono);font-size:12px;color:var(--signal);letter-spacing:.1em;text-transform:uppercase">
      {esc(meta.get("latin",""))} · {idx+1} / {total}</div>
    <h1 class="qtitle">{esc(r["title"])}</h1>
    {content}
  </article>
</div></div>
"""
    return head(esc(r["title"]), base="../") + body + footer("../")


def build():
    os.makedirs(OUT, exist_ok=True)
    # prune stale generated collections not present in the source tree
    for d in os.listdir(OUT):
        p = os.path.join(OUT, d)
        if os.path.isdir(p) and d not in ALL and d != "assets":
            shutil.rmtree(p)
            print("pruned stale dir:", d)
    # assign per-question filenames
    for slug, recs in ALL.items():
        os.makedirs(os.path.join(OUT, slug), exist_ok=True)
        seen = {}
        for r in recs:
            base = slugify_id(r["id"])
            c = seen.get(base, 0)
            seen[base] = c + 1
            r["q"] = (base if c == 0 else f"{base}-{c}") + ".html"

    # rewrite in-body resource links + gather copies
    for slug in ALL:
        for r in ALL[slug]:
            r["body"] = _rewrite_links(slug, r["src"], r["body"])
    for dest, src in COPIES.items():
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(src, dest)
    print("copied %d referenced resources into the site" % len(COPIES))

    # ship one PDF per collection for in-site viewing
    for slug in ALL:
        collect_pdfs(slug)
    print("pdfs per collection:", {k: len(v) for k, v in PDFS.items() if v})

    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(overview_page())
    for slug in ALL:
        with open(os.path.join(OUT, slug, "index.html"), "w", encoding="utf-8") as f:
            f.write(collection_page(slug))
        total = len(ALL[slug])
        for idx, r in enumerate(ALL[slug]):
            with open(os.path.join(OUT, slug, r["q"]), "w", encoding="utf-8") as f:
                f.write(question_page(slug, r, idx, total))
    n = sum(len(v) for v in ALL.values())
    print(f"built site → {OUT}  ({len(ALL)} collections, {n} question pages)")


if __name__ == "__main__":
    build()