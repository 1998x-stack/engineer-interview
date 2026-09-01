# Content Audit V2

生成日期：2026-09-01  
版本基线：Memcached 1.6.45

## 结果摘要

- 问题 Markdown：**100/100**
- V2 专家级展开：**100/100**
- Markdown 总文件数：**122**
- 仓库总文件数（打包前）：**140**
- 每题字符数：min **5119** / median **5882** / mean **6007** / max **7914**
- 001-100 编号连续性：**PASS**
- 必需章节检查：**PASS**
- 问题内部链接检查：**PASS**
- 仓库级相对链接检查：**949 links / PASS**
- Python labs `py_compile`：**PASS**
- `consistent_hash.py` smoke test：**PASS**（本次输出 modulo remap≈0.91074，ring remap≈0.08139）
- `mini_memcached.py` smoke test：**PASS**

## V2 每题新增标准

每一道题必须包含：

1. 第一性原理推导；
2. 关键源码符号和 `git grep` 阅读入口；
3. 边界条件与反例；
4. 生产故障推演；
5. 定量分析 / 可验证指标。

这五项用于减少“统一模板很长、实际信息密度很低”的问题。

## CI

`.github/workflows/validate.yml` 当前会执行：

```text
validate_repo.py
→ validate_content_v2.py
→ Python lab smoke tests
→ pip install docs requirements
→ mkdocs build --strict
```

本地沙箱无法访问 PyPI，因此本次未能安装 `mkdocs-material` 执行最终站点构建；这是**环境网络限制**，不是已观察到的文档构建错误。GitHub Actions 环境具备网络时会执行该检查。

## 重点增强样例

- `012`：SET 被拆为 private construction → body read → locked store decision → publication。
- `015`：明确 linked/alive、unlinked/freed 两组不同状态，用 refcount 解释并发安全。
- `021`：不再简化为“malloc 慢”，改为 size class/freelist/fragmentation/allocator variance。
- `041`：从 strict LRU 更新为 modern segmented LRU + deferred recency。
- `055`：加入 item/LRU/slab lock 域和锁序/self-deadlock 风险。
- `066/098`：把节点故障量化为 origin miss amplification。
- `097`：用 RAM/CPU/network/P99 四下界 + failure headroom 推导百万 QPS 节点数。
- `100`：把 Mini-Memcached 拆成可逐阶段验证的 7 层实现路线。

## 资料入口

- `references/official-sources.md`
- `references/source-symbol-map.md`
- `study-paths/source-reading-route.md`
