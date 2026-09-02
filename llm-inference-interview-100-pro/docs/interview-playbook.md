# 面试答题模板

## Step 1｜先给一句结论

控制在 20-30 秒；不要一开始堆框架名。

## Step 2｜写成本模型

至少给一个公式：KV、Roofline、通信、Goodput、成本。

## Step 3｜指出边界

使用“通常”“在低 batch / 长 context / 跨节点条件下”等限定语，避免绝对化。

## Step 4｜给工程证据

说清会看哪些 profiler/metrics：TTFT/TPOT、HBM、Tensor Core、NCCL、cache hit、queue。

## Step 5｜主动给反例

说明该优化何时无效或负优化，这是高阶回答的显著区分点。

## 评分自检

- 只会定义：基础；
- 会公式和机制：合格；
- 会边界与 trade-off：良好；
- 会 profiler、实验设计、SLO 与系统取舍：优秀。
