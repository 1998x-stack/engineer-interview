# 手撕代码骨架

这些文件不是完整训练框架，而是面试时应该能独立写出的 **最小核心**。建议顺序：先关掉自动补全自己实现，再运行 tiny test 对比。

| 文件 | 对应题 | 必须理解的 shape / stop-gradient |
|---|---|---|
| `dqn_loss.py` | Q017/Q022 | `[B,A] → gather [B]`，target no-grad，terminal mask |
| `ppo_gae.py` | Q036/Q039/Q048 | `[T,B]` 或 `[B,T]` mask，old logp detach，倒序 GAE |
| `ddpg_losses.py` | Q050/Q051 | critic target no-grad，actor 通过 critic 对 action 求梯度 |
| `td3_target.py` | Q052/Q053 | twin target Q、target action smoothing |
| `sac_losses.py` | Q054/Q055 | reparameterized action、entropy/log-prob、temperature |
| `reward_model_loss.py` | Q073 | pairwise reward difference → log-sigmoid |
| `dpo_loss.py` | Q079/Q080 | chosen/rejected policy-reference log-ratio |
| `grpo_core.py` | Q081/Q083/Q099 | `[B,G,T]`、group normalize、response mask、ratio/clip |

## 手撕代码评分标准

### 60 分：能写出主公式

但没有 shape、mask、terminal、detach 意识。

### 80 分：实现正确

- 明确 tensor shape；
- target 分支 stop-gradient；
- padding/response mask 正确；
- log-space ratio；
- 数值稳定处理 `std≈0`、`log(0)` 等边界。

### 90+ 分：可验证

为核心函数写 3 类 tiny test：

1. **手工可算样例**：2~4 个元素，结果能人工核对；
2. **边界样例**：terminal、全 padding、zero-variance group；
3. **梯度样例**：确认应该有梯度的参数有梯度，target/reference 没梯度。

## 推荐练习顺序

`DQN target → GAE → PPO clip → TD3 target → SAC actor loss → RM → DPO → GRPO`。
