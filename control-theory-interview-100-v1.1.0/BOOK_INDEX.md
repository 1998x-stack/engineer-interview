# 控制论原理面试 100 题 — 总索引

> 每题一个 Markdown；PDF 原始内容完整保留，并在其后明确分隔“仓库增强”。

## 1. 控制论基础与建模

从反馈、极点/零点、建模和不确定性建立完整的控制直觉。

- [Q001. 反馈到底改变了什么？为什么负反馈是控制论的核心？](questions/01-foundations-modeling/q001.md) · `基础` · ★★★★★ · PDF p.1
- [Q002. 开环与闭环控制的根本差别是什么？](questions/01-foundations-modeling/q002.md) · `基础` · ★★★★★ · PDF p.2
- [Q003. 为什么“快、准、稳、抗噪”不能同时无限提升？](questions/01-foundations-modeling/q003.md) · `进阶` · ★★★★★ · PDF p.3
- [Q004. 传递函数是什么？它隐藏了哪些信息？](questions/01-foundations-modeling/q004.md) · `基础` · ★★★★★ · PDF p.4
- [Q005. 极点、零点分别决定什么？为什么右半平面零点很麻烦？](questions/01-foundations-modeling/q005.md) · `基础` · ★★★★★ · PDF p.5
- [Q006. 如何从物理定律建立控制模型？](questions/01-foundations-modeling/q006.md) · `基础` · ★★★★★ · PDF p.5
- [Q007. 什么是线性、时不变、因果？为什么 LTI 如此重要？](questions/01-foundations-modeling/q007.md) · `基础` · ★★★★☆ · PDF p.6
- [Q008. 什么是平衡点？为什么控制器常围绕平衡点设计？](questions/01-foundations-modeling/q008.md) · `基础` · ★★★★☆ · PDF p.7
- [Q009. 什么是系统阶次？阶次与状态数量、极点数量是什么关系？](questions/01-foundations-modeling/q009.md) · `基础` · ★★★★☆ · PDF p.8
- [Q010. 模型为什么永远不完全准确？控制设计如何面对模型误差？](questions/01-foundations-modeling/q010.md) · `基础` · ★★★★★ · PDF p.9

## 2. 时域响应与二阶系统

把极点位置、阻尼、时间常数、稳态误差与实验响应联系起来。

- [Q011. 一阶系统的时间常数到底表示什么？](questions/02-time-domain-second-order/q011.md) · `基础` · ★★★★★ · PDF p.10
- [Q012. 标准二阶系统中的自然频率和阻尼比分别控制什么？](questions/02-time-domain-second-order/q012.md) · `基础` · ★★★★★ · PDF p.11
- [Q013. 二阶系统超调量如何从阻尼比得到？](questions/02-time-domain-second-order/q013.md) · `基础` · ★★★★★ · PDF p.12
- [Q014. 为什么 settling time 常近似为 4/(zeta wn)？](questions/02-time-domain-second-order/q014.md) · `基础` · ★★★★★ · PDF p.13
- [Q015. Rise time、peak time、settling time、overshoot 各自反映什么？](questions/02-time-domain-second-order/q015.md) · `基础` · ★★★★☆ · PDF p.13
- [Q016. 什么是系统型别？它为什么决定标准输入的稳态误差？](questions/02-time-domain-second-order/q016.md) · `基础` · ★★★★★ · PDF p.14
- [Q017. 终值定理怎样求稳态误差？什么时候不能用？](questions/02-time-domain-second-order/q017.md) · `基础` · ★★★★★ · PDF p.15
- [Q018. 什么是主导极点？高阶系统何时可近似为二阶？](questions/02-time-domain-second-order/q018.md) · `进阶` · ★★★★★ · PDF p.16
- [Q019. 左半平面零点如何改变阶跃响应？](questions/02-time-domain-second-order/q019.md) · `进阶` · ★★★★☆ · PDF p.16
- [Q020. 如何从实验阶跃数据快速判断对象类型？](questions/02-time-domain-second-order/q020.md) · `工程` · ★★★★★ · PDF p.17

## 3. PID 与工程实现

不仅会调 PID，更要理解 anti-windup、D 滤波、串级和前馈。

- [Q021. PID 三项的本质作用分别是什么？](questions/03-pid-engineering/q021.md) · `基础` · ★★★★★ · PDF p.19
- [Q022. 为什么积分能消除阶跃稳态误差？](questions/03-pid-engineering/q022.md) · `基础` · ★★★★★ · PDF p.20
- [Q023. 为什么理想微分 Kd*s 几乎不直接实现？](questions/03-pid-engineering/q023.md) · `基础` · ★★★★★ · PDF p.21
- [Q024. 什么是 derivative kick？如何避免？](questions/03-pid-engineering/q024.md) · `工程` · ★★★★★ · PDF p.21
- [Q025. Integral Windup 是什么？为什么饱和时尤其严重？](questions/03-pid-engineering/q025.md) · `工程` · ★★★★★ · PDF p.22
- [Q026. Clamping 与 back-calculation anti-windup 有什么区别？](questions/03-pid-engineering/q026.md) · `工程` · ★★★★★ · PDF p.23
- [Q027. PI 和 PID 怎么选？为什么电机电流环常见 PI？](questions/03-pid-engineering/q027.md) · `工程` · ★★★★★ · PDF p.24
- [Q028. 串级控制为什么有效？内外环带宽如何分配？](questions/03-pid-engineering/q028.md) · `工程` · ★★★★★ · PDF p.24
- [Q029. Feedforward 与 feedback 怎样组合？](questions/03-pid-engineering/q029.md) · `工程` · ★★★★★ · PDF p.25
- [Q030. Ziegler-Nichols 为什么经典但不应迷信？](questions/03-pid-engineering/q030.md) · `工程` · ★★★★☆ · PDF p.26

## 4. 稳定性与根轨迹

从内部稳定到 Routh、根轨迹、lead/lag，掌握经典稳定设计。

- [Q031. BIBO 稳定、渐近稳定、内部稳定有什么区别？](questions/04-stability-root-locus/q031.md) · `进阶` · ★★★★★ · PDF p.27
- [Q032. 为什么连续时间极点在左半平面才稳定？](questions/04-stability-root-locus/q032.md) · `基础` · ★★★★★ · PDF p.28
- [Q033. Routh-Hurwitz 判据为什么有用？](questions/04-stability-root-locus/q033.md) · `基础` · ★★★★★ · PDF p.29
- [Q034. 根轨迹是什么？它回答了什么设计问题？](questions/04-stability-root-locus/q034.md) · `基础` · ★★★★★ · PDF p.30
- [Q035. 根轨迹从哪里出发、在哪里结束？渐近线怎么求？](questions/04-stability-root-locus/q035.md) · `基础` · ★★★★★ · PDF p.30
- [Q036. Lead compensator 为什么能提高相位裕度和响应速度？](questions/04-stability-root-locus/q036.md) · `进阶` · ★★★★★ · PDF p.31
- [Q037. Lag compensator 为什么能改善稳态误差？](questions/04-stability-root-locus/q037.md) · `进阶` · ★★★★☆ · PDF p.32
- [Q038. 为什么不稳定 pole-zero cancellation 是危险设计？](questions/04-stability-root-locus/q038.md) · `进阶` · ★★★★★ · PDF p.33
- [Q039. 什么叫 minimum phase？为什么它代表“可逆性最好”的系统？](questions/04-stability-root-locus/q039.md) · `进阶` · ★★★★☆ · PDF p.33
- [Q040. 怎么从根轨迹选闭环极点而不是“凭感觉点一个 K”？](questions/04-stability-root-locus/q040.md) · `工程` · ★★★★★ · PDF p.34

## 5. 频率响应与鲁棒直觉

用 Bode/Nyquist/S/T 统一理解速度、抗扰、噪声与鲁棒性。

- [Q041. 为什么控制工程特别重视频率响应？](questions/05-frequency-robustness/q041.md) · `基础` · ★★★★★ · PDF p.36
- [Q042. Bode 图上的 pole/zero 规则怎样快速手画？](questions/05-frequency-robustness/q042.md) · `基础` · ★★★★★ · PDF p.37
- [Q043. Gain crossover、phase crossover、PM、GM 分别是什么？](questions/05-frequency-robustness/q043.md) · `基础` · ★★★★★ · PDF p.38
- [Q044. 为什么时间延迟特别危险？如何估计 delay margin？](questions/05-frequency-robustness/q044.md) · `进阶` · ★★★★★ · PDF p.39
- [Q045. Nyquist 判据到底在数什么？](questions/05-frequency-robustness/q045.md) · `进阶` · ★★★★★ · PDF p.39
- [Q046. 为什么 Bode margin 是 Nyquist 的局部简化？](questions/05-frequency-robustness/q046.md) · `进阶` · ★★★★☆ · PDF p.40
- [Q047. Sensitivity S 和 complementary sensitivity T 各自控制什么？](questions/05-frequency-robustness/q047.md) · `进阶` · ★★★★★ · PDF p.41
- [Q048. 什么是 waterbed effect？为什么 S 不可能处处很小？](questions/05-frequency-robustness/q048.md) · `高级` · ★★★★☆ · PDF p.42
- [Q049. 闭环带宽与响应速度有什么关系？为什么带宽不能无限高？](questions/05-frequency-robustness/q049.md) · `工程` · ★★★★★ · PDF p.42
- [Q050. 如何做一次真正的 loop-shaping 设计？](questions/05-frequency-robustness/q050.md) · `工程` · ★★★★★ · PDF p.43

## 6. 状态空间与现代线性控制

掌握状态、矩阵指数、线性化、MIMO、状态反馈与跟踪。

- [Q051. 状态到底是什么？如何判断一组变量能否作为状态？](questions/06-state-space-linear-control/q051.md) · `基础` · ★★★★★ · PDF p.45
- [Q052. 状态空间中的 A、B、C、D 分别代表什么物理意义？](questions/06-state-space-linear-control/q052.md) · `基础` · ★★★★★ · PDF p.46
- [Q053. 矩阵指数 e^{At} 为什么是状态空间的核心？](questions/06-state-space-linear-control/q053.md) · `进阶` · ★★★★☆ · PDF p.47
- [Q054. 为什么 A 的特征值就是系统模态？](questions/06-state-space-linear-control/q054.md) · `基础` · ★★★★★ · PDF p.47
- [Q055. 状态坐标变换为什么不改变系统本质？](questions/06-state-space-linear-control/q055.md) · `进阶` · ★★★★☆ · PDF p.48
- [Q056. 如何从状态空间得到传递函数？反过来怎么做？](questions/06-state-space-linear-control/q056.md) · `基础` · ★★★★★ · PDF p.49
- [Q057. 为什么状态空间特别适合 MIMO 控制？](questions/06-state-space-linear-control/q057.md) · `基础` · ★★★★★ · PDF p.50
- [Q058. 非线性系统如何线性化？Jacobian 的物理意义是什么？](questions/06-state-space-linear-control/q058.md) · `基础` · ★★★★★ · PDF p.50
- [Q059. 什么是状态反馈？Pole placement 如何工作？](questions/06-state-space-linear-control/q059.md) · `基础` · ★★★★★ · PDF p.51
- [Q060. 状态反馈如何实现零稳态跟踪？](questions/06-state-space-linear-control/q060.md) · `进阶` · ★★★★★ · PDF p.52

## 7. 可控可观、观测器与 Kalman

从结构性质走向状态估计和传感器融合。

- [Q061. 可控性是什么意思？Kalman rank test 在看什么？](questions/07-controllability-observability-kalman/q061.md) · `基础` · ★★★★★ · PDF p.54
- [Q062. 不可控系统一定不能稳定吗？Stabilizable 是什么？](questions/07-controllability-observability-kalman/q062.md) · `进阶` · ★★★★★ · PDF p.55
- [Q063. 可观性是什么意思？为什么“传感器少”不等于不可观？](questions/07-controllability-observability-kalman/q063.md) · `基础` · ★★★★★ · PDF p.55
- [Q064. Detectability 是什么？为什么观测器不一定要求完全可观？](questions/07-controllability-observability-kalman/q064.md) · `进阶` · ★★★★☆ · PDF p.56
- [Q065. Luenberger Observer 如何推导？](questions/07-controllability-observability-kalman/q065.md) · `基础` · ★★★★★ · PDF p.57
- [Q066. Observer poles 为什么不能无限快？](questions/07-controllability-observability-kalman/q066.md) · `工程` · ★★★★★ · PDF p.58
- [Q067. Separation Principle 为什么重要？](questions/07-controllability-observability-kalman/q067.md) · `进阶` · ★★★★★ · PDF p.59
- [Q068. Kalman Filter 和 Luenberger Observer 的本质关系？](questions/07-controllability-observability-kalman/q068.md) · `进阶` · ★★★★★ · PDF p.59
- [Q069. Kalman Filter 的 predict/update 两步各在做什么？](questions/07-controllability-observability-kalman/q069.md) · `基础` · ★★★★★ · PDF p.60
- [Q070. Kalman 中 Q、R 怎么调？为什么不能把它们当普通“滤波强度旋钮”？](questions/07-controllability-observability-kalman/q070.md) · `工程` · ★★★★★ · PDF p.61

## 8. 最优、MPC、鲁棒与自适应

理解 LQR/LQG/MPC/H∞ 等算法解决的不同问题。

- [Q071. 为什么 Pole Placement 之后还需要 LQR？](questions/08-optimal-mpc-robust-adaptive/q071.md) · `进阶` · ★★★★★ · PDF p.62
- [Q072. LQR 中 Q、R 如何选？](questions/08-optimal-mpc-robust-adaptive/q072.md) · `工程` · ★★★★★ · PDF p.63
- [Q073. CARE / Riccati 方程在 LQR 中为什么出现？](questions/08-optimal-mpc-robust-adaptive/q073.md) · `高级` · ★★★★☆ · PDF p.64
- [Q074. LQG 是什么？为什么“最优”不等于“鲁棒”？](questions/08-optimal-mpc-robust-adaptive/q074.md) · `高级` · ★★★★☆ · PDF p.65
- [Q075. MPC 和 LQR 最大区别是什么？](questions/08-optimal-mpc-robust-adaptive/q075.md) · `进阶` · ★★★★★ · PDF p.65
- [Q076. MPC horizon N 怎么选？越长越好吗？](questions/08-optimal-mpc-robust-adaptive/q076.md) · `工程` · ★★★★☆ · PDF p.66
- [Q077. 什么是鲁棒控制？Nominal stability 与 robust stability 有何区别？](questions/08-optimal-mpc-robust-adaptive/q077.md) · `进阶` · ★★★★★ · PDF p.67
- [Q078. H-infinity 控制的核心目标是什么？](questions/08-optimal-mpc-robust-adaptive/q078.md) · `高级` · ★★★★☆ · PDF p.68
- [Q079. 自适应控制和鲁棒控制有何本质不同？](questions/08-optimal-mpc-robust-adaptive/q079.md) · `进阶` · ★★★★☆ · PDF p.68
- [Q080. 什么是 disturbance observer / ADRC 类思想？](questions/08-optimal-mpc-robust-adaptive/q080.md) · `工程` · ★★★★☆ · PDF p.69

## 9. 离散控制与数字实现

把连续理论真正落到采样、延迟、量化和实时系统。

- [Q081. 连续控制器为什么必须认真做离散实现？](questions/09-discrete-digital-control/q081.md) · `基础` · ★★★★★ · PDF p.72
- [Q082. 连续 s 平面与离散 z 平面稳定区域如何对应？](questions/09-discrete-digital-control/q082.md) · `基础` · ★★★★★ · PDF p.72
- [Q083. 采样频率应该怎么选？Nyquist 2 倍为什么远远不够？](questions/09-discrete-digital-control/q083.md) · `工程` · ★★★★★ · PDF p.73
- [Q084. ZOH 离散化如何得到 Ad、Bd？](questions/09-discrete-digital-control/q084.md) · `进阶` · ★★★★★ · PDF p.74
- [Q085. Tustin / Bilinear Transform 的优缺点是什么？](questions/09-discrete-digital-control/q085.md) · `进阶` · ★★★★☆ · PDF p.74
- [Q086. 一个 sample delay 为什么可能把高带宽控制环弄崩？](questions/09-discrete-digital-control/q086.md) · `工程` · ★★★★★ · PDF p.75
- [Q087. 离散 PID 的积分和微分怎么写才可靠？](questions/09-discrete-digital-control/q087.md) · `工程` · ★★★★★ · PDF p.76
- [Q088. 量化、固定点和数值精度会怎样破坏控制？](questions/09-discrete-digital-control/q088.md) · `工程` · ★★★★☆ · PDF p.77
- [Q089. 多速率控制 multi-rate 为什么常见？](questions/09-discrete-digital-control/q089.md) · `工程` · ★★★★☆ · PDF p.77
- [Q090. 数字控制上线前应该做哪些验证？](questions/09-discrete-digital-control/q090.md) · `工程` · ★★★★★ · PDF p.78

## 10. 非线性与系统级工程面试

用 Lyapunov、非线性控制与系统调试完成能力闭环。

- [Q091. Lyapunov 稳定性为什么能在不求解析解时证明稳定？](questions/10-nonlinear-system-engineering/q091.md) · `进阶` · ★★★★★ · PDF p.80
- [Q092. 线性系统的 Lyapunov 方程如何判断稳定？](questions/10-nonlinear-system-engineering/q092.md) · `进阶` · ★★★★★ · PDF p.81
- [Q093. Feedback Linearization 和普通 Jacobian 线性化有什么区别？](questions/10-nonlinear-system-engineering/q093.md) · `高级` · ★★★★☆ · PDF p.82
- [Q094. Sliding Mode Control 为什么鲁棒？chattering 从哪里来？](questions/10-nonlinear-system-engineering/q094.md) · `高级` · ★★★★☆ · PDF p.83
- [Q095. Backstepping 适合什么类型的非线性系统？](questions/10-nonlinear-system-engineering/q095.md) · `高级` · ★★★☆☆ · PDF p.83
- [Q096. 为什么 actuator saturation / rate limit 是控制面试必须会的非线性？](questions/10-nonlinear-system-engineering/q096.md) · `工程` · ★★★★★ · PDF p.84
- [Q097. 控制系统出现振荡，怎样区分是“增益太高”还是结构问题？](questions/10-nonlinear-system-engineering/q097.md) · `工程` · ★★★★★ · PDF p.85
- [Q098. 仿真稳定但实机振荡，系统化排查顺序是什么？](questions/10-nonlinear-system-engineering/q098.md) · `工程` · ★★★★★ · PDF p.86
- [Q099. 如何回答“设计一个无人机/电机/倒立摆控制器”的开放题？](questions/10-nonlinear-system-engineering/q099.md) · `综合` · ★★★★★ · PDF p.86
- [Q100. 终极调试题：闭环性能突然变差，你如何用数据而不是猜测定位？](questions/10-nonlinear-system-engineering/q100.md) · `综合` · ★★★★★ · PDF p.87
