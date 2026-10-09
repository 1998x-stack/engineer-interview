# Computer Network Interview 100 · 2026

> **计算机网络面试 100 题：从协议原理到 Linux 网络栈与线上故障定位**

这是一个题解式、可持续维护的计算机网络面试仓库。仓库以《计算机网络面试100题_专业详解版_2026.pdf》为内容基线，将 PDF 中 **100 道题完整拆分为 100 个 Markdown**，并进一步加入 RFC / Linux 权威参考、工程边界、可观测性、实验验收标准、交叉链接和学习路线。

## V2.0 Deep Edition · 2026-09-02

本仓库已完成第二轮逐题深度增强。与初版相比，V2 不以“增加字数”为目标，而以**消除模板化、补齐协议不变量、增加工程反例和可验证证据链**为目标：

- **100/100 个题目 Markdown** 新增题目专属 `V2 深入`：第一性原理、协议/内核级展开、工程边界与线上案例。
- 对旧版追问回答进行质量清理：移除通用兜底式答案和跨题串入内容，保持 **300 个追问均有可直接口述的参考回答**。
- **10 个章节 README** 新增本章心智模型、白板题与最小实验组合，便于从“单题”升级到“章节能力”。
- TLS 章节更新到 **RFC 9846** 作为当前 TLS 1.3 主规范；RFC 8446 保留为历史对照。
- CUBIC 使用 RFC 9438；BBR 状态明确标记为 2026 年仍处于 IETF CCWG Active Internet-Draft。
- 每题保留 PDF 原内容与工程扩展边界，避免把后续研究补充伪装成原 PDF 内容。

当前题目文件平均约 **4.2k 字符**，并继续保留实验、可观测性、追问、Rubric 与权威资料。

## 仓库目标

不是背 100 个结论，而是形成一条可复用的推理链：

```text
应用协议 → 传输协议 → IP / 路由 → Linux 内核 → 抓包证据 → 业务故障
```

每题都按同一训练模板组织：

1. **30 秒标准回答**：面试第一轮必须能收住。
2. **Know-How + Know-Why**：状态、字段、时序、算法与设计动机。
3. **二次深化**：把 PDF 结论扩展到 Linux/云网络/中间盒等工程边界。
4. **追问树**：训练面试官连续追问，而不是单题背诵。
5. **可观测性**：用 `ss` / `tcpdump` / `dig` / `curl` / `perf` 等建立证据链。
6. **实验验收标准**：明确“看到了什么才算验证成功”。
7. **评分 Rubric**：从 1/5 八股到 5/5 故障推理能力。

## 全书目录

| 章 | 模块 | 题号 | 核心能力 |
|---:|---|---:|---|
| 01 | [第一章 网络分层、链路与二层基础](questions/01-link-layer-foundations/README.md) | 1-10 | 建立“逐层封装与当前一跳”的基本心智模型。 |
| 02 | [第二章 IP、NAT 与路由](questions/02-ip-nat-routing/README.md) | 11-20 | 从本机路由选择扩展到自治系统与全局流量调度。 |
| 03 | [第三章 TCP 连接、状态机与可靠性](questions/03-tcp-connection-reliability/README.md) | 21-35 | 面试最高频核心：握手、挥手、TIME_WAIT、序号、重传与 framing。 |
| 04 | [第四章 TCP 性能、窗口与拥塞控制](questions/04-tcp-performance-congestion/README.md) | 36-45 | 理解吞吐为什么受到 RTT、窗口、拥塞算法和系统队列共同约束。 |
| 05 | [第五章 UDP、QUIC 与 HTTP/3 传输基础](questions/05-udp-quic-http3/README.md) | 46-52 | 从“无连接数据报”到现代用户态可靠传输协议。 |
| 06 | [第六章 DNS、全局调度与 CDN](questions/06-dns-cdn/README.md) | 53-60 | 掌握域名解析、缓存、一致性与边缘加速。 |
| 07 | [第七章 HTTP/1.1、HTTP/2 与应用层协议](questions/07-http/README.md) | 61-73 | 从 HTTP 语义深入到 framing、缓存、多路复用与 RPC。 |
| 08 | [第八章 HTTPS、TLS 1.3 与 PKI](questions/08-tls-https-pki/README.md) | 74-80 | 掌握握手、证书、密钥协商与 0-RTT 风险。 |
| 09 | [第九章 Socket、epoll 与 Linux 网络栈](questions/09-linux-socket-io/README.md) | 81-90 | 把协议知识落到系统调用、事件循环与内核收包路径。 |
| 10 | [第十章 综合故障定位与系统设计](questions/10-troubleshooting-system-design/README.md) | 91-100 | 用分层方法处理真实线上问题与高并发架构题。 |

## PDF 原书

- [`book/计算机网络面试100题_专业详解版_2026.pdf`](book/计算机网络面试100题_专业详解版_2026.pdf)
- [`docs/pdf-content-map.md`](docs/pdf-content-map.md)：PDF → Repository 的逐项映射与完整性说明。

## 推荐学习路线

- **7 天冲刺**：[`docs/7-day-plan.md`](docs/7-day-plan.md)
- **30 天系统训练**：[`docs/30-day-plan.md`](docs/30-day-plan.md)
- **Top 20 必会题**：[`docs/top20.md`](docs/top20.md)
- **故障定位框架**：[`docs/troubleshooting-framework.md`](docs/troubleshooting-framework.md)
- **Linux 网络命令速查**：[`docs/linux-network-cheatsheet.md`](docs/linux-network-cheatsheet.md)
- **RFC 阅读方法**：[`docs/rfc-reading-guide.md`](docs/rfc-reading-guide.md)
- **术语表**：[`docs/glossary.md`](docs/glossary.md)

## 面试训练方法

一次完整训练建议：

```text
只看题目
  ↓
30 秒口述答案
  ↓
画时序 / 状态机 / 数据路径
  ↓
回答追问
  ↓
做最小实验或读抓包
  ↓
按 1-5 分 Rubric 自评
```

如果回答中出现“肯定、一定、永远”这类词，主动检查是否把**规范语义**和**具体实现**混在了一起。

## 权威参考策略

协议题优先使用 IETF/RFC；Linux 行为优先使用 Linux Kernel Documentation 与 Linux man-pages。HTTP 的共同语义以 RFC 9110 为准；TCP 基础规范以 RFC 9293 为准；Linux 多核收包扩展重点参考 RSS/RPS/RFS/XPS 文档。`references/README.md` 提供完整索引。

> 2026 状态提示：BBR 当前仍是 IETF CCWG Active Internet-Draft（`draft-ietf-ccwg-bbr-06`，2026-07-06），不是已经发布的正式 RFC。

## Repository Structure

```text
computer-network-interview-100/
├── README.md
├── book/                         # 原始 PDF
├── questions/
│   ├── 01-link-layer-foundations/
│   ├── 02-ip-nat-routing/
│   ├── ...
│   └── 10-troubleshooting-system-design/
├── docs/                         # 学习路线、附录、术语、排障方法
├── references/                   # RFC / Linux 官方参考索引
├── scripts/                      # 仓库一致性检查
└── .github/                      # CI / Issue / PR 模板
```

## 本地检查

```bash
python scripts/check_repo.py
python scripts/check_links.py
```

检查项包括：

- 100 个题目 Markdown 是否齐全；
- ID 是否为 1-100 且无重复；
- 每题是否包含标准章节；
- 原始 PDF 是否存在；
- 章节索引与题目数是否一致。

## 内容来源与扩展边界

- 标记为 **“PDF 原内容”** 的部分忠实来自本仓库对应 PDF。
- **“二次深化 / 权威资料 / 可观测性 / 实验验收标准”** 是在原内容基础上的工程化扩展。
- 对随时间变化的内容（例如 BBR IETF 状态、Linux 默认参数），仓库尽量给出权威链接并避免把某一版本默认值写成永久事实。

## 发布前 License 提示

本仓库没有替你选择公开发布许可证。若要上传到公开 GitHub，请根据你的使用目的为“文本内容”和“脚本代码”选择合适许可证，并确认引用资料的使用方式。
