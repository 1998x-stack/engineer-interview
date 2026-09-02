# 附录 A · 核心公式速查

## BM25

$$BM25(D,Q)=\sum_{q_i\in Q} IDF(q_i)\frac{f(q_i,D)(k_1+1)}{f(q_i,D)+k_1(1-b+b|D|/avgdl)}$$

- `k1`：TF saturation。
- `b`：长度归一化。

## NDCG

$$DCG@K=\sum_{i=1}^{K}\frac{2^{rel_i}-1}{\log_2(i+1)},\quad NDCG@K=DCG@K/IDCG@K$$

## RankNet

$$P_{ij}=\sigma(s_i-s_j)$$

LambdaRank 进一步按交换结果导致的 $|\Delta NDCG|$ 对 pairwise 梯度加权。

## Dense Contrastive Loss

$$L=-\log\frac{e^{s(q,d^+)/\tau}}{e^{s(q,d^+)/\tau}+\sum_j e^{s(q,d_j^-)/\tau}}$$

## RRF

$$RRF(d)=\sum_{r\in R}\frac{1}{k+rank_r(d)}$$

## Unit-vector: Cosine / IP / L2

$$\|x-y\|_2^2=2-2x^Ty$$

## IPS

$$\hat R=\frac1n\sum_i\frac{c_i}{p_i}\ell_i$$
