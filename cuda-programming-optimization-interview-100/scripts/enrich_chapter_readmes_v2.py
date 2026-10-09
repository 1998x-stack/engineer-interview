from pathlib import Path
import re

ROOT=Path('/mnt/data/cuda-programming-optimization-interview-100')
QROOT=ROOT/'questions'
MARK='<!-- CHAPTER-PROFESSIONAL-V2 -->'

CH={
1: dict(prereq='C/C++ 基础、kernel launch 语法、线程索引。', model='软件抽象 Grid→Block→Thread 必须映射到硬件 GPU→SM→Warp。同步、分支、内存访问与 occupancy 的讨论都从这张映射图出发。', labs=['用不同 block size 测最后一个 partial warp','写 grid-stride loop 并控制 grid 大小','用 CUDA Event 与 host wall-clock 对比 kernel 计时'], mastery=['能解释 block 为什么不跨 SM','能区分 warp/block/device 同步','能从 grid/block 配置推测 waves 与并行度']),
2: dict(prereq='第 1 章执行模型；知道 global/shared/register 基本语法。', model='所有优化都可看成让数据尽量停留在更近、更可复用的层级，同时控制资源占用。重点区分 hardware-managed cache 与 software-managed storage。', labs=['测 register pressure→spill 拐点','shared reuse vs global reload','pinned/pageable/UM 三类 host-device 数据移动'], mastery=['能画完整 memory hierarchy','能解释 spill 为什么危险','能根据访问模式选择 constant/texture/UM/pinned']),
3: dict(prereq='Warp 概念、memory hierarchy、基本地址计算。', model='把一个 warp 的 32 个地址写出来，再计算覆盖多少 memory sectors；requested bytes 与 actual bytes 的比值是理解 coalescing 的最直接入口。', labs=['stride=1..64 memory microbenchmark','offset=0..31 misalignment sweep','AoS/SoA/AoSoA 对比'], mastery=['能口算连续 float 的 sector 数','能解释高 DRAM throughput 仍可能低效','能给 layout 重构方案']),
4: dict(prereq='第 1/3 章，尤其 warp 与地址模式。', model='Shared memory 先看 lane→bank 映射；控制流先看 lane→active mask；warp primitive 先看 participating mask。三者都以 warp 为基本分析单位。', labs=['shared stride bank-conflict sweep','32x32 vs 32x33 transpose','shared vs shuffle warp reduction'], mastery=['能推导 32-way conflict','能解释 broadcast 例外','能正确使用 shuffle mask 与 syncwarp']),
5: dict(prereq='执行模型、memory hierarchy、基本 profiler。', model='Occupancy 是资源约束的结果，不是目标。真正目标是足够 eligible work 隐藏 latency，同时保留 register/shared reuse 与 ILP。', labs=['动态 shared memory 控制 occupancy','unroll/register-pressure sweep','block-size autotune CSV'], mastery=['能写 residency min-formula','能解释 100% occupancy 反例','能从 spill/eligible warp 判断 register trade-off']),
6: dict(prereq='前五章全部基础；能独立写 CUDA kernel。', model='每道现场 coding 题都按 Correct→Coalesced→Reuse→Less Sync/Divergence→Warp Primitive→Architecture/Library Baseline 的版本演进回答。', labs=['Reduction V0-V5','Blelloch scan','shared histogram','optimized transpose','tiled GEMM'], mastery=['白板写出边界正确版本','每一版能说清减少了什么成本','知道何时停止手写并调用 CUB/cuBLAS']),
7: dict(prereq='Streams/events 基本 API、shared memory、barrier。', model='性能目标从“单 kernel 更快”升级为“让数据移动与计算流水重叠”。核心是 dependency graph、buffer ownership、stage/phase 与资源预算。', labs=['双 stream H2D-K-D2H overlap','1/2/3/4 stage pipeline sweep','fusion 前后 bytes/registers 对比'], mastery=['能区分 enqueue async 与真实 overlap','能画 pipeline prologue/steady/epilogue','能解释 TMA 与 cp.async 的角色差异']),
8: dict(prereq='至少完成 Q001-Q070；会使用命令行工具。', model='性能诊断必须走证据链：Systems 找热点与空洞→Roofline 分类→Compute counters 找机制→单变量实验证伪。不要从优化口诀出发。', labs=['建立 nsys→ncu 工作流','vector/GEMM roofline','构造三类 stall microbenchmark'], mastery=['能判断 memory/compute/latency/launch bound','能解释 SOL 不等于最优','能设计可重复 benchmark']),
9: dict(prereq='Tiling、async pipeline、Roofline、Tensor Core 基础。', model='GEMM 把多级数据复用、矩阵指令、software pipeline、warp specialization 与 scheduler 集成到一个 kernel。理解 CUTLASS 应从 mainloop/epilogue/layout/scheduler 四块拆解。', labs=['naive→tiled GEMM','CUTLASS profiler top-kernel 对比','small/skinny GEMM + split-K/Stream-K'], mastery=['能画 CTA/warp/MMA tile hierarchy','能解释 dtype 与 Tensor Core trade-off','能说清 persistent/warp-specialized/Stream-K']),
10: dict(prereq='第 7-9 章；能阅读 NVIDIA Programming/Tuning/CUTLASS 文档。', model='现代 CUDA 的重点是跨 block 协作、专用数据搬运和新 Tensor Core 数据路径：Cluster/DSM 扩大协作范围，TMA 负责 tensor transfer，TMEM/TCGen05 改变 Blackwell 计算与 accumulator workflow。', labs=['画 SM90 producer-consumer pipeline','对比 SM90/SM100 CUTLASS recipe','CUDA Graph microkernel replay','cudaMallocAsync memory-pool benchmark'], mastery=['能严格区分 TMA/TMEM','能解释 Blackwell 为什么不能照搬 Hopper','能用架构特性解决已证实瓶颈而非炫技']),
}

for d in sorted(p for p in QROOT.iterdir() if p.is_dir()):
    m=re.match(r'(\d{2})-',d.name)
    if not m: continue
    ch=int(m.group(1)); info=CH[ch]
    p=d/'README.md'; txt=p.read_text(encoding='utf-8')
    if MARK in txt: txt=txt.split(MARK)[0].rstrip()+"\n"
    questions=[]
    for qf in sorted(d.glob('q*.md')):
        qtxt=qf.read_text(encoding='utf-8')
        tm=re.search(r'^# (Q\d{3})｜(.+)$',qtxt,re.M)
        if tm: questions.append((tm.group(1),tm.group(2),qf.name))
    table='\n'.join(f'| {q} | [{title}]({fn}) |' for q,title,fn in questions)
    labs='\n'.join(f'{i+1}. {x}' for i,x in enumerate(info['labs']))
    mastery='\n'.join(f'- [ ] {x}' for x in info['mastery'])
    block=f'''\n{MARK}\n## 专业学习指南 V2\n\n### 前置能力\n\n{info['prereq']}\n\n### 本章核心因果模型\n\n{info['model']}\n\n### 推荐学习顺序\n\n```text\n概念定义\n  ↓\n白板地址/线程/数据流\n  ↓\n定量模型\n  ↓\n正确 baseline\n  ↓\n单变量优化\n  ↓\nNsight 证据\n  ↓\n架构迁移检查\n```\n\n### 必做实验\n\n{labs}\n\n### 掌握度检查\n\n{mastery}\n\n### 本章题目矩阵\n\n| # | Question |\n|---:|---|\n{table}\n\n### 面试训练方式\n\n- **第一遍**：每题只看标题，30 秒给结论。\n- **第二遍**：每题至少写一个公式或画一张数据流图。\n- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。\n- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。\n'''
    p.write_text(txt.rstrip()+"\n"+block,encoding='utf-8')
print('updated chapter READMEs')
