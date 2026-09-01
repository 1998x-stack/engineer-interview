# 核心白板公式

## SFT

\[
\mathcal L_{SFT}=-\sum_t\log\pi_\theta(y_t|x,y_{<t})
\]

## Reward Model / Bradley-Terry

\[
\mathcal L_{RM}=-\log\sigma(r_w-r_l)
\]

## PPO Ratio

\[
r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}
\]

## PPO Clip

\[
L^{CLIP}=\mathbb E[\min(r_tA_t,\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)A_t)]
\]

## GAE

\[
\delta_t=r_t+\gamma V_{t+1}-V_t
\]

\[
\hat A_t=\sum_l(\gamma\lambda)^l\delta_{t+l}
\]

## DPO

\[
\mathcal L_{DPO}=-\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y_w)}{\pi_{ref}(y_w)}-\log\frac{\pi_\theta(y_l)}{\pi_{ref}(y_l)}\right]\right)
\]

## GRPO Advantage

\[
\hat A_i=\frac{r_i-\operatorname{mean}(r_{group})}{\operatorname{std}(r_{group})+\varepsilon}
\]

## GSPO Sequence Ratio

\[
s_i=\left(\frac{\pi_\theta(y_i|x)}{\pi_{old}(y_i|x)}\right)^{1/|y_i|}
\]

> 白板技巧：公式本身只占 30%。剩下 70% 是“这个量从哪里来、解决什么偏差、何时失效、系统中谁计算它”。


<!-- GUIDE_V2 -->
## V2 · 公式不只要“会写”

每个公式都按六问检查：**随机变量从哪里采样？谁是优化变量？baseline/reference 是谁？归一化粒度是什么？数值尾部怎么处理？异步/分布式后哪个等式只剩近似？** 这六问比再背十个变体更接近实际算法面试。
