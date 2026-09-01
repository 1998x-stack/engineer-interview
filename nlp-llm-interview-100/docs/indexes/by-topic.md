# 按主题索引

## `alignment`

- [Q065 Pretraining 与 SFT 的本质区别](../06-alignment/Q065-pretraining-vs-sft.md)
- [Q066 LoRA 的低秩假设到底是什么？](../06-alignment/Q066-lora.md)
- [Q067 LoRA 应该加 Q/V 还是加所有 Linear？](../06-alignment/Q067-lora-target-modules.md)
- [Q068 QLoRA 为什么能在更小显存上微调大模型？](../06-alignment/Q068-qlora.md)
- [Q069 知识蒸馏有哪些层级？](../06-alignment/Q069-knowledge-distillation.md)
- [Q070 RLHF 的经典 Pipeline 与 KL 约束](../06-alignment/Q070-rlhf.md)
- [Q071 REINFORCE 是 On‑policy 还是 Off‑policy？](../06-alignment/Q071-reinforce-on-policy.md)
- [Q072 REINFORCE 为什么加 Baseline 不引入偏差？](../06-alignment/Q072-reinforce-baseline.md)
- [Q073 DPO 为什么不需要显式 Reward Model？](../06-alignment/Q073-dpo.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](../06-alignment/Q074-ppo-dpo-grpo.md)

## `attention`

- [Q034 Seq2Seq 为什么需要 Attention？](../03-representation-sequence/Q034-seq2seq-attention.md)
- [Q035 Self‑Attention 的完整计算流程](../04-transformer/Q035-self-attention.md)
- [Q036 为什么 Attention 要除以 sqrt(d_k)？](../04-transformer/Q036-attention-scaling.md)
- [Q038 Multi‑Head Attention 为什么不是一个大 Head？](../04-transformer/Q038-multi-head-attention.md)
- [Q039 Self‑Attention 的复杂度到底是多少？](../04-transformer/Q039-attention-complexity.md)
- [Q047 Transformer 为什么 Attention 后还需要 FFN？](../04-transformer/Q047-transformer-ffn.md)
- [Q094 Continuous Batching 与 PagedAttention 解决什么？](../09-inference-infra/Q094-continuous-batching-pagedattention.md)
- [Q098 手写 Multi‑Head Attention：Shape、Mask、Contiguous](../10-coding-debug/Q098-implement-mha.md)

## `auc`

- [Q003 AUC 的两种理解为什么等价？](../01-ml-foundations/Q003-auc-ranking-interpretation.md)

## `bert`

- [Q015 BERT 后为什么还要接 CRF？](../02-classical-nlp/Q015-bert-crf.md)
- [Q018 NER 模型为什么从 HMM 演化到 BERT/LLM？](../02-classical-nlp/Q018-ner-evolution.md)
- [Q051 BERT 原始预训练任务：MLM 与 NSP](../05-pretraining/Q051-bert-mlm-nsp.md)
- [Q052 为什么 BERT 不能天然像 GPT 一样左到右生成？](../05-pretraining/Q052-bert-vs-autoregressive-generation.md)
- [Q053 BERT 与 GPT：双向理解和因果生成如何取舍？](../05-pretraining/Q053-bert-vs-gpt.md)

## `bm25`

- [Q021 BM25 相比 TF‑IDF 改进了什么？](../02-classical-nlp/Q021-bm25.md)

## `calibration`

- [Q009 什么是概率校准 Calibration？](../01-ml-foundations/Q009-calibration.md)

## `classical-nlp`

- [Q013 HMM：三个基本问题与两条核心假设](../02-classical-nlp/Q013-hmm.md)
- [Q014 CRF 和 HMM 有什么根本区别？](../02-classical-nlp/Q014-crf-vs-hmm.md)
- [Q015 BERT 后为什么还要接 CRF？](../02-classical-nlp/Q015-bert-crf.md)
- [Q016 CRF 的 Emission 与 Transition Matrix 分别表示什么？](../02-classical-nlp/Q016-crf-emission-transition.md)
- [Q017 中文分词：传统方法与 LLM 时代如何看？](../02-classical-nlp/Q017-chinese-word-segmentation.md)
- [Q018 NER 模型为什么从 HMM 演化到 BERT/LLM？](../02-classical-nlp/Q018-ner-evolution.md)
- [Q019 n‑gram Language Model 的核心问题与 Kneser‑Ney 直觉](../02-classical-nlp/Q019-ngram-kneser-ney.md)
- [Q020 TF‑IDF 的公式、直觉与局限](../02-classical-nlp/Q020-tf-idf.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](../02-classical-nlp/Q021-bm25.md)
- [Q022 编辑距离：动态规划怎么写？如何降空间？](../02-classical-nlp/Q022-edit-distance.md)
- [Q023 文本分类方案如何随数据规模演进？](../02-classical-nlp/Q023-text-classification-evolution.md)
- [Q024 NLP 数据增强：怎么保证不破坏标签？](../02-classical-nlp/Q024-nlp-data-augmentation.md)

## `coding-debug`

- [Q097 手写 Numerical Stable Softmax](../10-coding-debug/Q097-stable-softmax.md)
- [Q098 手写 Multi‑Head Attention：Shape、Mask、Contiguous](../10-coding-debug/Q098-implement-mha.md)
- [Q099 Vectorized 1‑NN：禁止 Python For‑loop](../10-coding-debug/Q099-vectorized-1nn.md)
- [Q100 Transformer Debug + 实现 KV Cache：综合终局题](../10-coding-debug/Q100-transformer-debug-kv-cache.md)

## `crf`

- [Q014 CRF 和 HMM 有什么根本区别？](../02-classical-nlp/Q014-crf-vs-hmm.md)
- [Q015 BERT 后为什么还要接 CRF？](../02-classical-nlp/Q015-bert-crf.md)
- [Q016 CRF 的 Emission 与 Transition Matrix 分别表示什么？](../02-classical-nlp/Q016-crf-emission-transition.md)

## `data`

- [Q023 文本分类方案如何随数据规模演进？](../02-classical-nlp/Q023-text-classification-evolution.md)
- [Q024 NLP 数据增强：怎么保证不破坏标签？](../02-classical-nlp/Q024-nlp-data-augmentation.md)
- [Q061 为什么“数据质量越高越好”是危险说法？](../05-pretraining/Q061-data-quality-tradeoff.md)
- [Q085 预训练数据清洗 Pipeline 应如何设计？](../08-data-evaluation/Q085-pretraining-data-pipeline.md)
- [Q088 合成数据质量：Validity、Faithfulness、Diversity、Utility](../08-data-evaluation/Q088-synthetic-data-quality.md)

## `data-evaluation`

- [Q085 预训练数据清洗 Pipeline 应如何设计？](../08-data-evaluation/Q085-pretraining-data-pipeline.md)
- [Q086 Exact Dedup 与 MinHash：何时用哪一个？](../08-data-evaluation/Q086-exact-dedup-vs-minhash.md)
- [Q087 Benchmark Decontamination 为什么不能只做 Exact Match？](../08-data-evaluation/Q087-benchmark-decontamination.md)
- [Q088 合成数据质量：Validity、Faithfulness、Diversity、Utility](../08-data-evaluation/Q088-synthetic-data-quality.md)
- [Q089 LLM‑as‑a‑Judge 有哪些系统性偏差？](../08-data-evaluation/Q089-llm-as-judge.md)
- [Q090 离线指标涨了，为什么线上可能变差？](../08-data-evaluation/Q090-offline-online-gap.md)

## `dedup`

- [Q086 Exact Dedup 与 MinHash：何时用哪一个？](../08-data-evaluation/Q086-exact-dedup-vs-minhash.md)

## `dpo`

- [Q073 DPO 为什么不需要显式 Reward Model？](../06-alignment/Q073-dpo.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](../06-alignment/Q074-ppo-dpo-grpo.md)

## `gpt`

- [Q052 为什么 BERT 不能天然像 GPT 一样左到右生成？](../05-pretraining/Q052-bert-vs-autoregressive-generation.md)
- [Q053 BERT 与 GPT：双向理解和因果生成如何取舍？](../05-pretraining/Q053-bert-vs-gpt.md)

## `grpo`

- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](../06-alignment/Q074-ppo-dpo-grpo.md)

## `hmm`

- [Q013 HMM：三个基本问题与两条核心假设](../02-classical-nlp/Q013-hmm.md)
- [Q014 CRF 和 HMM 有什么根本区别？](../02-classical-nlp/Q014-crf-vs-hmm.md)
- [Q018 NER 模型为什么从 HMM 演化到 BERT/LLM？](../02-classical-nlp/Q018-ner-evolution.md)

## `inference-infra`

- [Q091 KV Cache 为什么能显著加速自回归 Decode？](../09-inference-infra/Q091-kv-cache.md)
- [Q092 KV Cache 大小怎么估算？](../09-inference-infra/Q092-kv-cache-memory.md)
- [Q093 Quantization 为什么能提升 LLM 推理吞吐？](../09-inference-infra/Q093-quantization.md)
- [Q094 Continuous Batching 与 PagedAttention 解决什么？](../09-inference-infra/Q094-continuous-batching-pagedattention.md)
- [Q095 Speculative Decoding 为什么能“保证分布”又加速？](../09-inference-infra/Q095-speculative-decoding.md)
- [Q096 DP、TP、PP、EP：四种并行怎么组合？](../09-inference-infra/Q096-distributed-parallelism.md)

## `kv-cache`

- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](../04-transformer/Q050-mha-mqa-gqa.md)
- [Q091 KV Cache 为什么能显著加速自回归 Decode？](../09-inference-infra/Q091-kv-cache.md)
- [Q092 KV Cache 大小怎么估算？](../09-inference-infra/Q092-kv-cache-memory.md)
- [Q100 Transformer Debug + 实现 KV Cache：综合终局题](../10-coding-debug/Q100-transformer-debug-kv-cache.md)

## `llm`

- [Q017 中文分词：传统方法与 LLM 时代如何看？](../02-classical-nlp/Q017-chinese-word-segmentation.md)
- [Q018 NER 模型为什么从 HMM 演化到 BERT/LLM？](../02-classical-nlp/Q018-ner-evolution.md)
- [Q049 SwiGLU 为什么成了现代 LLM 常客？](../04-transformer/Q049-swiglu.md)
- [Q055 为什么 LLM 普遍使用 Subword/Byte Tokenization？](../05-pretraining/Q055-subword-byte-tokenization.md)
- [Q089 LLM‑as‑a‑Judge 有哪些系统性偏差？](../08-data-evaluation/Q089-llm-as-judge.md)
- [Q093 Quantization 为什么能提升 LLM 推理吞吐？](../09-inference-infra/Q093-quantization.md)

## `lora`

- [Q066 LoRA 的低秩假设到底是什么？](../06-alignment/Q066-lora.md)
- [Q067 LoRA 应该加 Q/V 还是加所有 Linear？](../06-alignment/Q067-lora-target-modules.md)
- [Q068 QLoRA 为什么能在更小显存上微调大模型？](../06-alignment/Q068-qlora.md)

## `ml-foundations`

- [Q001 为什么分类任务通常用交叉熵而不是 MSE？](../01-ml-foundations/Q001-cross-entropy-vs-mse.md)
- [Q002 Precision、Recall、F1：什么时候 Accuracy 会骗人？](../01-ml-foundations/Q002-precision-recall-f1.md)
- [Q003 AUC 的两种理解为什么等价？](../01-ml-foundations/Q003-auc-ranking-interpretation.md)
- [Q004 L1、L2 正则化与 MAP 的关系](../01-ml-foundations/Q004-l1-l2-map.md)
- [Q005 Bias‑Variance Trade‑off 在大模型时代还成立吗？](../01-ml-foundations/Q005-bias-variance.md)
- [Q006 BatchNorm 与 LayerNorm：Transformer 为什么偏爱 LN？](../01-ml-foundations/Q006-batchnorm-vs-layernorm.md)
- [Q007 Dropout 为什么有效？大模型里为什么常变少？](../01-ml-foundations/Q007-dropout.md)
- [Q008 类别极度不平衡怎么处理？](../01-ml-foundations/Q008-class-imbalance.md)
- [Q009 什么是概率校准 Calibration？](../01-ml-foundations/Q009-calibration.md)
- [Q010 贝叶斯基准率陷阱：99% 准确率为何不代表 99% 可信？](../01-ml-foundations/Q010-bayes-base-rate.md)
- [Q011 超长文件如何等概率抽取 k 行？Reservoir Sampling](../01-ml-foundations/Q011-reservoir-sampling.md)
- [Q012 Adam 与 AdamW 到底差在哪？](../01-ml-foundations/Q012-adam-vs-adamw.md)

## `moe`

- [Q064 MoE：为什么参数变大但每 token 计算不同比例增长？](../05-pretraining/Q064-moe.md)

## `ner`

- [Q018 NER 模型为什么从 HMM 演化到 BERT/LLM？](../02-classical-nlp/Q018-ner-evolution.md)

## `optimizer`

- [Q012 Adam 与 AdamW 到底差在哪？](../01-ml-foundations/Q012-adam-vs-adamw.md)

## `ppo`

- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](../06-alignment/Q074-ppo-dpo-grpo.md)

## `pretraining`

- [Q051 BERT 原始预训练任务：MLM 与 NSP](../05-pretraining/Q051-bert-mlm-nsp.md)
- [Q052 为什么 BERT 不能天然像 GPT 一样左到右生成？](../05-pretraining/Q052-bert-vs-autoregressive-generation.md)
- [Q053 BERT 与 GPT：双向理解和因果生成如何取舍？](../05-pretraining/Q053-bert-vs-gpt.md)
- [Q054 BPE、WordPiece、Unigram/SentencePiece 有什么区别？](../05-pretraining/Q054-bpe-wordpiece-unigram.md)
- [Q055 为什么 LLM 普遍使用 Subword/Byte Tokenization？](../05-pretraining/Q055-subword-byte-tokenization.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](../05-pretraining/Q056-decoder-lm-loss.md)
- [Q057 Perplexity：什么时候能比、什么时候不能比？](../05-pretraining/Q057-perplexity.md)
- [Q058 Weight Tying：为什么输入 Embedding 与 LM Head 可以共享？](../05-pretraining/Q058-weight-tying.md)
- [Q059 Scaling Law：为什么不能只堆参数？](../05-pretraining/Q059-scaling-laws.md)
- [Q060 大模型训练为什么必须去重？](../05-pretraining/Q060-pretraining-dedup.md)
- [Q061 为什么“数据质量越高越好”是危险说法？](../05-pretraining/Q061-data-quality-tradeoff.md)
- [Q062 Mixed Precision：BF16 为什么常比 FP16 稳？](../05-pretraining/Q062-mixed-precision.md)
- [Q063 Gradient Checkpointing：省了什么、付出什么？](../05-pretraining/Q063-gradient-checkpointing.md)
- [Q064 MoE：为什么参数变大但每 token 计算不同比例增长？](../05-pretraining/Q064-moe.md)

## `quantization`

- [Q093 Quantization 为什么能提升 LLM 推理吞吐？](../09-inference-infra/Q093-quantization.md)

## `rag`

- [Q081 RAG Chunking：为什么“固定 500 tokens”不是答案？](../07-retrieval-rag/Q081-rag-chunking.md)
- [Q084 如何完整评估一个 RAG 系统？](../07-retrieval-rag/Q084-rag-evaluation.md)

## `representation-sequence`

- [Q025 CBOW 与 Skip‑Gram：输入输出正好相反吗？](../03-representation-sequence/Q025-cbow-vs-skipgram.md)
- [Q026 Word2Vec 为什么需要 Negative Sampling？](../03-representation-sequence/Q026-negative-sampling.md)
- [Q027 Hierarchical Softmax 为什么是 O(log|V|)？](../03-representation-sequence/Q027-hierarchical-softmax.md)
- [Q028 SGNS 为什么与 PMI Matrix Factorization 有关系？](../03-representation-sequence/Q028-sgns-pmi.md)
- [Q029 GloVe 与 Word2Vec 的差异](../03-representation-sequence/Q029-glove-vs-word2vec.md)
- [Q030 静态词向量为什么解决不了一词多义？](../03-representation-sequence/Q030-contextual-embeddings.md)
- [Q031 RNN 为什么梯度消失/爆炸？](../03-representation-sequence/Q031-rnn-gradient.md)
- [Q032 LSTM 为什么缓解长依赖问题？](../03-representation-sequence/Q032-lstm-long-dependency.md)
- [Q033 GRU 与 LSTM 怎么选？](../03-representation-sequence/Q033-gru-vs-lstm.md)
- [Q034 Seq2Seq 为什么需要 Attention？](../03-representation-sequence/Q034-seq2seq-attention.md)

## `retrieval`

- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](../07-retrieval-rag/Q075-sparse-vs-dense-retrieval.md)
- [Q077 为什么搜索系统通常是多阶段 Retrieval→Rerank？](../07-retrieval-rag/Q077-multi-stage-retrieval.md)
- [Q078 Dense Retrieval 的负样本怎么构造？](../07-retrieval-rag/Q078-dense-retrieval-negatives.md)

## `retrieval-rag`

- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](../07-retrieval-rag/Q075-sparse-vs-dense-retrieval.md)
- [Q076 Bi‑Encoder 与 Cross‑Encoder：为什么一快一准？](../07-retrieval-rag/Q076-biencoder-vs-crossencoder.md)
- [Q077 为什么搜索系统通常是多阶段 Retrieval→Rerank？](../07-retrieval-rag/Q077-multi-stage-retrieval.md)
- [Q078 Dense Retrieval 的负样本怎么构造？](../07-retrieval-rag/Q078-dense-retrieval-negatives.md)
- [Q079 HNSW：为什么多层小世界图能快速 ANN？](../07-retrieval-rag/Q079-hnsw.md)
- [Q080 IVF‑PQ：如何用聚类与乘积量化压缩十亿向量？](../07-retrieval-rag/Q080-ivf-pq.md)
- [Q081 RAG Chunking：为什么“固定 500 tokens”不是答案？](../07-retrieval-rag/Q081-rag-chunking.md)
- [Q082 Hybrid Search 与 RRF：为什么排名融合常比 raw score 加权稳？](../07-retrieval-rag/Q082-hybrid-search-rrf.md)
- [Q083 为什么 Reranker 通常比 Retriever 更准？](../07-retrieval-rag/Q083-reranker.md)
- [Q084 如何完整评估一个 RAG 系统？](../07-retrieval-rag/Q084-rag-evaluation.md)

## `rlhf`

- [Q070 RLHF 的经典 Pipeline 与 KL 约束](../06-alignment/Q070-rlhf.md)

## `rope`

- [Q043 RoPE：如何把相对位置写进 QK 点积？](../04-transformer/Q043-rope.md)
- [Q044 为什么 RoPE 通常只作用于 Q/K，不作用于 V？](../04-transformer/Q044-rope-qk-not-v.md)
- [Q045 RoPE 为什么会有长度外推问题？YaRN/PI 在解决什么？](../04-transformer/Q045-rope-context-extension.md)

## `sft`

- [Q065 Pretraining 与 SFT 的本质区别](../06-alignment/Q065-pretraining-vs-sft.md)

## `softmax`

- [Q027 Hierarchical Softmax 为什么是 O(log|V|)？](../03-representation-sequence/Q027-hierarchical-softmax.md)
- [Q097 手写 Numerical Stable Softmax](../10-coding-debug/Q097-stable-softmax.md)

## `tokenizer`

- [Q055 为什么 LLM 普遍使用 Subword/Byte Tokenization？](../05-pretraining/Q055-subword-byte-tokenization.md)

## `transformer`

- [Q035 Self‑Attention 的完整计算流程](../04-transformer/Q035-self-attention.md)
- [Q036 为什么 Attention 要除以 sqrt(d_k)？](../04-transformer/Q036-attention-scaling.md)
- [Q037 为什么 Q、K、V 要用不同投影？](../04-transformer/Q037-qkv-projections.md)
- [Q038 Multi‑Head Attention 为什么不是一个大 Head？](../04-transformer/Q038-multi-head-attention.md)
- [Q039 Self‑Attention 的复杂度到底是多少？](../04-transformer/Q039-attention-complexity.md)
- [Q040 Causal Mask 是怎么工作的？](../04-transformer/Q040-causal-mask.md)
- [Q041 为什么 Transformer 必须注入位置信息？](../04-transformer/Q041-position-information.md)
- [Q042 Sinusoidal Positional Encoding 的设计直觉](../04-transformer/Q042-sinusoidal-position.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](../04-transformer/Q043-rope.md)
- [Q044 为什么 RoPE 通常只作用于 Q/K，不作用于 V？](../04-transformer/Q044-rope-qk-not-v.md)
- [Q045 RoPE 为什么会有长度外推问题？YaRN/PI 在解决什么？](../04-transformer/Q045-rope-context-extension.md)
- [Q046 Pre‑LN 与 Post‑LN：为什么深层模型更偏 Pre‑Norm？](../04-transformer/Q046-preln-vs-postln.md)
- [Q047 Transformer 为什么 Attention 后还需要 FFN？](../04-transformer/Q047-transformer-ffn.md)
- [Q048 GELU、ReLU 与 SiLU/SwiGLU 怎么比较？](../04-transformer/Q048-activation-functions.md)
- [Q049 SwiGLU 为什么成了现代 LLM 常客？](../04-transformer/Q049-swiglu.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](../04-transformer/Q050-mha-mqa-gqa.md)

## `word2vec`

- [Q026 Word2Vec 为什么需要 Negative Sampling？](../03-representation-sequence/Q026-negative-sampling.md)
- [Q029 GloVe 与 Word2Vec 的差异](../03-representation-sequence/Q029-glove-vs-word2vec.md)
