# M05 · 数值正确性与反向传播实验室

这是 **GitHub 模块新增的可执行教学实验**，不属于原始面试 PDF，也不等价于大规模分布式训练验证。

## 从公式到可执行不变量

| 关联题目 | 教学参考实现 | 对照与风险边界 |
|---|---|---|
| [Q003 CE 梯度](../questions/01-foundations/Q003-softmax-cross-entropy-gradient.md) | `cross_entropy_logits` | 直接 logits 的 logsumexp，前向与 `F.cross_entropy` 对拍；backward 与 `p-y` 对拍 |
| [Q012 AdamW](../questions/02-optimization-normalization/Q012-adam-vs-adamw.md) | `adamw_step` | 多步 AdamW 参数变化与 PyTorch 对拍；对比 Adam 的 L2 进入一二阶矩的差异 |
| [Q016 BatchNorm](../questions/02-optimization-normalization/Q016-batchnorm.md) | `batchnorm2d_train/eval` | Train 的 **biased** 方差计算、Eval 的 running stats；前向及梯度对拍 |
| [Q055 MHA](../questions/05-transformer/Q055-implement-mha.md) | `reference_attention` | `[B,H,T,D]`、padding/causal、SDPA 梯度对拍；全屏蔽行**拒绝**而不是均匀分布 |
| [Q069 InfoNCE](../questions/07-multimodal-diffusion/Q069-infonce.md) | `symmetric_infonce` | 双向/单向 NCE、温度与归一化、CLIP 风格 reference 梯度对拍 |
| [Q100 综合](../questions/10-project-system-design/Q100-implement-from-scratch.md) | 上述全体 | shape、finite、oracle、gradient、无效输入拒绝；CI 可重复 |

## 本地运行

在 `deep-learning-interview-100/` 下：

```bash
python -m pip install pytest
# PyTorch 请按本机 CPU/CUDA 环境安装；CI 固定 torch==2.5.1+cpu
python scripts/check_repo.py
python scripts/check_contracts.py
python scripts/build_index.py --check
python -m pytest -q tests
```

机器可读题库索引有两份：`metadata/questions.json` 与 `metadata/questions.jsonl`。
`check_contracts.py` 额外检查 100 道题的元数据、Markdown frontmatter、
章节目录和 PDF 页码标记是否相互一致。
**这些检查不能证明 PDF 页码本身有真实源文件依据，更不能证明全部题目事实正确。**

## 实验边界

- CE 假设互斥多分类、`[B,C]` logits 与有效 int64 target；不提供 ignore_index、sample weights、label smoothing。
- BN 用 `[B,C,H,W]`；`batchnorm2d_train` 不更新 running stats，而 PyTorch running variance 使用的无偏估计与前向归一化采用的有偏估计不同。
- AdamW 是单张量 functional 参考，不涵盖 fused foreach、AMP、参数分组和 optimizer state serialization。
- Attention mask 约定 **True=可见 key**；causal suffix 查询属于 key 的最后 Tq 个时间步；每个 query 至少要有一个可见 key。
- InfoNCE 假定 batch 内对角线为正样本，其他样本作为候选 negatives；false negatives、分布式 all-gather、多正样本并未解决。
- 对于 fp16/bfloat16，参考实现会在关键归一化/Softmax 运算中临时提升至 float32；数值验收以 CPU float64 为主，不能代替 GPU kernel 验收。

后续可以扩展 CPU/GPU dtype sweep、有限差分梯度检查、低精度溢出实验、不同 batch 的消融、分布式训练/推理实测与资源账本，但需要相应 GPU 环境或目标设备。
