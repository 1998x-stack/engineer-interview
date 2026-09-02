# 强化学习公式总表 · Interview Formula Sheet

> 目标：只保留面试中最常需要“现场写出来并解释”的公式。每个公式都附带使用条件与常见误区。

## 1. Return / Value / Advantage

\[
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
\]

\[
V^\pi(s)=\mathbb E_\pi[G_t|s_t=s],\quad
Q^\pi(s,a)=\mathbb E_\pi[G_t|s_t=s,a_t=a]
\]

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s),\qquad
\mathbb E_{a\sim\pi}[A^\pi(s,a)]=0
\]

**误区**：Advantage 不是新的价值定义，而是以状态基线中心化后的 action value。

## 2. Bellman

\[
V^\pi(s)=\mathbb E_\pi[r+\gamma V^\pi(s')]
\]

\[
Q^*(s,a)=\mathbb E[r+\gamma\max_{a'}Q^*(s',a')]
\]

terminal target：

\[
y=r+\gamma(1-d)V(s')
\]

其中 `d` 必须对应真正不可继续 bootstrap 的终止语义。

## 3. MC / TD / n-step / GAE

\[
\delta_t=r_t+\gamma V(s_{t+1})-V(s_t)
\]

\[
G_t^{(n)}=\sum_{k=0}^{n-1}\gamma^kr_{t+k}+\gamma^nV(s_{t+n})
\]

\[
\hat A_t^{GAE}=\sum_{l=0}^{\infty}(\gamma\lambda)^l\delta_{t+l}
\]

`λ→0` 更接近短 bootstrap；`λ→1` 更接近长 return。

## 4. Importance Sampling

\[
\mathbb E_p[f(x)] = \mathbb E_q\left[\frac{p(x)}{q(x)}f(x)\right]
\]

PPO ratio：

\[
r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}
=\exp(\log\pi_\theta-\log\pi_{old})
\]

## 5. Q-learning / DQN / Double DQN

\[
Q(s,a)\leftarrow Q(s,a)+\alpha[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]
\]

DQN：

\[
y=r+\gamma(1-d)\max_{a'}Q_{\theta^-}(s',a')
\]

Double DQN：

\[
a^*=\arg\max_aQ_\theta(s',a),\qquad
y=r+\gamma Q_{\theta^-}(s',a^*)
\]

## 6. Policy Gradient / Actor-Critic

\[
\nabla_\theta J(\theta)=\mathbb E[\nabla_\theta\log\pi_\theta(a|s)Q^\pi(s,a)]
\]

baseline 后：

\[
\nabla J=\mathbb E[\nabla\log\pi(a|s)A(s,a)]
\]

## 7. TRPO / PPO

TRPO：

\[
\max_\theta\;\mathbb E[r_t(\theta)A_t]
\quad s.t.\quad
\mathbb E[D_{KL}(\pi_{old}\|\pi_\theta)]\le\delta
\]

PPO：

\[
L^{CLIP}=\mathbb E\left[\min\left(r_t\hat A_t,
\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)\hat A_t\right)\right]
\]

完整实现常见：

\[
L_{total}=-L^{CLIP}+c_vL_V-c_eH(\pi)+\beta KL
\]

## 8. DDPG / TD3 / SAC

DDPG critic target：

\[
y=r+\gamma Q_{\phi^-}(s',\mu_{\theta^-}(s'))
\]

TD3：

\[
y=r+\gamma\min(Q_1^-,Q_2^-)(s',\mu^-(s')+\epsilon)
\]

SAC：

\[
J(\pi)=\mathbb E\left[\sum_t\gamma^t(r_t+\alpha H(\pi(\cdot|s_t)))\right]
\]

## 9. Offline RL

CQL（离散动作直观形式）：

\[
L_{CQL}=L_{Bellman}+\alpha\left(
\mathbb E_s[\log\sum_a e^{Q(s,a)}]-\mathbb E_{(s,a)\sim D}[Q(s,a)]
\right)
\]

IQL 三步：expectile `V` → Bellman `Q` → advantage-weighted BC。

## 10. Reward Model / DPO

RM pairwise：

\[
L_{RM}=-\log\sigma(r(x,y_w)-r(x,y_l))
\]

DPO：

\[
L_{DPO}=-\log\sigma\left(\beta\left[
\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-
\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}
\right]\right)
\]

## 11. GRPO / LLM RL

组内相对 advantage 的直观形式：

\[
A_i=\frac{r_i-\bar r}{\operatorname{std}(r)+\varepsilon}
\]

要区分：

- old log-prob：用于 policy update ratio；
- reference log-prob：用于 KL anchor；
- group reward：用于相对 baseline；
- token mask：决定哪些 token 真正进入 loss。

## 12. 公式面试自查

现场写任何式子后，强制回答四个问题：

1. 期望对哪个分布取？
2. 哪些量来自 rollout，哪些来自 learned estimator？
3. 哪些项必须 stop-gradient？
4. terminal / padding / response mask 怎么处理？
