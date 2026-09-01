---
id: Q022
title: "编辑距离：动态规划怎么写？如何降空间？"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★"
frequency: "★★★★★"
tags:
  - classical-nlp
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q022 编辑距离：动态规划怎么写？如何降空间？

[← Q021](Q021-bm25.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q023 →](Q023-text-classification-evolution.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`classical-nlp`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q022.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

求 Levenshtein distance：插入、删除、替换代价均为 1。写状态转移和复杂度。

## 2. 面试官到底在考什么

经典代码题，兼顾 NLP 场景。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

dp[i][ j] 表示 s[:i] 变成 t[:j] 的最小代价。字符相同取左上角，否则取删除、插入、替换三者最小值 加一。时间 O(mn)，空间可压缩到 O(min(m,n))。

## 4. 白板核心公式

- $dp[i][j]=\min\{dp[i-1][j]+1,\;dp[i][j-1]+1,\;dp[i-1][j-1]+[s_i\neq t_j]\}$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：初始化第一行/列对应连续插入或删除。
- **PDF 基线要点**：可扩展不同操作权重、Damerau transposition。
- **PDF 基线要点**：在拼写纠错、OCR、ASR、去重中常用。
- **扩展理解**：Levenshtein DP 的三个操作是插入、删除、替换；状态定义决定转移是否自然。
- **扩展理解**：空间可从 O(mn) 降到 O(min(m,n))，但若要恢复编辑路径需保留更多信息。
- **扩展理解**：面试可扩展到 weighted edit distance、Damerau-Levenshtein。

## 6. 专业深挖：原理、边界与工程

### 编辑距离的 DP 本质
- 令 $dp[i][j]$ 表示 $s[:i]$ 变成 $t[:j]$ 的最少操作；最后一步只能是删除、插入或替换/匹配，因此得到三路最优子结构。
- 边界 $dp[i][0]=i,dp[0][j]=j$；标准复杂度 $O(mn)$ 时间、$O(mn)$ 空间。
- 若只要距离而不恢复路径，每个状态只依赖上一行和当前行左侧，可降到 $O(\min(m,n))$ 空间。
### 边界与工程
- 若需要恢复编辑操作，必须保存 backpointer/完整表，或采用额外分治重算策略。
- 实际应用可能使用加权编辑距离、Damerau transpose、字符/Unicode grapheme 粒度，不能把标准 Levenshtein 当唯一版本。
- 当只关心距离 ≤k 时可使用 banded DP，只计算主对角线附近区域。

## 7. 实现、复杂度与工程验证

- 给出状态/标签空间、独立性假设和训练/解码复杂度。
- 区分局部 score、全局归一化与解码约束。
- 真实 NLP 数据要考虑 OOV、标注规范、领域词典和 span 对齐。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 边界条件漏掉空串。
- 把替换写成两次操作。

## 9. 追问树

1. 如何恢复具体编辑路径？
2. 如何做 banded DP 加速近似匹配？

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

## 10. 面试现场自检

- [ ] 30-60 秒能给出结论，不绕弯。
- [ ] 能写出关键公式、shape 或状态转移。
- [ ] 至少能解释一个 Why 和一个 trade-off。
- [ ] 能举出一个失败模式或反例。
- [ ] 能回答两层追问。
- [ ] 能把答案连接到真实训练/检索/服务系统。

## 11. 参考资料

- [CRF](https://repository.upenn.edu/cis_papers/159/)
- [BM25 overview (Stanford IR book)](https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)
- [Q023 文本分类方案如何随数据规模演进？](Q023-text-classification-evolution.md)
- [Q015 BERT 后为什么还要接 CRF？](Q015-bert-crf.md)

## 13. 一句话收束

> **编辑距离的 DP 本质**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
