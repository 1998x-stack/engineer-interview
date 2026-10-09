# 高频追问链

本页保留 PDF 附录 C 的四条追问链，并补充“答题终点”。

## A. PID

PID 三项 → 积分为何消除稳态误差 → windup → clamping/back-calculation → D 为什么放大噪声 → derivative kick → 离散实现 → sample time 改变为什么需重新验证。

**答题终点：** 能从理想公式一路谈到真实 actuator/sensor/timing。

## B. 稳定性

极点为何决定稳定 → RHP zero → BIBO vs internal stability → 不稳定 pole-zero cancellation → Root Locus → PM/GM → Nyquist → delay margin。

**答题终点：** 能把极点、代数判据、几何轨迹、频率裕度统一起来。

## C. 现代控制

状态是什么 → controllability → stabilizable → observability → observer → separation principle → LQR → Kalman → LQG 为什么不等于 robust。

**答题终点：** 能说明每个结构条件对应“能否控制/能否估计”的物理意义。

## D. 工程落地

仿真稳定实机振荡 → timing → actuator saturation → sensor noise/bias → unmodeled flexible mode → FRF → HIL → regression test。

**答题终点：** 从猜测转向数据证据链和可复现实验。
