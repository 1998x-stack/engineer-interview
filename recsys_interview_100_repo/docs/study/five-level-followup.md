# 把一道题答到 5 层：追问树

以双塔为例：

1. **定义**：双塔是什么？—— User Tower / Item Tower 独立编码，最后点积或相似度。
2. **为什么**：为什么适合召回？—— Item 向量可预计算并建立 ANN 索引。
3. **机制**：怎么训练？—— InfoNCE / sampled softmax，核心在 negative distribution。
4. **工程偏差**：In-batch 有什么问题？—— False Negative + popularity / sampling bias。
5. **线上验证**：离线 Recall 涨了为什么线上不涨？—— 候选增量、索引误差、后续排序吞噬、分布差异、时延。

真正的目标不是“背到第五层”，而是形成一条可以迁移到其他题目的推理路径：

> **Definition → Mechanism → Assumption → Trade-off → Online Evidence**
