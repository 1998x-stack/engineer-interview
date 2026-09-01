# 推荐系统核心原始资料索引

> 这一页只收录适合用于**校准模型定义和工业事实**的原始论文、会议页面或官方实现。公开面经用于判断题目频率，不应替代原始技术来源。

## 1. 工业推荐架构与召回

### YouTube DNN Recommendation

- **Deep Neural Networks for YouTube Recommendations**
- 关键主题：candidate generation、ranking、工业级两阶段推荐。
- 面试对应：Q001、Q002、Q014、Q024。
- 官方页面：https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/

阅读重点：不要只记“召回+排序”两个名字，要理解为什么 candidate generation 需要可扩展表示、为什么 ranking 可以使用更丰富特征，以及训练样本与线上候选分布如何对应。

### BPR

- **BPR: Bayesian Personalized Ranking from Implicit Feedback**
- 关键主题：implicit feedback、pairwise ranking。
- 面试对应：Q013、Q019、Q064。
- 论文：https://arxiv.org/abs/1205.2618

---

## 2. CTR 与特征交叉

### Wide & Deep

- **Wide & Deep Learning for Recommender Systems**
- 关键主题：memorization / generalization。
- 面试对应：Q028、Q029。
- 论文：https://arxiv.org/abs/1606.07792

### DeepFM

- **DeepFM: A Factorization-Machine based Neural Network for CTR Prediction**
- IJCAI 2017。
- 关键主题：FM 低阶交叉 + DNN 高阶交叉，共享 embedding。
- 面试对应：Q027—Q030。
- 会议页面：https://www.ijcai.org/proceedings/2017/239

### DCN / DCN V2

- **Deep & Cross Network for Ad Click Predictions**
- 关键主题：显式 bounded-degree feature crossing。
- 论文：https://arxiv.org/abs/1708.05123

- **DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems**
- WWW 2021。
- 关键主题：matrix cross、low-rank、CrossNet-Mix、web-scale ranking。
- 面试对应：Q031、Q032。
- DOI：https://doi.org/10.1145/3442381.3450078

---

## 3. 用户兴趣与长序列

### DIN

- **Deep Interest Network for Click-Through Rate Prediction**
- 关键主题：target-aware local activation、动态兴趣表达。
- 面试对应：Q039—Q042。
- 论文：https://arxiv.org/abs/1706.06978

### DIEN

- **Deep Interest Evolution Network for Click-Through Rate Prediction**
- AAAI 2019。
- 关键主题：interest extractor、auxiliary loss、interest evolution、AUGRU。
- 面试对应：Q043—Q045。
- 官方会议页面：https://ojs.aaai.org/index.php/AAAI/article/view/4545

### SIM

- **Search-based User Interest Modeling with Lifelong Sequential Behavior Data for CTR Prediction**
- CIKM 2020。
- 关键主题：GSU / ESU、search-first long-sequence modeling。
- 面试对应：Q047—Q049。
- DOI：https://doi.org/10.1145/3340531.3412744

---

## 4. 多任务与 CVR

### MMoE

- **Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts**
- KDD 2018。
- 关键主题：shared experts、task-specific gates、task relatedness。
- 面试对应：Q051—Q054。
- DOI：https://doi.org/10.1145/3219819.3220007

### PLE

- **Progressive Layered Extraction (PLE): A Novel Multi-Task Learning Model for Personalized Recommendations**
- RecSys 2020。
- 关键主题：shared / task-specific experts、negative transfer、seesaw phenomenon。
- 面试对应：Q055、Q056。
- DOI：https://doi.org/10.1145/3383313.3412236

### ESMM

- **Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate**
- 关键主题：sample selection bias、data sparsity、pCTCVR = pCTR × pCVR。
- 面试对应：Q059—Q061。
- 论文：https://arxiv.org/abs/1804.07931

---

## 5. 2024—2026 推荐 Scaling 与生成式推荐

### HSTU / Generative Recommenders

- **Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations**
- ICML 2024。
- 关键主题：sequential transduction、HSTU、recommendation scaling law、长序列硬件效率。
- 面试对应：Q094—Q096、Q100。
- PMLR：https://proceedings.mlr.press/v235/zhai24a.html
- 官方实现：https://github.com/meta-recsys/generative-recommenders

阅读时要特别区分：论文报告的实验规模与结论，和自己所在业务的可复现条件。不要把“论文证明可 scaling”直接等价成“任何推荐业务都应该上超大模型”。

### RankMixer

- **RankMixer: Scaling Up Ranking Models in Industrial Recommenders**
- 2025。
- 关键主题：hardware-aware ranking、token mixing、MFU、Sparse-MoE、ranking scaling。
- 面试对应：Q098、Q100。
- 论文：https://arxiv.org/abs/2507.15551

RankMixer 的阅读重点不是记住参数规模，而是理解：传统 ranking 中大量 feature-crossing 小模块为何不能充分利用 GPU，以及“硬件友好架构”为什么可能让模型容量在相同 latency 下继续扩展。

---

## 建议的论文阅读方法

每篇论文至少回答 7 个问题：

1. **它解决了上一代什么具体失败模式？**
2. **最核心的归纳偏置是什么？**
3. **关键公式中的每一项改变了什么？**
4. **实验中的 baseline 是否公平？**
5. **提升来自模型结构、数据、参数规模还是系统优化？**
6. **上线需要付出什么 latency / memory / engineering cost？**
7. **如果把论文放到另一种业务分布，哪些假设最先失效？**

这 7 个问题比背论文结构图更接近真实推荐算法面试的追问方式。
