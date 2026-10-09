# 仓库结构与命名约定 · REPO_STRUCTURE

本文件说明 **Engineer Interview 100** 各子教程的目录形态、题源命名差异，以及新增内容时的约定。目的是：**让差异可控、可预期**，而不是强行把 35 套独立生成的教程改成同一套物理布局（那会破坏各教程自带的 MkDocs `nav` 与题内相对链接）。

## 1. 顶层结构

```text
engineer-interview/
├── README.md                # 总览（35 教程 / 3,533 题）
├── REPO_STRUCTURE.md        # 本文件：结构约定
├── LICENSE-NOTICE.md        # 根级授权状态说明
├── index.html               # 重定向到线上站（GitHub Pages）
├── site/                    # 构建产物（.gitignore 忽略）
│   └── build.py             # 静态站生成器
└── <collection>/            # 每个方向一个独立子教程（35 个）
```

## 2. 子教程的四种题源布局（均为合法）

`site/build.py` **递归遍历**每个子教程、按 Markdown frontmatter 识别题目，因此以下布局都能被正确收录：

| 形态 | 典型目录 | 代表教程 |
|---|---|---|
| **A. `docs/` 章节式（MkDocs）** | `docs/<NN-chapter>/qNNN-slug.md` | `macroeconomics-interview-100`、`sqlite-interview-100` |
| **B. `questions/` 平铺式** | `questions/<NN-chapter>/QNNN-slug.md` | `rl-interview-100-v2`、`control-theory-interview-100-v1.1.0` |
| **C. `docs/questions/` 混合式** | `docs/questions/<NN-chapter>/QNNN.md` | `embodied-ai-interview-100`、`microeconomics-interview-100` |
| **D. 章节导读式（书籍型，非 100 题）** | `chapters/<NN-topic>.md` | `can-interview-offer`（未完成，见 §5） |

> 差异来源：面向 MkDocs 发布的教程必须把正文放在 `docs/` 下（否则 `mkdocs build` 找不到）；非 MkDocs 教程则常用根级 `questions/`。二者**不应**互相迁移。

## 3. 命名约定

- **题目文件名**：`Q001.md`、`q001.md`、`Q001-mdp-five-tuple.md`、`q001-*.md` 均**被接受**。
  - 大写 `Q` 多见于早期/母题式教程；小写 `q` 多见于新生成教程；带 slug 后缀更利于搜索。
  - **`site/build.py` 以 frontmatter 为准**，不依赖文件名大小写：
    - `id`（可选）：显式题号；缺省时从 `title` 前缀（如 `Q001`）推断；
    - `title`（**必需**）：无 `title` 的 Markdown 会被当作普通文档、**不进入题库**；
    - 其余可选：`chapter` / `chapter_title`、`difficulty` / `level` / `priority`、`tags` / `type` / `topics`、`must_do`、`frequency`。
- **章节目录**：建议 `<NN>-<kebab-topic>`（两位序号 + 主题），保证排序稳定。
- **其它文档**（`README.md`、`how-to-use`、`rubric`、`roadmap`、`knowledge-map` 等）：**不要**加 frontmatter `title`，以免被误收进题库。

## 4. 每个子教程建议自带的文件

| 文件 | 必需 | 说明 |
|---|---|---|
| `README.md` | ✅ | 方向定位、章节导航、快速入口 |
| `CONTRIBUTING.md` | ✅ | 该套内容的贡献规范 |
| `LICENSE` / `LICENSE.md` / `LICENSE-NOTICE.md` | ✅ | 授权状态（当前多为"未预选许可证"） |
| 学习路线（`roadmap` / `study-plan` / `learning-path`） | 建议 | 冲刺/系统学习路径 |
| 面试评分 Rubric | 建议 | 自测与模拟面试用 |
| `knowledge-map` / 能力地图 | 建议 | 建立全局图景 |
| 配套 PDF | ✅ | 整本手册，供离线/站内阅读 |
| `mkdocs.yml` | 可选 | 需要独立文档站时提供 |

## 5. 未完成 / 未上线的内容

`can-interview-offer`（车载 CAN）目前只有章节导读，题源 `questions/` 目录尚未落地，因此被 `site/build.py` 的 `SKIP_SLUGS` 排除，不进入站点与题量统计。

补齐 100 题题解后：从 `site/build.py` 的 `SKIP_SLUGS` 中移除该条目 → 运行 `python3 site/build.py` → 部署 `gh-pages`。

## 6. 新增一个子教程

1. 建目录 `<name>-interview-100/`，放入 `docs/` 或 `questions/` 题源；
2. 每题写 frontmatter（至少 `title`，建议 `id`/`chapter`/`tags`）；
3. 补 `README.md`、`CONTRIBUTING.md`、`LICENSE-NOTICE.md`、PDF；
4. 在 `site/build.py` 的 `META` 增加该集合的 `name`/`latin`/`cn`/`tagline`/`chips`/`domain`，并在 `GLYPH` 加一个符号；
5. `python3 site/build.py` 本地验证 → 同步 README 表格与统计。

> **为何不做物理统一**：35 套教程分别带 MkDocs `nav` 与大量题内相对链接（`../Q002.md` 等）。批量重命名/移动会静默破坏这些链接与 MkDocs 构建。因此本仓库选择**约定优先、不强制迁移**：通过 `build.py` 的 frontmatter 识别 + 本文件记录差异来保证可维护性。
