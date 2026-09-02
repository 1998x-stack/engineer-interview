# 公式速查：图像算法岗核心数学口径

> 目的不是背公式，而是保证现场计算时先声明变量、shape 和口径。

## 1. 卷积输出尺寸

$$
H_{out}=\left\lfloor\frac{H+2P-D(K-1)-1}{S}+1\right\rfloor
$$

参数量（groups=$G$）：

$$
K_hK_w\frac{C_{in}}{G}C_{out}
$$

MAC 约为：

$$
H_{out}W_{out}K_hK_w\frac{C_{in}}{G}C_{out}
$$

## 2. 感受野

$$
j_l=j_{l-1}s_l
$$

$$
r_l=r_{l-1}+(k_l-1)d_lj_{l-1}
$$

初始化：$r_0=1,j_0=1$。

## 3. BatchNorm

$$
\mu_B=\frac1m\sum_i x_i,\quad
\sigma_B^2=\frac1m\sum_i(x_i-\mu_B)^2
$$

$$
y_i=\gamma\frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}+\beta
$$

NCHW 的 BN2d 通常对 N/H/W 统计，每 channel 一组参数。

## 4. IoU / Dice

$$
IoU=\frac{|A\cap B|}{|A\cup B|}
$$

$$
Dice=\frac{2|A\cap B|}{|A|+|B|}
$$

关系（集合二值情形）：

$$
Dice=\frac{2IoU}{1+IoU}
$$

## 5. Focal Loss

$$
FL(p_t)=-\alpha_t(1-p_t)^\gamma\log p_t
$$

$\alpha$ 更偏类别平衡，$\gamma$ 控制 easy sample 衰减。

## 6. Detection AP

$$
Precision=\frac{TP}{TP+FP},\quad Recall=\frac{TP}{TP+FN}
$$

COCO AP 对 IoU 0.50:0.05:0.95 平均；实现还受 ignore/crowd/maxDet 等规则影响。

## 7. ViT token 与 Attention

$$
N=\frac{HW}{P^2}
$$

score matrix 为 $N\times N$；attention 关键二次项约 $O(N^2D)$，另有 QKV/MLP 的 $O(ND^2)$ 项。

## 8. CLIP 相似度

$$
s_{ij}=\frac{f_I(I_i)^Tf_T(T_j)}{\tau}
$$

通常 embedding 先 L2 normalize。

## 9. Diffusion closed form

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,
\quad\epsilon\sim\mathcal N(0,I)
$$

CFG：

$$
\epsilon=\epsilon_{uncond}+w(\epsilon_{cond}-\epsilon_{uncond})
$$

## 10. 相机投影

$$
P_c=RP_w+t
$$

$$
\tilde p=KP_c
$$

注意 world-to-camera / camera-to-world 约定必须先声明。

## 11. Stereo depth

理想 pinhole stereo：

$$
Z=\frac{fB}{d}
$$

其中 $f$ 焦距、$B$ baseline、$d$ disparity。

## 12. 统计显著性

样本均值标准误近似：

$$
SE=\frac{s}{\sqrt n}
$$

视觉评测中更常用 bootstrap 对 AP/accuracy 等非简单均值指标给置信区间。
