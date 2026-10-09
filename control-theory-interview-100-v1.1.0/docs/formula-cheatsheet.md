# 核心公式速查

本页完整覆盖 PDF 附录 A 的核心公式，并增加使用条件提示。

| 主题 | 公式/结论 | 使用提醒 |
|---|---|---|
| 闭环 | $T=L/(1+L)$，$S=1/(1+L)$，$S+T=1$ | 先明确信号注入点，noise/disturbance 路径并不相同 |
| 标准二阶 | $p=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}$ | 近邻零点/高阶模态会破坏标准二阶近似 |
| 超调 | $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ | 仅标准欠阻尼二阶 |
| Settling time | $t_s(2\%)\approx4/(\zeta\omega_n)$ | 来自指数包络近似 |
| 状态转移 | $x(t)=e^{At}x_0+\int_0^t e^{A(t-\tau)}Bu(\tau)d\tau$ | 连续 LTI |
| 可控性 | $\mathrm{rank}[B\ AB\ \cdots\ A^{n-1}B]=n$ | 数值上可结合 PBH / Gramian 判断 |
| 可观性 | $\mathrm{rank}[C^T\ (CA)^T\ \cdots]^T=n$ | 与可控性对偶 |
| LQR | $A^TP+PA-PBR^{-1}B^TP+Q=0$，$K=R^{-1}B^TP$ | 注意 state scaling 与 actuator limit |
| Kalman | $K=P^-C^T(CP^-C^T+R)^{-1}$ | Q/R 是 covariance 模型，不是随意平滑旋钮 |
| ZOH | $A_d=e^{AT_s}$，$B_d=\int_0^{T_s}e^{A\tau}B d\tau$ | 描述真实 sample-and-hold |
| 离散稳定 | $|z_i|<1$ | 连续左半平面通过 $z=e^{sT_s}$ 映射到单位圆内 |
