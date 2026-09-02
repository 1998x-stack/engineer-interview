# RL / Sim2Real 路线

```mermaid
flowchart LR
  MDP --> PPO
  MDP --> SAC
  PPO --> SIM[Parallel Simulation]
  SAC --> SIM
  SIM --> DR[Domain Randomization]
  DR --> SYSID[System Identification]
  SYSID --> REAL[Real Robot]
  REAL --> FAIL[Failure Mining]
  FAIL --> RL[VLA/Policy RL Refinement]
```

## 高频主线

- MDP / Bellman
- PPO clipped objective + GAE
- SAC entropy-regularized objective
- Reward shaping / reward hacking
- Parallel simulation / Isaac Lab
- Domain Randomization + system identification
- Sim2Real gap taxonomy
- Real robot online RL safety / reset / BC regularization
