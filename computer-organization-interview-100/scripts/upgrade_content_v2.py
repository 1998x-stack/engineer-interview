from __future__ import annotations
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'assets/source/questions-from-pdf.json'
DOCS = ROOT / 'docs'
questions = json.loads(SRC.read_text(encoding='utf-8'))

CORE_FIX_PATH = ROOT / 'assets/source/pdf-core-corrections.json'
CORE_FIX = json.loads(CORE_FIX_PATH.read_text(encoding='utf-8')) if CORE_FIX_PATH.exists() else {}

# Locate existing filenames by QID so links remain stable.
qid_to_file = {}
for f in DOCS.glob('[0-9][0-9]-*/q*.md'):
    m = re.search(r'q(\d{3})', f.name)
    if m:
        qid_to_file[int(m.group(1))] = f

chapters = {
1: dict(slug='01-architecture-data', title='体系结构与数据表示',
       first='从“软件看到的抽象”与“硬件真正保存的位模式”之间建立映射：同一串 bit 在不同类型、端序、位宽与 ABI 下可能具有不同语义。',
       metrics='重点关注表示范围、编码空间利用率、对齐/访存代价与 ABI 可移植性。',
       diagram='''flowchart LR\nA[源程序中的值] --> B[编译器/ABI]\nB --> C[机器位模式]\nC --> D[寄存器/内存]\nD --> E[端序/对齐/类型解释]\nE --> F[程序可观察结果]''',
       refs=[('Intel SDM','https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html'),('IEEE 754','https://standards.ieee.org/ieee/754/6210/')]),
2: dict(slug='02-arithmetic-alu', title='运算器与计算机算术',
       first='把运算理解为“有限位宽上的布尔电路”，而不是无限精度数学。正确性来自编码规则、进位链、舍入规则与异常状态。',
       metrics='关注关键路径、组合逻辑深度、吞吐/延迟、溢出条件与舍入误差。',
       diagram='''flowchart LR\nA[输入操作数] --> B[编码/符号解释]\nB --> C[ALU/FPU 数据通路]\nC --> D[规格化/舍入/标志位]\nD --> E[有限位宽结果]''',
       refs=[('RISC-V ISA','https://docs.riscv.org/'),('Intel SDM','https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html')]),
3: dict(slug='03-isa-abi', title='ISA 与 ABI',
       first='ISA 是软件与处理器之间的架构契约；ABI 是已编译软件之间的二进制契约。面试时必须把“架构规定”与“某颗 CPU 的实现”分开。',
       metrics='关注编码密度、取指/译码带宽、寄存器压力、调用开销与兼容性。',
       diagram='''flowchart LR\nA[高级语言] --> B[编译器]\nB --> C[ABI]\nC --> D[ISA 指令]\nD --> E[微架构实现]\nE --> F[硬件执行]''',
       refs=[('RISC-V Specs','https://docs.riscv.org/'),('Intel SDM','https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html')]),
4: dict(slug='04-datapath-control', title='数据通路与控制',
       first='把一条指令拆成“数据如何流动”和“控制信号如何选择路径”。单周期、多周期与流水线的差异，本质是硬件资源复用和时序切分方式不同。',
       metrics='关注 critical path、clock period、CPI、资源复用与控制复杂度。',
       diagram='''flowchart LR\nPC --> IF[取指]\nIF --> ID[译码/读寄存器]\nID --> EX[执行/地址计算]\nEX --> MEM[访存]\nMEM --> WB[写回]\nWB --> RF[寄存器文件]''',
       refs=[('RISC-V Specs','https://docs.riscv.org/'),('Intel Optimization Manual','https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html')]),
5: dict(slug='05-pipeline-ooo', title='流水线、预测与乱序执行',
       first='现代高性能 CPU 的目标不是让单条指令“神奇地更快”，而是在保持架构语义的前提下同时容纳更多 in-flight work，挖掘 ILP 并隐藏长延迟。',
       metrics='关注 IPC、backend/frontend stall、branch-miss、ROB/RS/LSQ occupancy、依赖链与执行端口利用率。',
       diagram='''flowchart LR\nF[Fetch] --> D[Decode]\nD --> R[Rename]\nR --> Q[Dispatch/Issue]\nQ --> E[Execute]\nE --> C[Complete]\nC --> ROB[ROB]\nROB --> T[In-order Retire]\nB[Branch Predictor] --> F''',
       refs=[('Intel Optimization Manual','https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html'),('RISC-V Specs','https://docs.riscv.org/')]),
6: dict(slug='06-cache-memory', title='Cache 与存储层次',
       first='Cache 的本质是用有限的高速 SRAM 保存“未来最可能再次使用”的主存副本。所有设计都围绕命中率、命中延迟、带宽、容量与一致性开销做权衡。',
       metrics='关注 hit latency、miss rate、miss penalty、MPKI、AMAT、带宽、MLP 与 cache-line 利用率。',
       diagram='''flowchart LR\nA[Load/Store] --> L1[L1 Cache]\nL1 -->|miss| L2[L2]\nL2 -->|miss| LLC[LLC]\nLLC -->|miss| MC[Memory Controller]\nMC --> DRAM[DRAM]\nDRAM --> MC --> LLC --> L2 --> L1''',
       refs=[('Intel Optimization Manual','https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html'),('Intel SDM','https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html')]),
7: dict(slug='07-mmu-tlb', title='MMU、页表与 TLB',
       first='虚拟内存把“程序使用的地址空间”与“物理存储布局”解耦；TLB 则缓存翻译结果，避免每次访存都进行昂贵的多级页表遍历。',
       metrics='关注 TLB reach、DTLB/ITLB miss、page-walk latency、page size、缺页成本与 shootdown 开销。',
       diagram='''flowchart LR\nVA[Virtual Address] --> TLB{TLB hit?}\nTLB -->|yes| PA[Physical Address]\nTLB -->|no| PTW[Page-table Walk]\nPTW -->|valid| PA\nPTW -->|invalid| PF[Page Fault]\nPA --> C[Cache/Memory]''',
       refs=[('Arm Memory Management','https://developer.arm.com/documentation/101811/latest/'),('Intel SDM','https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html')]),
8: dict(slug='08-coherence-memory-model', title='多核一致性与内存模型',
       first='多核正确性有两个不同问题：同一 cache line 的副本如何保持 coherence，以及多个内存操作允许以什么顺序被其他核观察。前者不是后者的替代品。',
       metrics='关注 invalidation traffic、cache-line bouncing、atomic retry、barrier cost、scalability 与 NUMA/locality。',
       diagram='''flowchart LR\nC0[Core 0 Cache] <--> COH[Coherence Fabric]\nC1[Core 1 Cache] <--> COH\nCOH <--> LLC[LLC/Directory]\nC0 --> SB0[Store Buffer]\nC1 --> SB1[Store Buffer]\nSB0 --> MM[Memory Ordering]\nSB1 --> MM''',
       refs=[('RISC-V RVWMO','https://docs.riscv.org/reference/isa/unpriv/rvwmo.html'),('Arm Architecture','https://developer.arm.com/documentation')]),
9: dict(slug='09-io-dma-interconnect', title='I/O、DMA 与互连',
       first='I/O 的关键不是“CPU 会不会读设备”，而是如何在 CPU、设备、内存和互连之间高效且有序地移动控制信息与大块数据。',
       metrics='关注 interrupt rate、DMA throughput、descriptor depth、PCIe/AXI outstanding、IOMMU、cache maintenance 与 memory ordering。',
       diagram='''flowchart LR\nCPU[CPU] --> MMIO[MMIO/控制]\nCPU --> MEM[Memory]\nDEV[Device] --> DMA[DMA Engine]\nDMA <--> MEM\nDEV --> IRQ[Interrupt]\nIRQ --> CPU\nCPU <--> FAB[SoC/PCIe Fabric]\nDEV <--> FAB''',
       refs=[('Arm AMBA','https://developer.arm.com/Architectures/AMBA'),('PCI-SIG','https://pcisig.com/')]),
10: dict(slug='10-storage-boot-performance', title='存储、启动与综合性能',
       first='这一章把前面的部件重新串成系统：介质特性决定存储层设计，启动链决定可信执行起点，而性能定位要求把“慢”分解成可测量的硬件事件。',
       metrics='关注 IOPS/latency/bandwidth、write amplification、refresh、occupancy、SIMD/SIMT 利用率、PMU 事件与 roofline/瓶颈分类。',
       diagram='''flowchart LR\nRESET[Reset] --> FW[Firmware/BootROM]\nFW --> BL[Bootloader]\nBL --> K[Kernel]\nK --> APP[Application]\nAPP --> CPU[CPU/GPU]\nCPU --> MEM[Cache/DRAM]\nCPU --> IO[Storage/I-O]''',
       refs=[('Intel Optimization Manual','https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html'),('PCI-SIG','https://pcisig.com/')]),
}

# Question-specific deepening. Each item provides a unique mechanism, quantitative hook, boundary and engineering hook.
S = {
1:('程序存储思想让“指令”和“数据”都进入统一可寻址存储体系；现代瓶颈更准确地说是处理器执行吞吐与数据供给能力增长不匹配。','用 CPU Time=IC×CPI×Tclk 分解：即使计算 CPI 很低，只要大量周期消耗在 memory stall，总时间仍由存储层主导。','现代 L1 往往 I/D 分离，因此“纯粹单总线冯·诺依曼”只是教学模型。','用 perf/PMU 看 LLC miss、memory bandwidth、stall cycles，判断是真正 memory-bound 还是算力/前端瓶颈。'),
2:('严格 Harvard 关注的是指令/数据地址空间和访问通路的分离；现代通用 CPU 常只在靠近核心处做 I/D 分离，下层重新统一。','分离 I/D 允许同周期取指和数据访问，减少结构冲突；统一下层可共享容量。','“L1 分离”不等于“整个系统是 Harvard”；自修改代码还需要指令缓存同步。','嵌入式 MCU/DSP 常能看到更明显 Harvard 特征；调试 JIT/自修改代码时要关注 I-cache maintenance。'),
3:('位宽至少影响通用寄存器、指针/地址表达、ABI 和算术能力，但“64 位”并不意味着所有 C 类型都变成 64 位。','2^32=4GiB 是经典地址空间数量级；64 位 ISA 实际往往只实现部分虚拟地址位。','数据模型可为 LP64、LLP64 等；同一 64-bit ISA 上 long 的宽度不一定相同。','检查 sizeof(void*)、ABI 文档和编译目标，不要只凭 OS 名称判断数据布局。'),
4:('二进制不是数学上唯一方案，而是数字电路在噪声容限、器件数量、逻辑设计和存储稳定性上的工程最优折中。','n 个二值器件可表示 2^n 个状态；多值逻辑虽可提高单器件信息量，但判决裕量和电路复杂度上升。','现实中存储器内部会用多电平单元，但对处理器暴露的逻辑接口仍是 bit。','理解 NAND Flash MLC/TLC 能帮助说明“物理多电平”和“逻辑二进制”并不矛盾。'),
5:('端序只规定多字节对象的字节顺序，不改变单个字节内的 bit 编号语义，也不等于网络协议字段的位序。','0x12345678 在 little-endian 内存最低地址放 0x78；网络字节序传统上是 big-endian。','类型转换、序列化和未对齐访问要分开讨论；不能靠未定义行为写端序检测。','协议/文件格式必须显式规定 byte order；跨平台序列化应使用 htons/ntohl 或明确编码函数。'),
6:('补码通过把模 2^n 的加法与有符号整数表示统一，使加减法共享硬件，并让 0 只有一种编码。','n 位补码范围 [-2^(n-1), 2^(n-1)-1]；取负可写成 ~x+1，但最小负数例外。','C/C++ signed overflow 语义与“硬件自然回绕”不是一回事，不能混用语言层与硬件层结论。','编译器优化可能利用“有符号溢出未定义”假设；低层位运算常选无符号类型。'),
7:('补码范围不对称导致最小负数没有对应正数，因此 abs(INT_MIN) 在同宽有符号类型中不可表示。','32 位时 INT_MIN=-2^31，INT_MAX=2^31-1。','硬件 bit pattern 可回绕，但语言层可能把有符号溢出定义为 UB 或异常语义。','写边界处理时先扩展到更宽类型，或显式判断 INT_MIN。'),
8:('IEEE 754 把数拆成 sign、biased exponent、fraction，并为零、无穷、NaN、subnormal 预留编码。','float 正常数约有 24 位有效二进制精度，double 约 53 位；这决定相对精度数量级。','NaN payload、舍入模式、flush-to-zero 等可能依平台/控制寄存器。','数值代码需要同时关注表示误差、舍入模式、FMA 和 fast-math 编译选项。'),
9:('十进制 0.1 在二进制中无限循环，有限尾数只能存邻近可表示数，因此运算结果经历再次舍入。','比较浮点数更合理的是绝对/相对误差：|a-b| <= atol + rtol·max(|a|,|b|)。','“用 epsilon 比所有浮点数”也不对；误差尺度必须与问题域相关。','金融金额优先用定点/十进制定点语义；科学计算需设计误差预算。'),
10:('对齐让一个对象更可能在少量总线/Cache 事务内完成访问，并满足 ISA/ABI 对自然边界与原子性的要求。','若 4B 对象跨越 cache line/page，可能触发两次访问甚至复杂 fault 情况；padding 是布局换性能/兼容性的结果。','x86 支持很多 unaligned access，但“支持”不代表所有跨界场景都无代价。','用 sizeof/alignof/offsetof 验证结构体布局；高性能结构要同时权衡 padding 与 cache footprint。'),
11:('减法在 n 位机器上可转为 A + (~B) + 1，本质利用补码的模 2^n 代数。','SUB 的加法器输入可复用 ADD 数据通路，只需反相 B 并设置 carry-in。','标志位解释要区分 borrow/carry 约定，不同 ISA 的 condition flags 定义可能不同。','阅读汇编时理解 CMP 常等价“做减法但不保存结果”，只更新条件码。'),
12:('Carry 描述无符号位宽外进位；Overflow 描述有符号结果超出补码范围，它们是同一加法器的不同解释。','有符号加法溢出条件：两个操作数同号且结果异号；无符号则看最高位 carry-out。','减法的 borrow/carry 语义在不同 ISA 中命名方向可能不同。','写编译器/加密/多精度算术时要准确区分 carry chain 与 signed overflow。'),
13:('ALU 常覆盖加减、逻辑、移位、比较；乘除、浮点、向量往往由独立执行单元承担。','ALU 的关键不是功能列表，而是 latency、throughput、端口数量和旁路网络。','某 ISA 有某条指令不代表它由“单个 ALU”一步完成，可能分解成 µops。','性能调优要看执行端口和依赖链，不应只数源码中的“算术操作”。'),
14:('比较通常复用减法/比较逻辑，但 signed 与 unsigned 的判定条件不同：前者要考虑符号与溢出，后者关注 carry/borrow。','补码 signed less-than 不能简单只看结果最高位，发生 overflow 时需修正。','ISA 可以提供直接比较指令，也可能通过 flags+branch 组合实现。','排查排序/边界 bug 时尤其注意把 size_t 与 int 混比导致的 unsigned 转换。'),
15:('左移 k 位在无溢出且语义允许时等价乘 2^k，但位宽截断和语言规则会破坏这种数学等价。','无符号 n 位左移本质对 2^n 取模；signed 左移的语言语义更严格。','编译器会自动 strength reduction，不必手工把所有乘法改成移位。','只有在位语义明确、性能数据支持时才手写位技巧。'),
16:('逻辑右移高位补 0，算术右移复制符号扩展，目的是分别保持无符号位模式和有符号数近似除 2 的语义。','对负数算术右移的舍入方向与语言/ISA 语义相关，不能简单等同数学除法。','某些语言对负 signed right shift 规定与 ISA 不同或历史上实现定义。','位运算跨语言/跨编译器时，用无符号类型最可控。'),
17:('乘法需要生成并压缩多个 partial products；高性能实现常使用 Booth 编码、carry-save 压缩树，再做最终进位传播。','位宽翻倍会显著增加部分积网络面积和时序压力，乘法单元通常比简单 ALU 更昂贵。','现代 CPU 的整数 MUL 可能完全流水化，latency 高但 throughput 可很好。','向量/矩阵硬件会通过大量 MAC 单元提高吞吐而非单次乘法延迟。'),
18:('整数除法依赖前一步余数/商估计，天然序列依赖更强，因此难像乘法那样高效做大规模树形并行。','硬件可能用 digit recurrence 或 reciprocal approximation；不同 operand 值还可能导致可变 latency。','常数除法常被编译器改写为乘法+移位，不能从源码 DIV 推断最终指令。','用反汇编/性能计数器确认真正瓶颈，尤其在热点循环中。'),
19:('浮点加法必须先对阶，再做 significand 加减，随后规格化与舍入；指数差过大时小数可能完全被吞掉。','误差关键来自 alignment shift 与 rounding；(a+b)+c 与 a+(b+c) 一般不等价。','FMA 只做一次最终舍入，因此数值结果可能比拆成 MUL+ADD 更精确。','数值算法优化不能只追求指令数，还要评估稳定性与可重复性。'),
20:('Infinity 让溢出与除零能继续传播，NaN 表达无效/未定义结果，subnormal 提供 gradual underflow 让接近 0 的数不突然跳零。','subnormal 精度逐渐下降但保持连续性；部分硬件/模式会 FTZ/DAZ 以换取性能。','NaN 比较具有特殊语义：通常与任何数（含自身）的有序比较都为 false。','高性能数值库要明确是否允许 flush-to-zero，避免平台差异。'),
21:('ISA 定义软件可见状态和指令语义；微架构决定如何实现这些语义，例如 pipeline 深度、ROB 大小、cache 结构都不属于 ISA 保证。','同一 x86-64 指令可在不同 CPU 上具有完全不同 µop 数、latency 和 throughput。','不要把某代 Intel/AMD 的实现细节写成 x86 架构规则。','优化时先守 ISA/ABI 正确性，再通过目标 CPU 手册/benchmark 做微架构调优。'),
22:('RISC/CISC 是历史设计取向而非现代性能标签；现代核心常把复杂 ISA 解码成更规则的内部操作。','固定/规则编码有利于前端并行译码；高代码密度则能减轻 I-cache 和 fetch 带宽压力。','Arm/RISC-V 也可能有压缩指令扩展，x86 也能在内部使用 RISC-like µops。','讨论时聚焦 load/store、编码、寄存器、译码与兼容性，不要说“RISC 一定更快”。'),
23:('Load/Store 架构把内存访问集中到 load/store 指令，使算术执行端与地址生成/内存系统职责更清晰。','典型 ADD 只读写寄存器；内存操作由 AGU/LSU 计算地址并访问 cache。','“只有 load/store 访问内存”是架构层规则，不代表实现中没有预取/页表遍历等隐式内存活动。','阅读 RISC-V/Arm 汇编时，数组和结构体性能常由 load/store 地址模式决定。'),
24:('寻址方式决定有效地址如何由寄存器、立即数和位移组合；Base+Offset 与栈帧、结构体字段、数组分块天然匹配。','EA = base + sign/zero-extended offset 是常见形式；复杂 ISA 还可支持 index×scale。','寻址“复杂”不一定更慢，取决于 AGU 能力和 µop 分解。','性能分析时关注地址生成端口、依赖链和是否产生额外 LEA/ADD。'),
25:('固定长度简化取指边界识别与并行译码；可变长度提高代码密度但增加前端切分、预译码和译码复杂度。','前端每周期可获取/译码的字节数和指令数共同限制 IPC。','压缩指令能改善 I-cache，但可能带来额外解码路径，不是单向收益。','用 I-cache miss、frontend bound 和 code size 共同评估编码密度价值。'),
26:('PC 是控制流的架构锚点；流水线前端围绕 predicted next PC 连续取指，真正结果稍后验证。','顺序路径通常 PC+len；分支/异常/返回会重定向前端。','现代 CPU 内部可能同时跟踪多个候选/恢复 PC，不能把单一寄存器模型当实现细节。','理解 PC 重定向有助于解释 branch mispredict flush 和 precise exception。'),
27:('函数调用由 ABI 规定参数、返回地址、栈帧和寄存器保存规则，再由 CALL/JAL/branch 等 ISA 机制实现。','调用开销包括控制流改变、可能的栈访问、寄存器 spill/fill，以及间接调用预测成本。','inline 可消除调用开销但会增加代码体积与 I-cache 压力。','用反汇编检查 tail call、inlining、frame pointer 与 spill，而不是只看源码。'),
28:('caller/callee-saved 是 ABI 在“每次调用都保存”和“只在需要时保存”之间做的责任分工。','叶函数往往能只用 caller-saved 而完全不建复杂栈帧；寄存器压力高时 spill 增多。','保存规则不是 ISA 固有属性，同一 ISA 不同 ABI 可不同。','跨语言 FFI、手写汇编、context switch 时必须严格遵守 ABI 保存集合。'),
29:('特权级用硬件阻止低权限代码执行敏感指令或访问受保护资源，是 OS 隔离与虚拟化的基础。','权限检查会出现在指令执行、页表权限和系统寄存器访问等多个位置。','Ring/EL 名称是具体 ISA 术语，不能跨架构机械对照。','漏洞分析要区分“软件逻辑权限”与“硬件特权/页表隔离”。'),
30:('ISA 保证机器指令语义；ABI 进一步约束函数调用、数据布局、符号和二进制接口，使独立编译模块能互操作。','同 ISA 上换 ABI 可能让二进制互不兼容，但源代码重新编译仍可工作。','编译器选项会影响 ABI（如 calling convention、packing），不是所有差异都能链接兼容。','FFI/动态库问题优先检查 ABI，不要先怀疑 CPU 指令。'),
31:('五级 IF-ID-EX-MEM-WB 是教学抽象；现代处理器通常还有 decode/rename/dispatch/issue/retire 等阶段。','关键是理解每阶段生产/消费什么状态，以及依赖、异常和控制流何时被确定。','不要把“五级”当现代 CPU 固定实现。','画出一条 load 和一条 dependent ALU 的生命周期，比背阶段名称更有说服力。'),
32:('寄存器可分架构寄存器和微架构物理寄存器；PC/SP/status/control register 的可见性与权限由 ISA 定义。','物理寄存器数量可大于架构寄存器，以支持 renaming 和更多 in-flight 指令。','MAR/MDR/IR 是教学抽象，不一定以同名硬件结构存在。','看 ISA 手册确认软件可见寄存器，看微架构资料理解内部 PRF/rename。'),
33:('控制器根据 opcode、当前状态和比较结果生成选择信号，使数据在寄存器、ALU、存储器和多路器之间走正确路径。','组合控制可快速直接；状态机/微码可把复杂指令拆成多步。','现代 OoO 控制远超简单“一个控制器”，包含分布式队列、调度和恢复逻辑。','学习时先用简单 datapath 建因果，再扩展到真实前后端。'),
34:('硬布线把控制逻辑直接编码进电路，速度高但修改成本大；微程序把复杂控制序列存成可更新的微指令。','微码可修复部分复杂指令行为/安全问题，但不是所有处理器都对所有指令使用微码。','“CISC=微码、RISC=硬布线”是过度简化。','关注复杂指令、微码更新与漏洞缓解时，理解这一层特别重要。'),
35:('单周期 CPU 的时钟周期必须覆盖最慢指令整条组合路径，导致简单指令也被迫等待最长路径。','Tclk >= max(path delay)；性能=IC×1×Tclk，CPI 虽是 1 但 Tclk 很大。','单周期不等于“每条指令现实中更快”，只是教学上 CPI=1。','这是解释“为什么需要多周期/流水线”的关键过渡题。'),
36:('多周期把一条指令拆成若干较短阶段并复用硬件，因此时钟可更短，不同指令也可使用不同周期数。','CPU Time=IC×CPI×Tclk：多周期牺牲 CPI，换更短 Tclk 和较少重复硬件。','多周期仍没有跨指令重叠，因此吞吐提升有限。','面试要能顺势引出 pipeline：进一步把不同指令的不同阶段重叠。'),
37:('流水线主要提高 steady-state throughput，而不是必然缩短单条指令 latency；额外 pipeline register 甚至可能增加单条延迟。','理想 k 级流水线处理 N 条任务约需 k+N-1 个周期，而非 Nk。','hazard、flush、stage imbalance 会让理想加速失效。','区分 latency/throughput 是理解 SIMD、GPU、存储和网络性能的通用能力。'),
38:('频率只是 Tclk 的倒数，最终性能还取决于 IC 与 CPI/IPC；高频设计可能因更深流水线和更高功耗带来副作用。','CPU Time=IC×CPI/frequency。','不同 ISA/编译器让 IC 不同，不同工作负载让 CPI 不同，因此 GHz 不能横比。','用 benchmark+PMU，而不是规格表频率判断真实应用性能。'),
39:('CPI/IPC 是吞吐统计，不等于单条指令 latency；超标量 CPU 可每周期 retire 多条指令，因此 IPC>1 很正常。','IPC=retired instructions / cycles；CPI 是其倒数仅在相同统计口径下成立。','包含 sleep/频率变化/SMT 时，指标解释要更谨慎。','把 IPC 与 stall 分类结合，才能知道低 IPC 是前端、后端还是内存问题。'),
40:('Latency 关注单个依赖结果多久可用，Throughput 关注单位时间可启动/完成多少独立操作；现代流水执行可做到高 latency 但高 throughput。','若 MUL latency=4 cyc、throughput=1/cyc，4 条独立 MUL 可流水重叠；依赖链则仍受 4 cyc 支配。','只看单指令 latency 无法预测独立并行 workload。','微基准应分别构造 dependency chain 和 independent streams 测两种指标。'),
41:('结构、数据、控制三类 hazard 分别对应资源冲突、依赖未满足和下一 PC 不确定；现代 OoO 只是用更复杂机制缓解，不会让这些约束消失。','stall CPI 可视为 base CPI 加各种 hazard penalty。','缓存 miss 等长延迟常通过 OoO/MLP 隐藏，不一定直接表现为固定 bubble 数。','分析 pipeline 要先画生产者/消费者和资源时间线。'),
42:('RAW 是真正的数据流依赖；WAR/WAW 属于寄存器名字复用造成的 false/name dependency，可通过 renaming 消除。','若 I2 必须读 I1 写出的值，RAW 无法“重命名掉”；只能调度或等待。','内存依赖还有更复杂的 load/store alias，不属于简单寄存器 RAW/WAR/WAW。','编译器调度和 OoO 调度都围绕 dependency graph 工作。'),
43:('forwarding 让结果从产生阶段直接送给消费者，绕过“必须先写回寄存器再读出”的不必要等待。','ALU→ALU 往往可下一周期旁路；旁路网络越复杂，面积、功耗和时序压力越大。','forwarding 不能创造尚未产生的数据，因此 load-use 仍可能 stall。','画 EX/MEM/WB 时间线能最直观解释哪些依赖可旁路。'),
44:('load 的真正数据往往到 cache lookup 后才可用，而下一条依赖指令可能更早需要 operand，产生时间缺口。','经典五级流水线常需 1-cycle bubble；现代 CPU 可通过 OoO 执行其他独立指令隐藏这段延迟。','L1 miss 时延迟可从几个 cycle 扩展到几十/几百 cycle，问题不再是固定 1 bubble。','优化热点时增加 ILP、software pipelining 或改变数据布局比“消除一条 load”更实际。'),
45:('分支在条件/目标解析前让 next PC 不确定；若等待结果再取指，深流水线会严重空转。','branch penalty≈mispredict rate×mispredict cost，可转化为 CPI 增量。','无条件 direct branch 目标通常更容易预测，但 indirect/return 也有专门预测结构。','用 branch-misses/branches 与 frontend stall 证实是否为控制流瓶颈。'),
46:('预测器至少要预测方向和目标，现代前端还要识别 call/return、indirect target，并维持历史信息。','BTB 负责目标缓存，方向预测器利用局部/全局历史，RAS 常辅助 return。','具体预测算法高度微架构相关，不属于 ISA。','性能优化上常通过减少不可预测分支、提高布局局部性或使用 if-conversion 改善。'),
47:('错误路径指令已经占用 fetch/decode/rename/执行资源；发现错误后必须 squash 年轻指令并恢复正确 rename/control state。','penalty 与“预测发现得有多晚”以及前端重新供给速度相关。','mispredict cost 不是简单等于 pipeline stage 数，真实实现更复杂。','高熵分支即使每次只做很少工作，也可能成为热点性能杀手。'),
48:('OoO 把“程序顺序”与“执行顺序”解耦：只要操作数/资源就绪，独立的年轻指令可先执行；最终仍受 retirement/一致性约束。','性能收益来自暴露 ILP 与隐藏 cache/multiply 等 latency；窗口大小受 ROB/RS/PRF/LSQ 限制。','OoO 不能越过真正数据依赖，也不能无限隐藏内存带宽瓶颈。','PMU 中 backend bound、ROB stalls、memory-level parallelism 能辅助判断 OoO 是否吃满。'),
49:('rename 将架构寄存器名映射到不同物理寄存器版本，使互不依赖的写不再因同名产生 WAR/WAW。','每次写架构寄存器分配新 physical reg；commit 后旧版本才可回收。','rename 不消除 RAW；rename table/checkpoint 恢复本身也有成本。','理解 rename 是理解 speculative execution、ROB、PRF 生命周期的核心。'),
50:('ROB 记录程序顺序中的 in-flight 指令并在头部有序 retire，使乱序执行仍可呈现 precise architectural state。','ROB 满会阻止继续分配/rename，形成 backpressure；可见性能上表现为窗口不足。','结果值可能主要存 PRF，ROB 不一定保存所有 value；实现差异很大。','区分 ROB、RS/issue queue、PRF、LSQ：一个管提交顺序，一个管待执行，一个管值，一个管内存顺序。'),
51:('Cache 依赖 temporal/spatial locality：程序访问分布若可预测，就能用小容量高速存储命中多数访问。','AMAT=hit time+miss rate×miss penalty；只要 miss penalty 巨大，少量 miss rate 变化也可能显著。','流式一次性访问可能几乎没有 temporal locality，cache 甚至会被污染。','用 cache miss/MPKI、working-set 与访问 stride 评估是否值得做 blocking/tiling。'),
52:('容量变大意味着更长的 tag/data array、更多布线和更复杂相联比较，因此 latency 通常上升；层级化是在容量与延迟之间折中。','L1 追求极低 latency，LLC 更重容量/共享；层级平均代价用递归 AMAT 衡量。','具体“L1几周期、L3几十周期”依 CPU，不应写死。','优化时先判断 miss 落到哪一级，而不是笼统说“cache miss”。'),
53:('cache line 是一致性与传输的基本块；64B 常见是空间局部性、tag 开销、总线突发与误取/false-sharing 的折中。','line 越大：tag 开销下降、顺序访问收益增大，但 miss transfer 与 false sharing 可能变严重。','不是所有处理器都 64B，软件不应无条件硬编码。','做 padding/预取/数据布局前先查目标平台 cache line 或用硬件干扰大小接口。'),
54:('offset 选 line 内字节，index 选 set，tag 区分映射到同一 set 的不同内存块。','若 line=64B→offset=6bit；sets=C/(line×ways)，index=log2(sets)。','VIPT 场景还要考虑 index bits 是否落在 page offset 内以避免别名复杂度。','面试计算题要先写容量、相联度、line size，再推 sets/index/tag。'),
55:('相联度越高越能降低 conflict miss，但并行 tag 比较、mux 和替换状态更复杂，命中延迟/功耗可能增加。','direct-mapped=1-way；fully associative=1 set；N-way 是两者折中。','提升 ways 对 capacity miss 无能为力。','用 conflict-heavy 微基准或硬件计数器判断是否真受组冲突影响。'),
56:('3C 把 miss 根因分成 compulsory、capacity、conflict；多核还常额外讨论 coherence miss。','冷启动首访是 compulsory；工作集大于 cache 是 capacity；映射碰撞是 conflict。','真实硬件有预取、inclusive/exclusive、victim cache，使严格归因更复杂。','优化策略应匹配类型：blocking 针对容量，布局/相联度针对冲突，预取针对部分 compulsory/streaming。'),
57:('精确 LRU 需要维护 set 内所有 way 的全序，ways 增大后状态更新和关键路径成本快速上升。','N-way 精确 LRU 需要表达大量相对次序；PLRU/RRIP 用更低成本近似未来复用。','替换策略只在 miss 且需要 victim 时起作用，不能解决所有缓存问题。','现代 CPU 具体策略常不公开，优化应基于访问模式而非假设“硬件一定 LRU”。'),
58:('write-through 简化下层可见性但增加写流量；write-back 用 dirty line 合并多次写，显著降低带宽压力。','write-back eviction 若 dirty 需额外写回，可能占用 fill/writeback buffer。','coherence 系统中“写回到哪里”可能是下层 cache 而非直接 DRAM。','分析 store-heavy workload 时要看 store buffer、writeback traffic 和内存带宽。'),
59:('write-allocate 在写 miss 时先把 line 拉入 cache，适合之后还会继续写/读；no-write-allocate 适合流式写以避免污染。','write-back+write-allocate 是常见组合；write-through+no-write-allocate 也是经典组合，但并非绝对。','non-temporal store 可绕开常规 cache 路径，语义和平台实现需具体看。','大块初始化/拷贝可研究 streaming store，但必须 benchmark。'),
60:('AMAT 把局部命中与逐级 miss penalty 统一为期望值，是判断某个 hit-rate 优化是否值得的基础模型。','L1+L2：AMAT=T1+MR1·(T2+MR2·PenaltyMem)。','AMAT 只描述平均延迟，无法完整表达 MLP、带宽饱和和排队效应。','真实性能还应结合 MPKI、MLP、bandwidth 和 stalled cycles。'),
61:('虚拟地址提供隔离、稀疏地址空间、共享和重定位，让每个进程看到相对稳定的逻辑布局。','地址空间大小由 VA bits 决定，实际物理内存远小于虚拟空间。','虚拟内存不等于“磁盘交换”；即使完全不 swap，也需要地址翻译和权限。','mmap、共享库、ASLR、COW 都建立在虚拟内存抽象上。'),
62:('MMU 做 VA→PA 翻译并检查访问权限/属性；page table 是软件维护的数据结构，TLB/page-walker 是硬件加速路径。','页偏移不参与翻译；VPN 经过页表映射到 PPN，再拼接 offset。','不同 ISA 的页表格式、权限位和硬件/软件 page walk 机制不同。','驱动/内核调试要结合 page table、TLB 和 memory attribute 一起看。'),
63:('TLB 缓存近期页表翻译，相当于地址翻译路径上的专用 cache；其有效覆盖范围可用 TLB reach 描述。','TLB reach≈entries×page size；大页直接扩大 reach。','TLB miss 不表示页面不存在，只表示 translation cache 未命中。','大数据库/模型推理可通过 huge page 降 DTLB miss，但要权衡碎片。'),
64:('TLB miss 是硬件缓存 miss，通常由 page walk 解决；page fault 是页表语义无法完成当前访问，需要进入 OS。','一次 TLB miss 可能触发多级页表访存，而 page fault 可能涉及分配、IO、COW，成本差几个数量级。','permission fault 也属于 page fault/exception 范畴，不一定是“页面被换出”。','perf 中区分 dTLB-load-misses 与 major/minor faults，避免把两者混为一谈。'),
65:('多级页表用树结构只为实际使用的 VA 区域分配下级表，利用地址空间稀疏性节省内存。','单级页表项数≈VA空间/page size；48-bit VA、4KiB 页若全展开会非常巨大。','多级页表节省空间但增加 walk 深度；TLB 是抵消该延迟的关键。','页表层数、页大小和大页支持必须以具体 ISA/OS 为准。'),
66:('一次 load 同时穿过“执行调度、地址生成、地址翻译、cache 层级、可能的 DRAM”和最终写回/唤醒消费者。','L1 hit 与 DRAM miss 的 latency 可相差数量级；OoO 通过 MLP 隐藏部分长延迟。','真实实现中 TLB lookup 与 L1 indexing 可部分并行，不能机械串行化。','这是综合题：回答应能顺带提 LSQ、TLB、VIPT、cache miss、page fault。'),
67:('从架构语义看最终必须得到物理地址/属性；从微架构时序看 VIPT 可用 page offset 同时启动 L1 index 与 TLB lookup。','若 cache index 完全位于 page offset 内，可在翻译完成前安全选择 set，随后用 physical tag 校验。','不同 cache level 可能采用不同索引/标记策略。','高分答案必须区分 logical dependency 与 overlapped implementation。'),
68:('VIVT 快但有 homonym/synonym；PIPT 简单一致但受翻译延迟；VIPT 试图并行 TLB 与 L1 lookup，兼顾延迟与别名控制。','VIPT 常要求 set index bits 不越过 page offset，约束 L1 容量/ways 组合。','ASID/PCID 等可缓解部分 VIVT homonym/TLB context 问题，但实现细节不同。','理解 VIPT 能解释为什么 page size、L1 size、associativity 之间存在结构性关系。'),
69:('Huge page 通过扩大单个 translation 覆盖范围减少 TLB miss/page walk，也可能降低页表内存开销。','2MiB 相比 4KiB 覆盖放大 512×；相同 TLB entries 可映射更多地址。','代价包括内部碎片、分配/迁移困难、COW 粒度变大。','数据库/大模型常受益，但必须用 DTLB miss、page faults 和 RSS 验证。'),
70:('页表更新后，旧 translation 可能仍缓存于本核/其他核 TLB；必须 invalidate 并建立正确同步顺序。','多核 shootdown 常涉及 IPI/广播和等待 acknowledgement，线程数增大时会很贵。','并非每次页表更新都要全局 flush；ASID/PCID 和精细 invalidation 可降低成本。','高频 mmap/mprotect/unmap 场景可被 shootdown 开销限制扩展性。'),
71:('每核私有 cache 会复制同一内存块；coherence 协议保证对同一位置的写在多核间以一致方式传播/失效。','写共享 line 通常需要获取独占/修改权限，导致 invalidation traffic。','coherence 不等于所有内存操作严格程序序可见。','共享计数器/锁热点可通过 cache-line bouncing 直接体现 coherence 成本。'),
72:('MESI 用 M/E/S/I 表示 line 的脏/独占/共享/无效状态，核心目标是减少不必要内存访问并维护单写多读语义。','E→M 可本地升级；S→M 通常需要 invalidation 其他 sharers。','真实协议常是 MESIF/MOESI/目录协议等扩展，不要说所有 CPU 只有 MESI。','画一次 read miss、第二核 read、第一核 write 的状态转移，是最有效面试演示。'),
73:('coherence 约束单个地址的写传播/序列；consistency 约束多个地址上的 load/store 允许以什么顺序被其他线程观察。','即使每个地址都 coherent，也可能出现 store buffer 导致的跨地址重排现象。','语言内存模型（C++/Java）还位于 ISA 内存模型之上，不能直接互换。','并发 bug 分析要先问：是 data race、ordering 还是 coherence/false sharing 性能问题。'),
74:('MESI 解决副本一致，不保证程序顺序；store buffer、speculation、OoO 会让其他核观察到不同顺序，因此需要 fence/acquire/release。','barrier 约束的是 ordering/completion 范围，通常不是“清空所有 cache”。','不同 fence 强度和作用域差异很大，过度使用会损害性能。','无锁代码应优先使用语言级原子 memory order，再理解其如何映射到 ISA fence。'),
75:('x86 通常提供更强的默认内存顺序，而 Arm/RISC-V 允许更积极重排，以换取实现自由度和性能/功耗空间。','同一无锁算法在不同 ISA 上需要不同 fence/atomic mapping，但语言层可通过编译器统一。','“x86 强内存模型=完全顺序一致”不准确。','跨平台并发代码不要依赖偶然的 x86 行为。'),
76:('DMB 主要建立数据访问顺序，DSB 还等待相关操作完成，ISB 重新同步后续指令获取/执行上下文。','系统寄存器/页表/设备配置常需要正确 barrier 序列；选择过强 barrier 会增加 pipeline 等待。','具体 domain/shareability 参数是 Arm 架构细节，不能只背三个缩写。','驱动和内核代码中 barrier 错误常表现为极难复现的设备/多核 bug。'),
77:('false sharing 是不同线程写不同变量，但变量处于同一 coherence granule/cache line，导致 line ownership 在核间来回迁移。','如果两个核交替写同一 64B line，哪怕各写 8B，也可能每次都触发 invalidation/transfer。','只读共享一般不会产生同样的 ping-pong；关键是写入与 line 粒度。','用 perf c2c、HITM 等工具/事件可定位 cache-line bouncing。'),
78:('解决 false sharing 的核心是改变数据布局或写入归属，让高频独立写落到不同 line；padding 只是其中一种方法。','per-thread shard/local aggregation 常比简单 padding 更可扩展，最终再 reduce。','盲目 alignas(64) 会增加 footprint，可能反而伤害 cache/TLB。','先定位热点 line，再决定 padding、AoS→SoA、分片或减少共享写。'),
79:('原子 RMW 依赖 cache coherence 获取 line 的独占修改权，并由 ISA 提供 CAS/LL-SC/AMO 等原子语义。','无竞争原子可能很快；高竞争时 line 在核间反复迁移，性能随线程数恶化。','原子性不等于顺序一致，仍需正确 memory order。','锁自由算法性能要看 retry、contention、NUMA 和 false sharing，而不是只看“没有 mutex”。'),
80:('ABA 指值经历 A→B→A，CAS 只比较当前值因此误以为未改变；本质是“状态版本信息丢失”。','常见缓解：tagged pointer/version counter、hazard pointers、epoch reclamation 等。','版本号也可能回绕；内存回收问题常与 ABA 交织。','面试中不要只说“加锁”，要解释版本化或安全内存回收为何有效。'),
81:('中断把“设备事件到来”变成异步通知，让 CPU 不必持续轮询；但每次中断也有 entry/exit、cache/TLB 干扰与调度成本。','低频事件适合 interrupt，高包速网络常采用 interrupt moderation + polling/NAPI 类混合。','中断并不天然比 polling 延迟低，在极高频场景可能相反。','选择机制要看事件率、延迟 SLO 和 CPU 利用率。'),
82:('interrupt 通常来自异步外设，exception 由当前指令同步触发；trap 术语在 ISA/OS 中定义不同，回答时应说明上下文。','page fault、illegal instruction 是同步 exception；timer interrupt 是异步。','不要把软件 syscall 一律叫“trap”而不说明具体架构。','内核调试时准确区分 fault/abort/interrupt 有助于定位重启语义。'),
83:('异常/中断向量把事件类型映射到处理入口，并让硬件以定义好的方式保存必要上下文、切换权限/栈或读取向量表。','向量化减少软件逐个判断中断源的开销，但具体表结构依 ISA。','x86 IDT、Arm vector table 的格式完全不同，不应混讲。','写启动代码/裸机系统时，向量表位置、对齐、权限是首要检查项。'),
84:('polling 用持续检查换低路径复杂度和可预测性；interrupt 用异步通知节省空闲 CPU，但事件太密集会形成 interrupt storm。','存在 break-even event rate：超过后 polling/batching 更划算。','忙轮询还可能借助 CPU affinity、cache locality 获得极低 latency。','高性能网络/存储经常采用自适应 polling、batching 与中断合并。'),
85:('DMA engine 根据 CPU 配置的 descriptor 在设备与内存之间搬数据，CPU 主要负责建立 buffer、地址、长度、ownership 并处理完成通知。','吞吐取决于 burst、outstanding、IOMMU、内存带宽与设备链路，而不是 CPU memcpy 性能。','DMA 不等于“完全不占系统资源”；仍占互连和 DRAM bandwidth。','理解 ring descriptor、doorbell、completion queue 是网卡/NVMe 驱动基础。'),
86:('非 coherent DMA 可能绕过 CPU cache：CPU dirty line 未写回时设备读旧 DRAM，设备写新 DRAM 后 CPU 又可能命中旧 cache line。','CPU→device 前常需 clean/writeback；device→CPU 后常需 invalidate，具体 API/方向依平台。','coherent DMA 平台可由硬件维护一致性，但仍要遵守 ownership/order。','驱动代码应使用 OS DMA API，而不是手工假设 cache 行为。'),
87:('MMIO 把设备控制寄存器映射进地址空间，但其访问有 side effect、顺序和宽度要求，不能像普通 WB cacheable RAM 随意合并/重排。','memory attribute 决定 Device/Strongly-ordered/uncacheable 等行为；具体术语依 ISA。','volatile 只解决编译器层可见访问，不自动提供多核/设备所需的所有硬件 barrier。','驱动必须使用 readl/writel 等平台抽象并遵循设备手册时序。'),
88:('地址/数据/控制线是共享总线教学模型；现代 SoC 更像 packetized/interconnect network，含多主设备、仲裁、ID、QoS、clock-domain crossing。','带宽≈传输宽度×频率×有效利用率，但 outstanding/仲裁/协议开销决定实际值。','不能用“地址线数量=物理针脚数量”解释片上 NoC。','AXI/NoC 性能问题通常看 channel backpressure、outstanding 和 arbitration。'),
89:('AHB 是较简单的共享/流水总线风格；AXI 把读写拆成独立通道并支持多 outstanding、ID 和更高并发。','AXI 五通道常见：AR/R/AW/W/B；握手基于 VALID/READY。','AXI 版本/子集很多，Lite 与 full AXI 能力差异大。','SoC 性能调优要定位是地址通道、数据通道还是响应/背压限制。'),
90:('PCIe 用 point-to-point serial lanes 和 packet transaction 取代共享并行总线，以提高频率、扩展性、信号完整性和拓扑灵活性。','x16 由多 lane 聚合；实际吞吐受 generation、编码效率、协议/TLP 开销和 payload size 影响。','“串行一定比并行慢”是错误直觉：更高频率与 lane aggregation 可提供更高总带宽。','GPU/NVMe 性能要同时看 PCIe link width/speed、NUMA/root complex 和 DMA。'),
91:('SRAM cell 快且无需 refresh，但面积大；DRAM 以电容存 bit 密度高但读取破坏性、需 refresh，适合大容量主存。','cache 的价值不仅是介质快，还因位置靠近核心、banking/端口和小容量低延迟。','现代 cache 也可能使用不同 SRAM/eDRAM 技术，不能绝对化。','理解介质特性是解释层次化存储成本曲线的基础。'),
92:('DRAM 电容会漏电，因此控制器必须周期刷新；refresh 占用 bank/rank 时间并影响 tail latency。','refresh interval 与温度/器件规格相关；容量增加会让 refresh 管理更重要。','并非 CPU 软件定时逐行刷新，通常由内存控制器/DRAM 机制管理。','高实时性/大内存系统要关注 refresh 对延迟抖动的影响。'),
93:('HDD 的机械寻道/旋转延迟让随机 IO 昂贵；SSD 没有机械部件，随机读取更快，但受 NAND page/block、控制器和队列影响。','HDD 适合大顺序带宽/低成本容量；SSD 随机 IOPS 高，但写入受 FTL/GC 限制。','SSD 也不是“没有延迟”，队列、GC、thermal throttling 都可显著影响尾延迟。','压测应分 sequential/random、read/write、queue depth 和 block size。'),
94:('NAND erase granularity 大于 program/read page，更新小块数据常需搬迁有效页、擦除整块，再重写，从而产生写放大。','WA=physical NAND bytes written / host bytes written；>1 会同时降低性能与寿命。','host filesystem WA 与 device internal WA 是不同层次。','TRIM、over-provisioning、顺序写与 FTL 策略都会影响 WA。'),
95:('CPU 优先低延迟、复杂控制与单线程性能；GPU 用更多执行单元和线程上下文换吞吐，通过 massive parallelism 隐藏 latency。','GPU 性能常受 occupancy、memory coalescing、warp divergence 和 bandwidth 限制。','GPU 不等于“很多简单 CPU core”；执行模型、memory hierarchy 与调度方式不同。','判断任务是否适合 GPU，要看并行度、算术强度、数据搬运成本和控制流。'),
96:('SIMD 是“一条向量指令操作多个数据 lane”的 ISA/执行抽象；SIMT 向程序员暴露很多线程，硬件以 warp/wavefront 成组执行。','divergence 让同一 warp 的不同分支路径串行化，降低有效 lane 利用率。','CPU 也可有 SIMD，GPU 也不只 SIMT；概念不能按设备类型硬绑定。','优化向量/核函数时分别看 vectorization efficiency 与 warp occupancy/divergence。'),
97:('Reset 后 CPU 从架构定义的入口开始执行固件；BootROM/firmware 建立最小可信环境，加载下一阶段 bootloader，初始化 DRAM/设备并最终跳入 kernel。','多阶段启动用更小可信根逐步加载更复杂软件；Secure Boot 还会增加签名验证链。','PC 与 SoC 启动流程差异巨大，不应只背 BIOS→OS。','调试“上电不启动”要按 reset vector、clock、SRAM/DRAM、镜像加载、异常向量逐层定位。'),
98:('hardware prefetch 根据 stride/stream/history 猜未来访问并提前发请求，目标是把 memory latency 与计算重叠。','收益取决于 accuracy、coverage、timeliness；错误 prefetch 会浪费带宽并污染 cache。','prefetcher 算法高度微架构相关，软件通常无法假设固定策略。','用 bandwidth、LLC miss、prefetch events 和 workload 对照实验判断是否有效。'),
99:('顺序遍历同时利用 cache line 空间局部性、硬件 prefetch、TLB locality 和 DRAM row/burst 行为；随机访问会破坏这些机制。','64B line 若元素 8B，可一次 fill 带来 8 个连续元素；随机访问可能每个 line 只用 1 个元素。','若数据完全驻留 L1，小规模随机与顺序差距可能显著缩小。','数组布局、blocking、SoA/AoS 与数据压缩都围绕提高每次内存传输的有效工作量。'),
100:('系统定位必须先把“慢”转成可测量假设，再按 frontend、execution、memory、translation、coherence、bandwidth/IO 分层排除。','CPU Time=IC×CPI/f；CPI 再拆 branch、cache/TLB、dependency 等 stall。可辅以 Roofline 判断 compute/bandwidth bound。','单个指标不能定罪，例如 LLC miss 高但被 MLP 隐藏时未必是主瓶颈。','建立基线→采 PMU→构造微基准/对照→验证优化，是比“凭经验改代码”更专业的流程。'),
}

# Chapter-level architecture notes and code snippets.
ARCH_NOTES = {
1:'本章多数结论属于数据表示/ABI 共性；涉及对象布局、signed overflow、unaligned access 时，要明确区分语言标准、ABI 与 ISA。',
2:'算术电路的架构可见结果由 ISA 定义，内部 adder/multiplier/divider/FPU 结构则是微架构实现。',
3:'回答时优先引用“ISA 规定什么、ABI 规定什么、微架构自由实现什么”这三个层级。',
4:'五级流水线只是教学模型；真实 CPU 可有更多阶段，阶段边界和旁路时序依微架构。',
5:'分支预测器、ROB/RS/PRF 大小、µop 数、执行端口都不是 ISA 保证；优化必须针对具体 CPU。',
6:'Cache line size、层级包含关系、replacement policy、latency 都可能变化；只有内存一致性/ISA 可见语义是软件真正依赖的边界。',
7:'页表格式、ASID/PCID、page size、TLB 结构依 ISA/OS；“虚拟地址→翻译→物理访问”是共性模型。',
8:'语言内存模型、ISA 内存模型、cache coherence 是三层不同契约；跨层推理必须明确桥接关系。',
9:'I/O memory attributes、DMA coherence、IOMMU、AXI/PCIe revision 都是平台相关；驱动应依赖 OS/平台抽象。',
10:'存储与加速器性能高度依具体介质和平台；面试应给机制和指标，而不是背固定延迟数字。',
}

CODE = {
1:'''```c\n#include <stdint.h>\n#include <stddef.h>\n// 用 sizeof/alignof/offsetof 验证“语言对象 → ABI 布局”，不要凭感觉猜。\n```''',
2:'''```text\nA - B  ==  A + (~B) + 1   (mod 2^n)\n\n性能题：分别构造 dependent chain 与 independent ops，区分 latency / throughput。\n```''',
3:'''```asm\n# 伪汇编：参数寄存器/返回地址/栈布局由 ABI 定义\ncall target\n# ISA 只定义指令语义，不定义所有语言级调用细节\n```''',
4:'''```text\nIF → ID → EX → MEM → WB\n\n先用这一教学模型解释数据流，再说明现代 CPU 会继续拆成 rename/issue/retire 等阶段。\n```''',
5:'''```text\nprogram order: I1 → I2 → I3 → I4\nexecute order: I1 → I3 → I4 → I2   (若依赖/资源允许)\nretire order : I1 → I2 → I3 → I4\n```''',
6:'''```text\naddress = [ tag | set index | block offset ]\nsets = capacity / (line_size × ways)\nAMAT = hit_time + miss_rate × miss_penalty\n```''',
7:'''```text\nVA = [ VPN | page offset ]\nTLB/page table: VPN → PPN\nPA = [ PPN | page offset ]\n```''',
8:'''```cpp\n// 语言级同步是首选接口；编译器再映射到目标 ISA 的原子/屏障。\nstd::atomic<int> flag{0};\n```''',
9:'''```text\nCPU --MMIO--> device control\ndevice --DMA--> memory\ndevice --IRQ--> CPU\n\n控制面与数据面应分开理解。\n```''',
10:'''```text\nmeasure → classify → hypothesize → change one variable → re-measure\n\n“性能优化”首先是一套实验方法，而不是技巧列表。\n```''',
}


def rel_link(src: Path, dst: Path) -> str:
    import os
    return Path(os.path.relpath(dst, src.parent)).as_posix()


def parse_bullets(text: str):
    parts=[]
    for line in text.splitlines():
        line=line.strip()
        if not line: continue
        line=re.sub(r'^[•\-*]\s*','',line)
        parts.append(line)
    return parts


def chapter_of(qid:int): return (qid-1)//10+1

for q in questions:
    qid=q['id']; ch=chapter_of(qid); c=chapters[ch]
    f=qid_to_file[qid]
    mechanism, quant, boundary, engineering = S[qid]
    deep_bullets=parse_bullets(q.get('deep',''))
    pdf_core = CORE_FIX.get(str(qid), q.get('core') or q.get('recap',''))
    stars=q['difficulty']; diff_num=stars.count('★')
    prev_link=next_link=''
    if qid>1:
        pf=qid_to_file[qid-1]; prev_link=f"[← Q{qid-1:03d} {questions[qid-2]['title']}]({rel_link(f,pf)})"
    if qid<100:
        nf=qid_to_file[qid+1]; next_link=f"[Q{qid+1:03d} {questions[qid]['title']} →]({rel_link(f,nf)})"
    nav=' · '.join(x for x in [prev_link,next_link] if x)
    pdf_link=rel_link(f, DOCS/'assets/pdf/计算机组成原理面试100题_专业详解版.pdf')+f'#page={q["page"]}'
    related=[]
    for rid in [max((ch-1)*10+1,qid-2), max((ch-1)*10+1,qid-1), min(ch*10,qid+1), min(ch*10,qid+2)]:
        if rid!=qid and rid not in related: related.append(rid)
    related_lines='\n'.join(f"- [Q{rid:03d}｜{questions[rid-1]['title']}]({rel_link(f,qid_to_file[rid])})" for rid in related)
    refs='\n'.join(f'- [{name}]({url})' for name,url in c['refs'])
    deep_md='\n'.join(f'- {b}' for b in deep_bullets) or '- 原 PDF 本页未提供额外分点。'
    follow=q.get('followups','').strip()
    gotcha=q.get('gotcha','').strip()

    text=f'''---
id: Q{qid:03d}
title: "{q['title'].replace('"','\\"')}"
chapter: {ch}
chapter_title: "{c['title']}"
difficulty: {diff_num}
frequency: "{q['frequency']}"
pdf_page: {q['page']}
tags: ["{c['title']}", "{q['frequency']}", "Q{qid:03d}"]
content_version: "2.0-deep"
---

# Q{qid:03d}｜{q['title']}

> **来源与边界**：`PDF 核心内容` 忠实保留原 PDF 第 {q['page']} 页的结论、解析与易错点；从“第一性原理推导”开始属于 **GitHub v2 深度增强内容**，用于把题目扩展到现代 CPU/SoC、工程性能与连续追问。具体 ISA/微架构参数以目标处理器官方文档为准。  
> [查看原 PDF 对应页]({pdf_link})

| 项目 | 内容 |
|---|---|
| 难度 | {stars} |
| 频率 | {q['frequency']} |
| 模块 | {c['title']} |
| PDF 页码 | {q['page']} |
| 原 PDF 考察点 | {q['exam_points']} |
| GitHub v2 目标 | 从“会背定义”升级到“能推导、能量化、能定位工程问题” |

## 0. 面试定位

这题的高分标准不是堆术语，而是完成下面四步：

1. **先给结论**：30 秒内明确对象是什么、解决什么问题。
2. **再讲机制**：指出关键数据结构/电路/执行阶段，以及信息如何流动。
3. **补充量化关系**：至少给一个公式、数量级或可测指标。
4. **最后讲边界**：明确哪些是架构保证，哪些只是常见微架构实现。

> **本题一句话心智模型**：{mechanism}

---

## PDF 核心结论

### 原 PDF 一句话答案

> {pdf_core}

### PDF 深度解析要点

{deep_md}

### PDF 建议的回答组织

> {q['answer_org']}

### PDF 易错点

> {gotcha}

---

## 深入扩展

### 第一性原理推导：为什么硬件需要这个机制？

{c['first']}

针对本题，更具体地说：**{mechanism}**

面试时可以使用“压力 → 机制 → 代价”的推导链：

```text
原始问题 / 物理限制
        ↓
如果什么都不做，会产生的正确性或性能问题
        ↓
硬件/ISA 引入本题机制
        ↓
改善 latency / throughput / capacity / correctness 中的某一项
        ↓
付出面积、功耗、带宽、复杂度或软件约束
```

### 本题必须守住的抽象层级

{ARCH_NOTES[ch]}

一个专业回答通常会显式使用下面两句话之一：

- **“这是 architectural guarantee；具体如何做到属于 microarchitecture。”**
- **“这是常见实现，不是 ISA 必须如此。”**

这样可以避免把教材示意图、某一代 Intel/Arm/RISC-V 核心的参数，错误泛化成所有处理器的规则。

---

## 机制展开：从输入到结果

### 核心机制

{mechanism}

### 原 PDF 要点如何落到完整执行链

{deep_md}

### 最小结构图

```mermaid
{c['diagram']}
```

图的目的不是背结构，而是回答两个问题：

1. **信息/数据在哪里产生？**
2. **下一个消费者什么时候才能安全使用？**

只要把生产者、消费者、缓存/队列和提交点画清楚，大多数连续追问都会自然展开。

---

## 定量模型与最小例子

{quant}

本章常用的量化视角是：{c['metrics']}

{CODE[ch]}

### 面试中的定量回答套路

不要只说“更快”“更慢”，而要把影响投影到一个可观察量：

| 类型 | 更专业的指标 |
|---|---|
| 指令执行 | latency、throughput、IPC/CPI、dependency depth |
| Cache/内存 | hit rate、MPKI、AMAT、bandwidth、MLP |
| 地址翻译 | TLB miss、page-walk、TLB reach |
| 多核 | invalidation、HITM、cache-line bouncing、barrier cost |
| I/O | interrupt rate、DMA throughput、queue depth、outstanding |
| 存储 | IOPS、latency percentile、bandwidth、write amplification |

---

## 边界条件、反例与“不要说绝对”

**本题最重要的边界：** {boundary}

进一步回答时建议主动检查：

- 结论是否只对 **单核 / 多核** 中一种成立？
- 是否假设了 **cache hit / TLB hit / 无异常**？
- 是否把 **语言语义、ABI、ISA、微架构、OS** 混成一层？
- 是否把“常见值”说成“固定值”？例如 64B cache line、某级 cache latency、ROB 大小。
- 是否忽略了并发、带宽饱和、排队和 backpressure？

### 一个反例思维

如果一个结论是“机制 X 会更快”，立刻追问：

> 在工作集、并发度、访问模式或硬件资源发生什么变化时，它会失效甚至变慢？

能回答这个问题，通常已经从“背题”进入真正的体系结构分析。

---

## 工程连接

{engineering}

### 推荐验证方法

```text
1. 建立 baseline：固定输入、绑核/记录频率、重复运行
2. 提出单一假设：例如 branch miss 或 DTLB miss 是主因
3. 找直接指标：PMU / trace / latency / bandwidth
4. 只改一个变量
5. 重测并检查副作用
6. 保留反例：优化是否只对某一数据规模有效？
```

### 常用工具思路

- Linux：`perf stat`、`perf record`、`perf c2c`、`numactl`、`vmstat`、`iostat`。
- 汇编/编译：Compiler Explorer、`objdump` / `llvm-objdump`。
- 微基准：Google Benchmark、自写 dependency-chain / pointer-chasing / streaming benchmark。
- 平台资料：Intel/AMD optimization manual、Arm TRM、RISC-V core vendor manual。

> 工具只是证据来源。真正重要的是：**每个指标都要对应一个可证伪的性能假设。**

---

## 架构实现差异：x86 / Arm / RISC-V 应怎么回答

本题若被追问到具体 ISA，建议使用“共性 + 差异”结构：

1. **共性机制**：先说明所有现代处理器为什么都面临同一设计压力。
2. **ISA 差异**：再说明指令、内存模型、页表、barrier 或 ABI 的规定不同。
3. **微架构差异**：最后强调 cache、predictor、ROB、端口等实现参数依具体 CPU。

{ARCH_NOTES[ch]}

不要在没有芯片手册或可靠测量时背具体周期数。面试官更看重你是否知道 **“哪些数字可以变化”**。

---

## 30–60 秒标准回答

### 30 秒版

> **结论：** {q['recap']}
>
> **机制：** {mechanism}
>
> **边界：** {boundary}

### 2 分钟版

建议按下面顺序回答：

1. 重述本题对象与目标；
2. 用 2–3 个核心结构解释机制；
3. 给出一个最小公式/例子：**{quant}**
4. 指出最重要的边界：**{boundary}**
5. 用一句工程话收尾：**{engineering}**

### 5 分钟深挖版

在 2 分钟版基础上继续加入：

- 与相邻机制的区别，例如 cache vs TLB、ROB vs RS、coherence vs consistency；
- 一个反例或 trade-off；
- x86 / Arm / RISC-V 中哪些是共性、哪些不同；
- 一个 PMU/微基准验证方案；
- 如果资源扩大 2×，性能是否也能 2×，为什么？

---

## 原 PDF 追问 + 二阶追问树

### 原 PDF 追问

> {follow}

### GitHub v2 二阶追问

1. **设计动机**：如果完全移除这个机制，首先破坏的是正确性还是性能？为什么？
2. **资源上限**：如果把相关 buffer/cache/队列扩大 2×，收益会在哪个点开始递减？
3. **相邻机制**：它与本章前后题中的哪个机制最容易混淆？判定边界是什么？
4. **架构差异**：换到另一种 ISA，哪些结论仍成立，哪些必须查手册？
5. **性能验证**：你会观察哪 2–3 个硬件事件来证明它真的成为瓶颈？
6. **反例**：构造一个 workload，让这个机制几乎没有收益，甚至产生负收益。

---

## 常见错误表达 → 专业表达

| 不够专业 | 更专业的说法 |
|---|---|
| “CPU 就是这样做的” | “这是常见微架构实现；ISA 只保证最终可观察语义。” |
| “它会更快” | “它主要降低/隐藏某类 latency，或提高 throughput；收益取决于命中率、并行度和资源占用。” |
| “Cache/内存很慢” | “先看具体层级、MPKI、miss penalty 与 bandwidth 是否饱和。” |
| “加大 buffer 就行” | “窗口扩大只能覆盖更多独立工作；若受 true dependency 或带宽限制，收益会饱和。” |
| “某参数固定是 X” | “X 是常见实现值，目标平台应查官方手册或实测。” |

本题尤其要避免：**{gotcha}**

---

## 面试官评分标准

### 合格

- 定义正确；
- 能复述 PDF 核心结论；
- 不混淆最基本术语。

### 良好

- 能解释“为什么需要”；
- 能描述关键执行链；
- 能给出一个边界条件和一个量化关系。

### 优秀

- 主动区分 ISA / microarchitecture / OS / ABI；
- 能讨论 trade-off 而不是单向优点；
- 能提出 PMU 或微基准验证方法；
- 能把本题连接到相邻题形成完整系统模型。

---

## 自测

- [ ] 能在 30 秒内回答，不使用超过 5 个术语。
- [ ] 能画出最小数据/控制路径，并标出生产者和消费者。
- [ ] 能写出至少一个相关公式或数量级关系。
- [ ] 能给出一个反例，说明机制不是“永远更好”。
- [ ] 能说清 architectural guarantee 与 microarchitectural implementation。
- [ ] 能提出 2 个 PMU/实验指标来验证性能判断。
- [ ] 能把本题与本章相邻问题连接起来。

---

## 关联题目

{related_lines}

---

## 延伸阅读

以下资料用于 **GitHub 深度扩展的架构校准**，不代表原 PDF 逐字引用：

{refs}

全仓统一参考索引见：[参考资料与校准基线]({rel_link(f, DOCS/'appendices/references.md')})。

---

## 一句话复盘

> {q['recap']}

---

{nav}
'''
    f.write_text(text,encoding='utf-8')

# Upgrade chapter READMEs with competency ladders.
for ch,c in chapters.items():
    folder=DOCS/c['slug']
    rows=[]
    for q in questions[(ch-1)*10:ch*10]:
        f=qid_to_file[q['id']]
        rows.append(f"| [Q{q['id']:03d}]({f.name}) | {q['title']} | {q['difficulty']} | {q['frequency']} | {q['page']} |")
    readme=f'''# 第 {ch} 章｜{c['title']}

> **本章目标**：{c['first']}

## 能力阶梯

| 层级 | 你应该做到什么 |
|---|---|
| L1 定义 | 30 秒说清术语和目标 |
| L2 机制 | 能画出最小硬件/执行链 |
| L3 定量 | 能用公式、数量级或 PMU 指标分析 |
| L4 边界 | 能指出架构保证与微架构差异 |
| L5 工程 | 能设计 benchmark / profiling 验证假设 |

## 本章核心指标

{c['metrics']}

```mermaid
{c['diagram']}
```

## 题目索引

| 题号 | 题目 | 难度 | 频率 | PDF 页 |
|---|---|---|---|---:|
{chr(10).join(rows)}

## 学习要求

建议每题完成三轮：

1. **30 秒**：只答结论、机制、边界；
2. **2 分钟**：加入一个公式/最小例子；
3. **5 分钟**：加入架构差异、工程指标与反例。

完成本章后，不应只“认识名词”，而应能把 10 道题连接成一条因果链。
'''
    (folder/'README.md').write_text(readme,encoding='utf-8')

# README/STYLE/CHANGELOG upgrades.
readme=(ROOT/'README.md').read_text(encoding='utf-8')
readme=re.sub(r'## 特点\n', '## v2 深度增强版\n\n- 100/100 题已升级为 **第一性原理 → 机制 → 定量 → 边界 → 工程验证 → 架构差异 → 追问树** 的完整结构。\n- 每题都保留 PDF 原始内容，并明确标记 GitHub v2 新增部分，避免来源混淆。\n- 每题加入 30 秒 / 2 分钟 / 5 分钟三档回答，以及 PMU/微基准验证思路。\n- 各章 README 增加能力阶梯、关键指标和架构图。\n\n## 特点\n', readme, count=1)
(ROOT/'README.md').write_text(readme,encoding='utf-8')

style='''# Style Guide · v2\n\n每题采用统一顺序：\n\n1. 面试定位\n2. PDF 核心内容\n3. 第一性原理推导\n4. 机制展开\n5. 定量模型与最小例子\n6. 边界条件与反例\n7. 工程验证\n8. 架构实现差异\n9. 30 秒 / 2 分钟 / 5 分钟回答\n10. 追问树\n11. 错误表达修正\n12. 评分标准与自测\n13. 关联题与官方参考\n\n## 强制原则\n\n- 先结论后细节；\n- 明确 architectural vs microarchitectural；\n- “更快/更慢”必须落到 latency、throughput、IPC/CPI、miss rate、bandwidth、MPKI 等指标；\n- 教材模型与现代实现并列，而不是互相替代；\n- 任何具体 cache latency、ROB size、predictor 结构都不得冒充 ISA 固定事实；\n- 原 PDF 内容与 GitHub 增强内容必须显式分区；\n- 不伪造公司/面试轮次归属。\n'''
(ROOT/'STYLE_GUIDE.md').write_text(style,encoding='utf-8')

chg=(ROOT/'CHANGELOG.md').read_text(encoding='utf-8') if (ROOT/'CHANGELOG.md').exists() else '# Changelog\n'
entry='''\n## v2.0-deep — 2026-09-02\n\n- 100/100 题全部深度重写扩展；\n- 每题增加第一性原理、机制链、定量模型、反例/边界、工程验证、架构差异；\n- 每题增加 30 秒 / 2 分钟 / 5 分钟三档回答；\n- 每题增加二阶追问树、面试官评分标准、关联题和官方参考；\n- 10 个章节 README 升级为能力阶梯 + 指标 + Mermaid 架构图；\n- 明确 PDF 原始内容与 GitHub v2 增强内容的 provenance。\n'''
if 'v2.0-deep' not in chg:
    chg += entry
(ROOT/'CHANGELOG.md').write_text(chg,encoding='utf-8')

print('Upgraded 100 question markdown files and 10 chapter READMEs.')
