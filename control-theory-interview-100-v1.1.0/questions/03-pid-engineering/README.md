# 第 3 章：PID 与工程实现

不仅会调 PID，更要理解 anti-windup、D 滤波、串级和前馈。

题号：Q021–Q030

## 本章题目

- [Q021. PID 三项的本质作用分别是什么？](q021.md) — 基础 · ★★★★★
- [Q022. 为什么积分能消除阶跃稳态误差？](q022.md) — 基础 · ★★★★★
- [Q023. 为什么理想微分 Kd*s 几乎不直接实现？](q023.md) — 基础 · ★★★★★
- [Q024. 什么是 derivative kick？如何避免？](q024.md) — 工程 · ★★★★★
- [Q025. Integral Windup 是什么？为什么饱和时尤其严重？](q025.md) — 工程 · ★★★★★
- [Q026. Clamping 与 back-calculation anti-windup 有什么区别？](q026.md) — 工程 · ★★★★★
- [Q027. PI 和 PID 怎么选？为什么电机电流环常见 PI？](q027.md) — 工程 · ★★★★★
- [Q028. 串级控制为什么有效？内外环带宽如何分配？](q028.md) — 工程 · ★★★★★
- [Q029. Feedforward 与 feedback 怎样组合？](q029.md) — 工程 · ★★★★★
- [Q030. Ziegler-Nichols 为什么经典但不应迷信？](q030.md) — 工程 · ★★★★☆

## 章节学习建议

PID 面试真正区分水平的地方是实现细节。理想连续公式只是起点；实机还要处理传感器噪声、D 项滤波、setpoint kick、输出饱和、rate limit、bumpless transfer、manual/auto 切换以及离散采样。

任何 PID 调参结论都应该带条件，例如“增大 $K_p$ 通常加快响应”只在闭环仍有足够稳定裕度、执行器未饱和、未激励未建模动态时成立。

## 专业学习框架

### 知识主线

- P/I/D 的频域作用
- filtered derivative/setpoint weighting
- saturation 与 anti-windup
- 串级、前馈与两自由度
- 整定与上线实现

### 学完本章应达到

- [ ] 能解释为什么 PI 在工业中极常见
- [ ] 能完整画出 saturation/anti-windup 信号路径
- [ ] 能把 PID 参数变化映射到 crossover/PM/noise

### 面试表达原则

面试时主动提 actual actuator、rate limit 和采样实现，比只背 Kp/Ki/Kd 更有区分度。

### 推荐复习顺序

1. 先做本章所有 ★★★★★ 题，只练 30 秒结论。
2. 第二遍只做公式/白板推导，不看标准答案。
3. 第三遍逐题回答“什么时候失效”和“如何用实验验证”。
4. 最后从本章任选两题串成连续追问链，练 5–10 分钟深挖。

## 推荐实验

- 运行 `examples/python/03_*.py` 对应实验。
- 每道题至少完成一次 30 秒口述和一次白板推导。
