# 公式速查

## 1. E2E 延迟

$$T_{E2E} pprox TTFT + (N_{out}-1)\cdot TPOT$$

## 2. Roofline

$$Performance \le \min(Peak\ FLOPS,\ Arithmetic\ Intensity 	imes Memory\ Bandwidth)$$

## 3. KV Cache

$$M_{KV}=B\cdot T\cdot L\cdot 2\cdot H_{kv}\cdot D_{head}\cdot bytes$$

## 4. Decode 带宽上界

$$tokens/s \lesssim rac{effective\ HBM\ bandwidth}{bytes\ read\ per\ token}$$

## 5. 通信

$$T_{comm}pprox lpha + rac{bytes}{effective\ bandwidth}$$

## 6. Spec Decode

实际收益由 **accepted tokens / (draft cost + verify cost)** 主导，而不是 draft 长度本身。

## 7. Goodput

$$Goodput=rac{requests\ meeting\ SLO}{second}$$

## 8. 成本

$$\$/M\ output\ tokens=rac{cluster\ \$/h}{output\ tokens/h}	imes 10^6$$

> 所有公式都是一阶模型；请用实际 effective bandwidth、kernel efficiency、queueing 与 overlap 校正。
