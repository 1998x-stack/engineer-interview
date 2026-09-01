# 高频公式速查

> 只用来快速回忆；正式面试要能解释每个公式的假设与含义。

## [Q001 为什么分类任务通常用交叉熵而不是 MSE？](../01-ml-foundations/Q001-cross-entropy-vs-mse.md)

- $p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}$
- $\mathcal L=-\sum_k y_k\log p_k$
- $\frac{\partial \mathcal L}{\partial z_k}=p_k-y_k$

## [Q002 Precision、Recall、F1：什么时候 Accuracy 会骗人？](../01-ml-foundations/Q002-precision-recall-f1.md)

- $P=\frac{TP}{TP+FP}$
- $R=\frac{TP}{TP+FN}$
- $F_1=\frac{2PR}{P+R}$

## [Q003 AUC 的两种理解为什么等价？](../01-ml-foundations/Q003-auc-ranking-interpretation.md)

- $\mathrm{AUC}=P(s(x^+)>s(x^-))$

## [Q004 L1、L2 正则化与 MAP 的关系](../01-ml-foundations/Q004-l1-l2-map.md)

- $\mathcal L_{L1}=\mathcal L+\lambda\|w\|_1$
- $\mathcal L_{L2}=\mathcal L+\lambda\|w\|_2^2$

## [Q005 Bias‑Variance Trade‑off 在大模型时代还成立吗？](../01-ml-foundations/Q005-bias-variance.md)

- $\mathbb E[(y-\hat f(x))^2]=\mathrm{Bias}^2+\mathrm{Variance}+\sigma^2$

## [Q006 BatchNorm 与 LayerNorm：Transformer 为什么偏爱 LN？](../01-ml-foundations/Q006-batchnorm-vs-layernorm.md)

- $\mathrm{LN}(x)=\gamma\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}+\beta$

## [Q009 什么是概率校准 Calibration？](../01-ml-foundations/Q009-calibration.md)

- $\mathrm{ECE}=\sum_m\frac{|B_m|}{n}\,|\mathrm{acc}(B_m)-\mathrm{conf}(B_m)|$

## [Q010 贝叶斯基准率陷阱：99% 准确率为何不代表 99% 可信？](../01-ml-foundations/Q010-bayes-base-rate.md)

- $P(D|+)=\frac{P(+|D)P(D)}{P(+|D)P(D)+P(+|\neg D)P(\neg D)}$

## [Q011 超长文件如何等概率抽取 k 行？Reservoir Sampling](../01-ml-foundations/Q011-reservoir-sampling.md)

- $P(\text{item }i\text{ survives})=\frac{k}{N}$

## [Q012 Adam 与 AdamW 到底差在哪？](../01-ml-foundations/Q012-adam-vs-adamw.md)

- $\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}$

## [Q013 HMM：三个基本问题与两条核心假设](../02-classical-nlp/Q013-hmm.md)

- $P(x,z)=P(z_1)\prod_{t=2}^T P(z_t|z_{t-1})\prod_{t=1}^T P(x_t|z_t)$

## [Q014 CRF 和 HMM 有什么根本区别？](../02-classical-nlp/Q014-crf-vs-hmm.md)

- $P(y|x)=\frac{\exp s(x,y)}{\sum_{y\prime}\exp s(x,y\prime)}$

## [Q015 BERT 后为什么还要接 CRF？](../02-classical-nlp/Q015-bert-crf.md)

- $s(x,y)=\sum_i E_{i,y_i}+\sum_i A_{y_{i-1},y_i}$

## [Q016 CRF 的 Emission 与 Transition Matrix 分别表示什么？](../02-classical-nlp/Q016-crf-emission-transition.md)

- $s(x,y)=\sum_i \mathrm{Emission}_i(y_i)+\sum_i\mathrm{Transition}(y_{i-1},y_i)$

## [Q019 n‑gram Language Model 的核心问题与 Kneser‑Ney 直觉](../02-classical-nlp/Q019-ngram-kneser-ney.md)

- $P(w_{1:T})\approx\prod_t P(w_t|w_{t-n+1:t-1})$

## [Q020 TF‑IDF 的公式、直觉与局限](../02-classical-nlp/Q020-tf-idf.md)

- $\mathrm{TFIDF}(t,d)=\mathrm{TF}(t,d)\cdot \log\frac{N}{df(t)}$

## [Q021 BM25 相比 TF‑IDF 改进了什么？](../02-classical-nlp/Q021-bm25.md)

- $\mathrm{BM25}(D,Q)=\sum_{q\in Q}\mathrm{IDF}(q)\frac{f(q,D)(k_1+1)}{f(q,D)+k_1(1-b+b|D|/\mathrm{avgdl})}$

## [Q022 编辑距离：动态规划怎么写？如何降空间？](../02-classical-nlp/Q022-edit-distance.md)

- $dp[i][j]=\min\{dp[i-1][j]+1,\;dp[i][j-1]+1,\;dp[i-1][j-1]+[s_i\neq t_j]\}$

## [Q026 Word2Vec 为什么需要 Negative Sampling？](../03-representation-sequence/Q026-negative-sampling.md)

- $\log\sigma(v_o^\top v_i)+\sum_{k=1}^K\log\sigma(-v_k^\top v_i)$

## [Q028 SGNS 为什么与 PMI Matrix Factorization 有关系？](../03-representation-sequence/Q028-sgns-pmi.md)

- $\mathrm{SGNS}\;\approx\;\mathrm{PMI}(w,c)-\log k$

## [Q029 GloVe 与 Word2Vec 的差异](../03-representation-sequence/Q029-glove-vs-word2vec.md)

- $J=\sum_{ij}f(X_{ij})(w_i^\top\tilde w_j+b_i+\tilde b_j-\log X_{ij})^2$

## [Q031 RNN 为什么梯度消失/爆炸？](../03-representation-sequence/Q031-rnn-gradient.md)

- $\frac{\partial h_t}{\partial h_{t-k}}=\prod_i J_i$

## [Q032 LSTM 为什么缓解长依赖问题？](../03-representation-sequence/Q032-lstm-long-dependency.md)

- $c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t$

## [Q034 Seq2Seq 为什么需要 Attention？](../03-representation-sequence/Q034-seq2seq-attention.md)

- $c_t=\sum_i \alpha_{ti}h_i$

## [Q035 Self‑Attention 的完整计算流程](../04-transformer/Q035-self-attention.md)

- $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})V$

## [Q036 为什么 Attention 要除以 sqrt(d_k)？](../04-transformer/Q036-attention-scaling.md)

- $\mathrm{Var}(q^\top k)\approx d_k$

## [Q039 Self‑Attention 的复杂度到底是多少？](../04-transformer/Q039-attention-complexity.md)

- $\mathrm{time}=O(T^2d),\quad \mathrm{attention\ memory}=O(T^2)$

## [Q043 RoPE：如何把相对位置写进 QK 点积？](../04-transformer/Q043-rope.md)

- $q_m^\top k_n=(R_m q)^\top(R_n k)=q^\top R_{n-m}k$

## [Q046 Pre‑LN 与 Post‑LN：为什么深层模型更偏 Pre‑Norm？](../04-transformer/Q046-preln-vs-postln.md)

- $x_{l+1}=x_l+F(\mathrm{LN}(x_l))\quad\text{(Pre-LN)}$

## [Q047 Transformer 为什么 Attention 后还需要 FFN？](../04-transformer/Q047-transformer-ffn.md)

- $\mathrm{FFN}(x)=W_2\,\phi(W_1x)$

## [Q049 SwiGLU 为什么成了现代 LLM 常客？](../04-transformer/Q049-swiglu.md)

- $\mathrm{SwiGLU}(x)=W_3(\mathrm{SiLU}(xW_1)\odot xW_2)$

## [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](../05-pretraining/Q056-decoder-lm-loss.md)

- $\mathcal L=-\sum_{t=1}^T\log P_\theta(x_t|x_{<t})$

## [Q057 Perplexity：什么时候能比、什么时候不能比？](../05-pretraining/Q057-perplexity.md)

- $\mathrm{PPL}=\exp\left(-\frac1N\sum_i\log P(x_i|x_{<i})\right)$

## [Q058 Weight Tying：为什么输入 Embedding 与 LM Head 可以共享？](../05-pretraining/Q058-weight-tying.md)

- $W_{\mathrm{LM\ head}}=E^\top$

## [Q066 LoRA 的低秩假设到底是什么？](../06-alignment/Q066-lora.md)

- $W=W_0+\Delta W,\quad \Delta W=BA,\quad \mathrm{rank}(BA)\le r$

## [Q070 RLHF 的经典 Pipeline 与 KL 约束](../06-alignment/Q070-rlhf.md)

- $\max_\theta\;\mathbb E[r(x,y)]-\beta\,\mathrm{KL}(\pi_\theta\|\pi_{ref})$

## [Q071 REINFORCE 是 On‑policy 还是 Off‑policy？](../06-alignment/Q071-reinforce-on-policy.md)

- $\nabla_\theta J=\mathbb E[R\nabla_\theta\log\pi_\theta(a|s)]$

## [Q072 REINFORCE 为什么加 Baseline 不引入偏差？](../06-alignment/Q072-reinforce-baseline.md)

- $\mathbb E[(R-b(s))\nabla\log\pi(a|s)]$

## [Q073 DPO 为什么不需要显式 Reward Model？](../06-alignment/Q073-dpo.md)

- $\mathcal L_{DPO}=-\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right)$

## [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](../07-retrieval-rag/Q075-sparse-vs-dense-retrieval.md)

- $s(q,d)=e_q^\top e_d$

## [Q082 Hybrid Search 与 RRF：为什么排名融合常比 raw score 加权稳？](../07-retrieval-rag/Q082-hybrid-search-rrf.md)

- $\mathrm{RRF}(d)=\sum_j\frac1{k+\mathrm{rank}_j(d)}$

## [Q084 如何完整评估一个 RAG 系统？](../07-retrieval-rag/Q084-rag-evaluation.md)

- $P(\mathrm{correct})\approx P(\mathrm{retrieve\ evidence})\times P(\mathrm{answer\ correct}|\mathrm{evidence})$

## [Q086 Exact Dedup 与 MinHash：何时用哪一个？](../08-data-evaluation/Q086-exact-dedup-vs-minhash.md)

- $J(A,B)=\frac{|A\cap B|}{|A\cup B|}$
- $P[h_{min}(A)=h_{min}(B)]=J(A,B)$

## [Q092 KV Cache 大小怎么估算？](../09-inference-infra/Q092-kv-cache-memory.md)

- $\mathrm{KV\ bytes}=2\times L\times T\times H_{kv}\times D_h\times \mathrm{bytes\ per\ element}$

## [Q099 Vectorized 1‑NN：禁止 Python For‑loop](../10-coding-debug/Q099-vectorized-1nn.md)

- $\|q-x\|^2=\|q\|^2+\|x\|^2-2q^\top x$
