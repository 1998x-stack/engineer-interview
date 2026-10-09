# 爬虫与反爬虫面试 100 题 · GitHub 增强版

> 从 HTTP 语义到十亿级 URL Frontier，从 Scrapy / Browser Pool 到数据质量、Bot Detection、Rate Limiting 与系统设计。

本仓库由 **90 页《爬虫与反爬虫面试100题_专业详解》PDF** 重构而来。每道题一个 Markdown，并在 PDF 基础上进一步增加：

- 原理推导与关键心智模型；
- 工程化 Checklist 与可观测指标；
- 伪代码 / 容量公式 / 状态机；
- 生产 Gotchas、FMEA 失败模式与缓解策略；
- 原始追问的**逐题参考回答**，不再只有泛化提示；
- 核心边界、机制链路、Trade-off 矩阵、验证策略；
- 初级 / 中级 / 高级面试评分标准；
- 权威官方资料链接；
- 上一题 / 下一题导航。

## 仓库结构

```text
crawler-anti-crawler-interview-100/
├── README.md
├── mkdocs.yml
├── assets/
│   ├── pdf/                         # 原 PDF
│   └── source/                      # 生成 PDF 的 DOCX 内容基线
├── docs/
│   ├── 00-overview/                 # 知识地图、路线、评分框架
│   ├── 01-http-url-robots-cache/    # Q001-Q010
│   ├── ...
│   ├── 10-system-design/            # Q091-Q100
│   └── appendix/                    # 公式、参考资料、排障清单
├── data/
│   ├── question-index.json
│   └── source-extracted.json
├── scripts/                         # 结构与内容校验
└── .github/workflows/               # Markdown / repo CI
```

## 10 大章节

| # | 章节 | 题号 | 导航 |
|---:|---|---|---|
| 1 | 第一章 HTTP、URL、Robots 与缓存 | Q001-Q010 | [HTTP / URL / Robots / Cache](docs/01-http-url-robots-cache/index.md) |
| 2 | 第二章 HTML、DOM 与数据抽取 | Q011-Q020 | [HTML / DOM / Extraction](docs/02-html-dom-extraction/index.md) |
| 3 | 第三章 Scrapy、异步与并发 | Q021-Q030 | [Scrapy / Async](docs/03-scrapy-async-concurrency/index.md) |
| 4 | 第四章 JavaScript、SPA 与浏览器自动化 | Q031-Q040 | [SPA / Browser Automation](docs/04-js-spa-browser-automation/index.md) |
| 5 | 第五章 分布式爬虫 | Q041-Q050 | [Distributed Crawling](docs/05-distributed-crawling/index.md) |
| 6 | 第六章 去重、调度、存储与数据质量 | Q051-Q060 | [Dedup / Storage / Quality](docs/06-dedup-scheduling-storage-quality/index.md) |
| 7 | 第七章 反爬检测原理 | Q061-Q070 | [Bot Detection](docs/07-bot-detection-principles/index.md) |
| 8 | 第八章 服务端防爬体系 | Q071-Q080 | [Server-side Mitigation](docs/08-server-side-bot-mitigation/index.md) |
| 9 | 第九章 稳定性、可观测性与数据质量 | Q081-Q090 | [Reliability / Observability](docs/09-reliability-observability-quality/index.md) |
| 10 | 第十章 高级系统设计 | Q091-Q100 | [System Design](docs/10-system-design/index.md) |

## 推荐学习路径

- 新手：Q001-Q040 → Q051-Q060 → Q081-Q090。
- 爬虫后端：Q001-Q060 + Q081-Q100。
- 数据平台 / 搜索：重点 Q041-Q060、Q091-Q100。
- 防守 / Bot Management：Q061-Q080 + Q098。

详细安排见 [7 天冲刺路线](docs/00-overview/seven-day-roadmap.md)。

## 文档站

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

## PDF 完整内容镜像

- [PDF / DOCX 完整文本基线](docs/PDF-BASELINE.md)
- [原 PDF 附录文本镜像](docs/appendix/pdf-original-appendices.md)

## 内容基线与增强原则

1. PDF 中 100 道题的题意、考察点、推荐回答、深度解析、易错点、追问和“一句话记忆”全部进入对应 Markdown。
2. GitHub 增强内容不会把 `robots.txt`、验证码或登录状态描述成“绕过技巧”；涉及反爬内容时以服务端检测、防护、误判治理和负责任采集为边界。
3. 工具与协议引用优先使用 RFC 和官方文档。

## 快速校验

```bash
python scripts/validate_questions.py
```

校验项：100 个 Q 文件、Q001-Q100 无缺号、front matter ID 一致、PDF/DOCX 源文件存在、每题包含核心章节、最低内容深度、章节/附录污染追问检测。

## License

仓库未替维护者擅自选择开源许可证。请在公开发布前根据你的发布目的选择合适许可证；见 [`LICENSE`](LICENSE)。
