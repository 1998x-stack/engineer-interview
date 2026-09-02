# Primary Papers / 官方资料

本仓库扩展内容优先链接原论文或官方出版页。PDF 中的算法结论保持原口径，新增说明尽量用 primary source 校验。

- **sutton-barto** — [Reinforcement Learning: An Introduction (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html)
- **dqn** — [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236)
- **double-dqn** — [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461)
- **dueling** — [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581)
- **per** — [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)
- **distributional** — [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887)
- **rainbow** — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298)
- **a3c** — [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783)
- **gae** — [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438)
- **trpo** — [Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477)
- **ppo** — [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- **ddpg** — [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)
- **td3** — [Addressing Function Approximation Error in Actor-Critic Methods](https://proceedings.mlr.press/v80/fujimoto18a.html)
- **sac** — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html)
- **cql** — [Conservative Q-Learning for Offline Reinforcement Learning](https://arxiv.org/abs/2006.04779)
- **iql** — [Offline Reinforcement Learning with Implicit Q-Learning](https://arxiv.org/abs/2110.06169)
- **qmix** — [QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1803.11485)
- **domain-rand** — [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907)
- **instructgpt** — [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- **dpo** — [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
- **deepseekmath** — [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)
- **deepseek-r1** — [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z)
- **dapo** — [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- **gspo** — [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071)

## 2026 面试阅读顺序

1. Sutton & Barto：MDP / Bellman / TD / policy gradient 基础。
2. DQN → Double/Dueling/PER/Distributional/Rainbow：value-based 演化。
3. GAE → TRPO → PPO：policy optimization 主线。
4. DDPG → TD3 → SAC：连续控制主线。
5. CQL / IQL：offline distribution shift。
6. InstructGPT → DPO → DeepSeekMath/GRPO → DeepSeek-R1 → DAPO → GSPO：LLM post-training RL。
