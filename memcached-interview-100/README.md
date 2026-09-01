# Memcached Interview 100 · 源码穿透版

一套面向 **后端 / 基础架构 / 缓存系统 / C/C++ 系统岗位** 的 Memcached 面试学习仓库。以 **Memcached 1.6.45（2026-07-09）** 为版本基线，把 PDF 的 100 道题拆为 100 个独立 Markdown，并进一步扩展源码、并发、性能、生产实践和实验。

> 组织方法借鉴经典“题目 → 思路 → 深挖 → 追问 → 易错点”的训练方式；内容独立撰写，不复制《剑指 Offer》或其他第三方书籍正文。

## 你会得到什么

- **100 题 / 100 Markdown**：每题可独立阅读、引用、review。
- **源码穿透**：Item / Assoc / Slab / LRU / Worker / Protocol 主线。
- **现代 Memcached**：Meta Protocol、segmented LRU、Extstore、Warm Restart、Built-in Proxy。
- **生产工程**：击穿、雪崩、Hot Key、origin 保护、监控、容量、NUMA/Swap。
- **系统设计**：百万 QPS、N+1 容量、节点故障、扩缩容与 Hash Ring 变更。
- **可执行实验**：基础协议、一致性哈希、Mini-Memcached、stats 诊断。
- **工程化维护**：MkDocs、GitHub Actions、100 题完整性/链接校验脚本。

## 仓库结构

```text
memcached-interview-100/
├── README.md
├── book/
│   └── Memcached_Interview_100_剑指Offer风格.pdf
├── docs/
│   ├── 01-architecture-design/                 # 001-010
│   ├── 02-item-set-get-source/                 # 011-020
│   ├── 03-slab-memory/                         # 021-030
│   ├── 04-assoc-hashtable/                     # 031-040
│   ├── 05-lru-ttl-eviction/                    # 041-050
│   ├── 06-thread-lock-libevent-protocol/       # 051-060
│   ├── 07-consistent-hashing-distributed/      # 061-070
│   ├── 08-cache-consistency-resilience/        # 071-080
│   ├── 09-observability-capacity-troubleshooting/ # 081-090
│   └── 10-advanced-source-system-design/       # 091-100
├── study-paths/
├── labs/
├── references/
├── assets/diagrams/
├── scripts/
├── .github/workflows/
└── mkdocs.yml
```

## 建议学习顺序

```text
Item
  ↓
SET / GET lifecycle
  ↓
Slab memory
  ↓
Assoc hash
  ↓
LRU / TTL
  ↓
Locks / libevent
  ↓
Consistent hashing
  ↓
Cache resilience
  ↓
Observability
  ↓
Million-QPS design
```

优先入口：

- [30+ 道必刷核心题](study-paths/30-must-do.md)
- [7 天冲刺计划](study-paths/7-day-plan.md)
- [源码阅读路线](study-paths/source-reading-route.md)
- [系统设计路线](study-paths/system-design-route.md)
- [100 题总目录](docs/README.md)
- [官方资料与源码索引](references/official-sources.md)
- [原始 PDF](book/Memcached_Interview_100_剑指Offer风格.pdf)

## 四个核心问题

| 模块 | 它回答的问题 |
|---|---|
| **Item** | 一个 KV 在服务端到底是什么对象？ |
| **Assoc** | 给定 key，怎么找到 `item*`？ |
| **Slab** | Item 的物理内存从哪里来、如何复用？ |
| **LRU / TTL** | Item 何时过期、谁在内存压力下先离开？ |

再用 **refcount / locks** 解决“并发下何时可以安全释放”，用 **client/proxy routing** 把单节点外推成集群。

## 本地校验

```bash
python scripts/validate_repo.py
```

当前规则会检查：恰好 100 个题目文件、ID 001-100 完整、关键章节存在、内部 Markdown 链接不破损。

## 构建文档站

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

## 版本说明

本仓库制作时官方 Downloads 的 latest stable 为 **Memcached 1.6.45（2026-07-09）**。协议方面官方当前推荐 Basic Text / Meta Text，新客户端优先考虑 Meta；Binary Protocol 已 deprecated。源码定位尽量固定到 `1.6.45` tag，避免 `master` 漂移。

## License

本仓库未替你预设开源许可证。公开发布前请根据用途选择合适许可证（文档内容常见选择包括 CC BY 4.0 / CC BY-NC-SA；代码常见选择包括 MIT / Apache-2.0），并自行确认适用性。

## V2 专家级增强

当前每一道题都新增了独立的 **专家级展开（V2）**：第一性原理推导、函数级源码符号、边界条件/反例、生产故障推演、定量指标。仓库不再把统一模板当作“深度”，而要求每题都能用指标或实验验证。

- [Memcached 1.6.45 源码符号地图](references/source-symbol-map.md)
- `python scripts/validate_content_v2.py`：检查 100 题专家栏目、最低内容厚度和旧模板残留。
