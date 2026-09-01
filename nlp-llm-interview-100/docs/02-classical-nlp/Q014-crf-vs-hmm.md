---
id: Q014
title: "CRF 和 HMM 有什么根本区别？"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - classical-nlp
  - crf
  - hmm
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q014 CRF 和 HMM 有什么根本区别？

[← Q013](Q013-hmm.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q015 →](Q015-bert-crf.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`classical-nlp`, `crf`, `hmm`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q014.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

Linear-chain CRF 为什么适合序列标注？与 HMM 相比优势在哪里？

## 2. 面试官到底在考什么

考察生成式与判别式序列建模。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

HMM 建模 P(X,Y)，CRF 直接建模 P(Y|X)，可自由使用输入特征并通过全局归一化建模标签序列 依赖。

## 4. 白板核心公式

- $P(y|x)=\frac{\exp s(x,y)}{\sum_{y\prime}\exp s(x,y\prime)}$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：CRF 的 score 通常由 emission 与 transition 累加。
- **PDF 基线要点**：分母需要对所有标签序列求和，可用动态规划计算 partition function。
- **PDF 基线要点**：CRF 避免 MEMM 的局部归一化 label bias 问题。
- **扩展理解**：CRF 直接建模 P(y|x)，无需为输入分布建模，因此能使用更丰富的重叠特征。
- **扩展理解**：Linear-chain CRF 的全局归一化避免逐位置独立分类导致的标签不一致。
- **扩展理解**：可继续讨论 label bias：它更典型地出现在局部归一化的 MEMM。

## 6. 专业深挖：原理、边界与工程

### 生成模型与判别模型的根本分界
- HMM 建模 $P(X,Y)$，需要为输入观测的生成过程指定 emission；CRF 直接建模 $P(Y|X)$，可以自由使用任意输入特征。
- 线性链 CRF 的序列 score 经过全局 partition function 归一化，训练用 forward/logsumexp，解码用 Viterbi/max。
- 全局归一化也是 CRF 相对 MEMM 的关键：它缓解局部归一化带来的 label bias。
### 边界与工程
- CRF 仍然通常只建模一阶标签依赖，跨句、嵌套实体等复杂结构并不会自动解决。
- 神经 CRF 只是把 emission 换成神经网络输出，CRF 的 transition、partition 和动态规划本质不变。
- 实现中非法 BIO transition 可硬 mask 成大负值，padding 必须从序列 DP 中排除。

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

- 把 CRF 当成“一个分类器层”。
- 说 CRF 一定比 token softmax 好。

## 9. 追问树

1. 什么是 label bias？
2. CRF 训练的负对数似然如何计算？

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

- [Q013 HMM：三个基本问题与两条核心假设](Q013-hmm.md)
- [Q015 BERT 后为什么还要接 CRF？](Q015-bert-crf.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)

## 13. 一句话收束

> **生成模型与判别模型的根本分界**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
