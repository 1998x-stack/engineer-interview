# 算法演化：从 Failure Mode 反推方法

## PPO -> GRPO -> DAPO

```mermaid
flowchart TD
    PPO[PPO: Actor + Critic] -->|Critic costly| GRPO[GRPO: group-relative baseline]
    GRPO --> F1[Entropy collapse]
    GRPO --> F2[All-correct/all-wrong groups]
    GRPO --> F3[Long-CoT weighting]
    GRPO --> F4[Overlong reward cliff]
    F1 --> DAPO[DAPO]
    F2 --> DAPO
    F3 --> DAPO
    F4 --> DAPO
    DAPO --> T1[Clip-Higher]
    DAPO --> T2[Dynamic Sampling]
    DAPO --> T3[Token-level PG]
    DAPO --> T4[Overlong Reward Shaping]
```

## GRPO -> GSPO

```mermaid
flowchart TD
    GRPO[GRPO token-level ratio] --> N[Token ratio noise / long training instability]
    N --> M[MoE routing mismatch]
    M --> GSPO[GSPO sequence-level ratio & clipping]
```

**核心原则**：不要说“因为算法更新”。要说“我观察到了某个具体 failure，因此这个机制是最小必要改动”。


<!-- GUIDE_V2 -->
## V2 · Failure-Driven 决策原则

不要把 PPO→GRPO→DAPO/GSPO 画成“新算法替代旧算法”的时间线。更准确的是：**critic 成本、group 退化、长序列权重、entropy、MoE/back-end mismatch、policy freshness** 分别触发不同修正；只在观测到对应 failure 时升级方法。
