# 学习路线

题号很多，但 Quant 面试准备不应按 001→100 机械线性推进。推荐按“先建立研究可信度，再扩展专业方向”的方式学习。

## 1. 通用 QR / Financial ML 主路线

```text
A 概率
  ↓
B 统计推断
  ↓
G 回测与研究方法
  ↓
D 时间序列
  ↓
E Financial ML
  ↓
J Coding / Systems
  ↓
F / H / C / I 按岗位补齐
```

### 为什么 G 要提前

很多候选人先学模型再学回测，顺序其实相反。若不先理解 PIT、look-ahead、survivorship、multiple testing 和 walk-forward，即使模型推导正确，也可能在错误实验上得到漂亮结果。

## 2. 三阶段学习法

### Phase 1：基础推理

目标：A + B + D 的核心题能白板独立推导。

重点检查：

- conditioning；
- estimator/inference；
- stationarity/time order。

### Phase 2：研究闭环

目标：G + E + F/H 中，能从数据定义一直讲到 OOS 与 deployment。

重点检查：

- available-at timestamp；
- metric / utility；
- transaction cost / fill；
- drift / parity。

### Phase 3：工程与专项

目标：J + 目标团队专项模块。

- HFT：F + J；
- Derivatives：C + I + H；
- Portfolio research：D + G + H；
- ML research：B + D + E + G + J。

## 3. 14 天冲刺计划

| 时间 | 内容 | 完成标准 |
|---|---|---|
| Day 1 | A 001-005 | 全部能 30 秒回答，Q005 独立递推 |
| Day 2 | A 006-010 + B 011-012 | 条件/依赖/MLE 不混淆 |
| Day 3 | B 013-020 | multiple testing、HAC、bootstrap 能解释 Why |
| Day 4 | G 061-065 | 建 PIT/leakage/cost checklist |
| Day 5 | G 066-070 | 能完整审计 Sharpe=3 与 research lineage |
| Day 6 | D 031-035 | stationarity/unit-root/spurious regression |
| Day 7 | D 036-040 | cointegration/GARCH/async sampling |
| Day 8 | E 041-045 | baseline、leakage、feature evaluation |
| Day 9 | E 046-050 | calibration、drift、offline-online debug |
| Day 10 | J 091-096 | heap/sliding/as-of/LOB，计时手写 |
| Day 11 | J 097-100 + F 051-055 | performance + state machine + book basics |
| Day 12 | F 056-060 + H/C/I 目标专项 | execution/latency 或衍生品专项 |
| Day 13 | 两次 Mock | 一次数学/统计，一次开放研究/系统 |
| Day 14 | 复盘 | 只看错题、追问和表达，不再扩题 |

## 4. 每天的训练单元

对每道重点题做四次输出：

1. **Closed book**：完全不看答案；
2. **Whiteboard**：写关键公式/状态；
3. **30 秒口述**：删掉所有非必要背景；
4. **3 分钟追问**：主动给边界和验证。

## 5. 如何判断该不该继续刷新题

如果你已经看过很多题但仍出现以下情况，不应继续扩题：

- 看到条件概率题仍然先代公式；
- 能背 ADF 但说不清 null；
- 回测结果好时不会先查 leakage；
- HFT 题只谈 signal 不谈 fill/latency；
- coding 题只谈 Big-O 不谈 state invariants。

此时最有效的是**重复输出旧题并接受追问**。

## 6. Mock Interview 评分建议

每题 0–2 分评五项，总分 10：

- Definition
- Correctness
- Why
- Boundary
- Verification / Engineering

8 分以上才算真正掌握；只做出最终数值但不会解释，最多按 4–5 分处理。
