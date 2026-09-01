# Minimal runnable examples

这些代码只用于面试理解，不是生产实现。刻意保持依赖少、逻辑短，以便把“公式 → 代码”对应起来。

| 文件 | 对应主题 |
|---|---|
| `itemcf.py` | UserCF / ItemCF |
| `two_tower_infonce.py` | 双塔 + In-batch InfoNCE |
| `fm.py` | FM 二阶项 O(nd) 计算 |
| `metrics.py` | Recall@K / NDCG |
| `ab_bucket.py` | 稳定 A/B hash 分桶 |
| `ips.py` | IPS / clipped IPS |
| `mmr.py` | 多样性重排 / MMR |

运行：

```bash
python -m pip install -r requirements.txt
python examples/two_tower_infonce.py
```
