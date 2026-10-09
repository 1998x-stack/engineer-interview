# 时间序列面试速查表

## 最小 baseline 栈

1. Last value / Naive
2. Seasonal Naive
3. ETS / ARIMA
4. Linear / LightGBM global model
5. Deep / Foundation model（只有在统一 backtest 上证明增量才升级）

## 数据正确性五问

- 预测 cut-off 是什么？
- 每个 feature 的 event time、publish time、available time 是什么？
- rolling feature 是否 `shift` 后再滚动？
- preprocessing 是否只在训练窗 fit？
- backfill / revision 是否导致历史数据“看到了未来版本”？

## 常用公式

**AR(1)**

$$y_t=c+\phi y_{t-1}+\epsilon_t,\qquad |\phi|<1$$

$$E[y_t]=\frac{c}{1-\phi},\qquad Var(y_t)=\frac{\sigma_\epsilon^2}{1-\phi^2}$$

**差分**

$$\nabla y_t=y_t-y_{t-1},\qquad \nabla_m y_t=y_t-y_{t-m}$$

**MAE / RMSE**

$$MAE=\frac{1}{n}\sum |y-\hat y|$$

$$RMSE=\sqrt{\frac{1}{n}\sum(y-\hat y)^2}$$

**Pinball loss**

$$L_\tau(y,\hat q)=\max(\tau(y-\hat q),(\tau-1)(y-\hat q))$$

**层级一致性**

$$y_t=S b_t$$

## 高级答题检查

- 是否给出假设？
- 是否给出失效条件？
- 是否有强 baseline？
- 是否按 horizon / segment 看误差？
- 是否讨论概率校准？
- 是否把模型输出转成业务 decision？
