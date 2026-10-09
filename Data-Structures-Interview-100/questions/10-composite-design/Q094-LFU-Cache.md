---
id: Q094
title: "LFU Cache"
difficulty: "H"
category: "复合数据结构设计"
core: "HashMap / Frequency Buckets"
source: "《数据结构面试100题：专业面试宝典》2026 Edition"
---

# Q094 LFU Cache

> **难度：** H  
> **核心：** HashMap / Frequency Buckets  
> **章节：** 复合数据结构设计  
> **内容边界：** “原稿”部分来自仓库内 PDF 对应题目；“深化解析”是在原稿基础上的扩展讲解，不新增未经来源支持的公司题库归属。

[← Q093 LRU Cache](../10-composite-design/Q093-LRU-Cache.md) · [返回 100 题索引](../../README.md#100-题目录) · [Q095 Time Based Key-Value Store →](../10-composite-design/Q095-Time-Based-Key-Value-Store.md)

## 1. 题目

固定容量缓存，淘汰使用频率最低的键；频率相同时按 LRU 淘汰。要求 get/put 平均 O(1)。

### 仓库深化：手推示例

> 容量 2：`put(1,1), put(2,2), get(1), put(3,3)` 时 key=2 频率最低被淘汰；若频率相同，则再按同频桶内的 LRU 顺序淘汰。

手推时不要只算最终输出，建议同步写出核心结构在每一步的状态变化，这比“看懂答案”更接近真实面试。

## 2. 面试开始先澄清

- 输入规模与合法性：是否允许空输入、重复值、负数，是否保证答案存在？

- 是否允许修改输入？输出是否要求稳定顺序或去重？

- 复杂度目标：题目是否明确要求 O(n)、O(log n) 或 O(1) 额外空间？

## 3. 基线方案与瓶颈

每次淘汰扫描全部键找最低频会 O(n)。

### 解法演进对比

| 层级 | 思路 | 代价 / 价值 |
|---|---|---|
| Baseline | 每次淘汰扫描全部键找最低频会 O(n)。 | 先保证正确，暴露真正瓶颈 |
| 面试目标 | 围绕 `HashMap / Frequency Buckets` 维护最小必要状态 | 平均 get/put O(1)，空间 O(capacity)。 |

这张表的重点不是“最优解一定唯一”，而是能够解释**为什么新结构减少了哪一类重复工作**。

### 深化解析：先定位重复工作

本题所在章节的核心原则是 **API 复杂度倒推结构组合**。逐个写出 API 的目标复杂度，再找单一结构无法满足的地方，最后组合 Hash、链表、堆、桶、树或环形数组。

面试中不要直接报最优结构。先说明基线方案具体重复做了什么，再指出目标结构如何把这部分重复工作缓存、单调淘汰、分层搜索或局部化维护。这样能证明你是在从约束推导算法，而不是背模板。

## 4. 关键洞察：为什么这个数据结构合适

维护 key→node；freq→双向链表（同频节点按 LRU 排列）；minFreq 指向当前最低频率。访问节点时从 旧频率链移除并加入 freq+1 链尾；若旧链为空且等于 minFreq，则 minFreq++。

### 结构选择检查表

- **我们反复查询/维护的信息是什么？** 把它写成一句话。
- **这个信息是否具有有序性、单调性、前缀性、局部性或等价关系？** 这些性质通常直接决定数据结构。
- **是否需要在线更新？** 静态问题和动态问题往往需要不同结构。
- **输出规模是否本身构成复杂度下界？** 返回所有答案时尤其重要。
- **是否能说明替代结构为什么更差？** 面试官常通过这一问验证理解深度。

## 5. 不变量与正确性证明

> **原稿不变量：** 每个节点只存在于与其 freq 对应的一条链；minFreq 始终是非空频率桶最小值，因此 淘汰可直接从该桶 LRU 端取。

### 正确性证明框架

1. **初始化：** 证明算法开始时不变量成立。
2. **保持：** 假设处理当前元素/节点前不变量成立，说明一次更新后仍成立。
3. **终止：** 结合循环或递归终止条件，说明得到的状态恰好对应题目要求。
4. **无遗漏/无重复：** 如果题目要求枚举答案，额外说明为何每个合法答案都会被访问，且不会被重复输出。

这是面试中比“跑几个样例看起来对”更强的论证方式。

## 6. 参考实现（Python）

```python
# 面试代码建议复用带哨兵的 DoublyLinkedList。
# 状态核心：
# nodes[key] -> node(key,value,freq)
# buckets[freq] -> ordered nodes of that freq
# min_freq -> smallest non-empty frequency
```

### 仓库深化：完整可执行实现

> 以下实现是 **GitHub 仓库深化内容**，用于把 PDF 中的结构骨架补成可执行版本；核心设计仍严格遵循原稿的 `nodes + buckets + minFreq` 不变量。

```python
from collections import defaultdict


class _LFUNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class _DoublyLinkedList:
    def __init__(self):
        self.head = _LFUNode()
        self.tail = _LFUNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1

    def pop_lru(self):
        if self.size == 0:
            return None
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}
        self.buckets = defaultdict(_DoublyLinkedList)
        self.min_freq = 0

    def _touch(self, node):
        old_freq = node.freq
        old_bucket = self.buckets[old_freq]
        old_bucket.remove(node)

        if old_freq == self.min_freq and old_bucket.size == 0:
            self.min_freq += 1

        node.freq += 1
        self.buckets[node.freq].append(node)

    def get(self, key):
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._touch(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._touch(node)
            return

        if len(self.nodes) == self.capacity:
            victim = self.buckets[self.min_freq].pop_lru()
            del self.nodes[victim.key]

        node = _LFUNode(key, value)
        self.nodes[key] = node
        self.buckets[1].append(node)
        self.min_freq = 1
```

**为什么仍是平均 O(1)：** 哈希表定位节点是平均 O(1)；节点只在相邻频率桶之间移动；双向链表已知节点删除、尾部插入、LRU 端淘汰均为 O(1)。`min_freq` 只在当前最低频桶变空时递增，插入新键时直接重置为 1。


### Code Review 视角

- 变量名应直接体现状态含义，不要让 `i/j/tmp` 承担过多语义。
- 修改共享结构前，先确认是否会丢失后续仍需访问的信息。
- 对 Hash/Heap/Queue/Tree 等结构，明确其中保存的是**值、下标、节点还是聚合状态**。
- 让实现与上面的不变量一一对应；如果代码中存在无法解释的特殊分支，通常意味着状态定义还不够干净。
- Python 内置操作也有复杂度：例如 list 头部删除是 O(n)，`heapq` pop/push 是 O(log n)，dict/set 操作是平均 O(1)。

## 7. 复杂度

平均 get/put O(1)，空间 O(capacity)。

### 复杂度审查

| 维度 | 需要回答的问题 |
|---|---|
| 时间 | 是最坏、平均还是摊销？隐藏参数是 n、k、V/E、L 还是窗口 W？ |
| 空间 | 统计的是额外空间还是包含输出？递归栈算不算？ |
| 预处理 | 排序、建索引、建 Trie/Heap 的成本是否被漏算？ |
| 输出下界 | 若答案本身有 m 项，是否至少需要 O(m)？ |

## 8. 高频失分点

- 只维护频率，不处理同频 LRU

- 桶空后忘记更新 minFreq

- put 新键 minFreq 必须重置为 1

### 额外边界测试

- 最小合法输入与空输入（若题目允许）
- 重复值/重复状态是否改变算法不变量
- 只有一个节点/容量为 1
- 头尾节点或删除最后一个元素

建议面试现场至少手推一个“最小输入”、一个“最容易破坏不变量的输入”和一个“规模极端输入”。

## 9. 面试官追问与答题方向

- 如果频率无限增长如何 aging？
  - **答题方向：** 先把新增约束写成需要维护的新不变量，再判断原结构能否继续满足；若不能，明确需要替换或组合的结构。
- 为什么“频率+时间”两个排序维度不适合一个简单 heap？
  - **答题方向：** 先把新增约束写成需要维护的新不变量，再判断原结构能否继续满足；若不能，明确需要替换或组合的结构。

### Follow-up 的统一处理方法

不要把追问当成新题。先问：**原方案依赖的哪个前提被改变了？** 然后只替换受到影响的那一层结构。例如从离线变在线，通常保留问题定义而替换状态维护方式；从单机变分布式，则新增分片、一致性和容错约束。

## 10. 60 秒口述模板

我会先给出一个可工作的基线方案：每次淘汰扫描全部键找最低频会 O(n)。 真正的瓶颈在重复工作，因此优化的核心 是：维护 key→node；freq→双向链表（同频节点按 LRU 排列）；minFreq 指向当前最低频率。访问节点时从旧频率 链移除并加入 freq+1 链尾；若旧链为空且等于 minFreq，则 minFreq++。 正确性依赖的不变量是：每个节点只存在于 与其 freq 对应的一条链；minFreq 始终是非空频率桶最小值，因此淘汰可直接从该桶 LRU 端取。 最终复杂度为：平均 get/put O(1)，空间 O(capacity)。

## 11. 自测清单

- [ ] 不看代码，能在 60 秒内讲清“基线 → 瓶颈 → 关键结构”。
- [ ] 能写出核心不变量，并解释一次状态更新为什么不破坏它。
- [ ] 能独立手写参考实现，不依赖 IDE 自动补全。
- [ ] 能给出时间/空间复杂度，并注明平均、摊销或最坏情形。
- [ ] 能覆盖至少 3 个边界条件。
- [ ] 能回答至少 2 个 follow-up，并说明为什么需要/不需要替换数据结构。


## 12. 专业深化：约束驱动的完整面试推导

> 本节属于 **GitHub 仓库深化内容**：在源 PDF 的题意、洞察、不变量与代码之上补充更严格的算法论证、替代方案、测试与工程边界；不新增未经来源支持的公司题库归属。

### 12.1 先从约束识别 Pattern，而不是从题名背模板

本题的目标结构是 **HashMap + 频次桶双链表**。出现以下信号时，应主动联想到这一类结构：

- 一个 API 同时要求多种看似冲突的复杂度目标
- 单一结构不能同时满足定位、排序、淘汰/随机访问
- 题目核心是组合结构与状态一致性

把题目抽象成一句“数据结构需求”会更有效：

> 先列每个 API 需要的 primitive operation，再为每个 operation 选择结构；最后写跨结构的一致性 invariant。

> **本题特别说明：** LFU 比 LRU 多一个排序维度：frequency；而同 frequency 内仍需 recency。`minFreq` 是把“找最低频桶”从扫描降到 O(1) 的关键冗余状态。

### 12.2 状态最小化：到底必须记住什么

源书稿给出的核心不变量是：

> 每个 node 只属于与自身 freq 相同的一个 LRU 桶；minFreq 始终指向至少一个节点的最小频次。

进一步拆成三个层次：

1. **输入事实**：当前扫描到的元素、节点、边或操作，哪些信息一旦过去就不会再改变？
2. **未来充分统计量**：未来决策真正需要历史中的哪些摘要？只保存这些，而不是保存“所有历史以防万一”。
3. **答案状态**：区分“用于继续计算的状态”和“已经闭合的最终候选”。Tree DP、Heap、窗口和复合结构题尤其容易把两者混在一起。

面试时可以直接用下面这句话验证自己的状态设计：

> **如果我删除当前结构中的某一类信息，未来是否存在一个合法输入让我无法正确决定？如果不存在，它就不应该被保存。**

### 12.3 解法谱系与 Trade-off

| # | 方案 | 定位 |
|---:|---|---|
| 1 | 每次淘汰扫描所有 key O(n) | 基线/对照 |
| 2 | Heap 可 O(log n) 但更新有 stale entry | 可选方案 |
| 3 | key map + freq->LRU DLL + minFreq 实现平均 O(1) | 面试主解 |

选择主解时至少回答三个问题：

- 它具体消除了基线中的哪一类重复工作？
- 它依赖哪些输入性质（有序、非负、单调、树结构、固定窗口等）？
- 如果这些性质被 follow-up 改掉，哪一层会首先失效？

### 12.4 针对本题的正确性证明

- **跨结构不变量：** 每个 node 只属于与自身 freq 相同的一个 LRU 桶；minFreq 始终指向至少一个节点的最小频次。
- **定位正确性：** Hash/索引层必须能唯一定位当前逻辑对象，不能出现同一 key 对应多个活跃节点。
- **顺序/桶正确性：** 链表、Heap、频次桶或时间槽只承担自己那一维顺序；每次 API 操作都要同步维护索引层与顺序层。
- **原子更新：** 一次逻辑操作结束后，要么对象同时存在于所有应存在的结构中，要么从所有结构中移除；不存在“只更新了一半”的中间持久状态。
- **复杂度结论：** 每个 API 只做常数次 Hash 操作与目标结构的 O(1)/O(log n) 原语，因此整体复杂度由这些原语上界给出。

> **面试表达建议：** 不要说“代码跑样例是对的”。先说状态语义，再说一次更新为什么保持语义，最后说明终止时为何覆盖所有合法答案。

### 12.5 复杂度：除了 Big-O 还要说明参数和模型

源书稿结论：**设计正确时 get/put 平均 O(1)，空间 O(capacity)。**

进一步需要注意：

- HashMap/Set 操作按平均 O(1) 计；若讨论 adversarial collision，最坏界需要单独说明。

专业回答建议写成：

```text
n = 主输入规模
k / L / V / E / W = 题目中真正影响结构规模的辅助参数
Time = ...（说明 worst / average / amortized）
Aux Space = ...（不含/包含输出，明确递归栈）
Preprocess = ...（若存在排序、压缩、建索引）
```

### 12.6 Dry Run：必须跟踪“状态”，不是只写答案

建议在白板手推时至少画下面这张表；列名已经按本题 Pattern 定制：

| operation | key/input | index/hash state | order/bucket state | result & invariant check |
| --- | --- | --- | --- | --- |
| `...` | `...` | `...` | `...` | `...` |
| `...` | `...` | `...` | `...` | `...` |
| `...` | `...` | `...` | `...` | `...` |

每一行都要能够回答：**为什么这个状态可以被加入、删除、移动或结算？** 如果答不出来，通常说明不变量还没有真正建立。

### 12.7 代码审查：从 AC 代码提升到面试级实现

- 先设计 Node/Bucket 数据模型再写 API
- 任何跨两个容器的修改都要考虑“只更新一边”的一致性 bug
- 真实系统要额外讨论并发、容量、持久化、过期与故障恢复，但不要让系统设计淹没算法题

此外，对本题代码建议做四次快速 review：

1. **State review**：每个变量能否用一句不变量解释？
2. **Boundary review**：所有 `+1/-1`、开闭区间、空结构分支是否统一？
3. **Mutation review**：修改容器/指针后，另一个索引或引用是否需要同步更新？
4. **Complexity review**：有没有隐藏的切片、排序、线性删除、重复 DFS 让宣称复杂度失真？

### 12.8 对抗性测试矩阵

| 测试维度 | 本题应覆盖的情况 | 目的 |
|---|---|---|
| 最小/空边界 | 容量 0/1 | 验证不变量与边界处理，不只验证最终值 |
| 重复/相等状态 | 更新已存在 key | 验证不变量与边界处理，不只验证最终值 |
| 结构极端 | 淘汰/删除恰好发生在头尾或唯一元素 | 验证不变量与边界处理，不只验证最终值 |
| 约束破坏/反例 | 只用一个 heap 会因更新频次产生 stale entries，难保证严格 O(1)。 | 验证不变量与边界处理，不只验证最终值 |

源书稿中的高频失分点也应逐个转成单元测试：

- **反例化：** 只用一个 heap 会因更新频次产生 stale entries，难保证严格 O(1)。
- **反例化：** minFreq 更新是最容易漏的状态。
- **反例化：** 同频次必须再维护 LRU 顺序。

### 12.9 Follow-up 深挖：不是换题，而是定位“哪个前提变了”

#### 12.9.1 如果允许 O(log n)，用 heap 是否更简单？

- **变化的前提：** 放宽复杂度到 O(log n) 后，可以用更通用但更简单的优先队列。
- **推荐方向：** 说明 Heap 的 stale-entry/update 问题；若能接受 lazy deletion，它往往减少双链表/桶结构实现复杂度。
#### 12.9.2 频次会无限增长如何 aging？

- **变化的前提：** 传统 LFU 把历史频次永久累加，会让很久以前的热点长期占优势。
- **推荐方向：** 引入时间衰减/周期性 halving、epoch 频次，或使用近似频率 sketch；这会改变 `minFreq` 的严格整数相邻性，通常要接受更复杂维护或近似策略。
#### 12.9.3 TinyLFU 与传统 LFU 的区别？

- **核心区别：** TinyLFU 更像“准入策略（admission policy）”而不是单纯的淘汰顺序。它用近似频率统计判断新对象是否值得挤掉 victim。
- **推荐方向：** 频率可由 Count-Min Sketch/Doorkeeper 近似，缓存主体仍可配 LRU/SLRU；目标是减少一次性扫描流量污染缓存。

### 12.10 Pattern 迁移：什么时候应该想到它

**识别信号：**

- 一个 API 同时要求多种看似冲突的复杂度目标
- 单一结构不能同时满足定位、排序、淘汰/随机访问
- 题目核心是组合结构与状态一致性

**迁移方法：**

- 先保留本题的不变量形式，再替换数据载体。例如数组窗口换成字符流，核心仍是“进入/离开时可增量更新的统计”。
- 如果从静态变动态，问“原预处理为什么失效”，再引入可更新结构；不要直接跳到更复杂数据结构。
- 如果从单答案变所有答案，先把输出规模写进复杂度，再讨论去重、predecessor 或路径恢复。
- 如果从算法题变系统级 follow-up，明确算法层与工程层边界：算法不变量仍要成立，工程层再叠加并发、分片、缓存与容错。

### 12.11 面试官视角：这题真正区分候选人的地方

| 能力层级 | 典型表现 |
|---|---|
| 只会做 | 能写出代码，但无法解释为什么该结构成立 |
| 合格 | 能从 baseline 推出 `HashMap + 频次桶双链表`，复杂度与边界基本正确 |
| 较强 | 能写出不变量/证明，并比较至少一种替代方案 |
| 很强 | follow-up 改约束后，能明确指出**失效的前提**并局部替换结构，而不是重新猜算法 |

建议复盘时把目标定为最后两档，而不是“AC 即完成”。
---

**源书稿：** [`assets/pdf/数据结构面试100题_专业版.pdf`](../../assets/pdf/数据结构面试100题_专业版.pdf)  
**章节索引：** [`复合数据结构设计`](./README.md)
