# v2 深度增强交付报告

## 本轮目标

将原有“100 道独立面试题 Markdown”从提纲型内容升级为可以独立阅读、复现实验、源码追踪和用于面试评分的专业技术章节。

## 结果

- 100 / 100 道题完成深度增强。
- 题目正文总量约 57.8 万字符。
- 平均每题约 5.78K 字符；最短题目也超过 5.4K 字符。
- 每题统一具备 14 个主章节。
- 新增 10 个章节级 Lab。
- 新增统一 SQLite 源码阅读指南。
- 内部 Markdown 相对链接：1,076 个，全部通过检查。
- SQLite 稳定版本基线：3.53.4（2026-07-24）。

## 每题新增的专业层

1. 面试评分 Rubric：0～4 分，明确“背到结论 / 机制正确 / 工程可用 / 专家级”的差异。
2. SQLite 子系统定位：把问题放到 Parser / Planner / VDBE / B-Tree / Pager / WAL / VFS 中理解。
3. 四层推导：SQL 语义 → Planner/执行 → B-Tree/Pager/WAL → 工程决策。
4. 可验证方法：EQP、PRAGMA、typeof、双连接实验、page/WAL/index 统计等。
5. 性能/正确性/可维护性权衡。
6. 反例、边界条件和故障注入问题。
7. 源码树阅读入口。
8. 对应章节 Lab。
9. 一分钟复习卡。

## QA 命令

```bash
python scripts/validate_repo.py
python scripts/check_links.py
```

当前结果：

```text
OK: 100 enriched question markdown files + 10 labs + metadata + PDF + indexes
OK: 1076 internal Markdown links checked
```

## MkDocs

仓库保留 `mkdocs.yml` 和 `requirements-docs.txt`。本交付环境未预装 `mkdocs-material/pymdownx`，因此本轮只做了 YAML 结构检查；在安装 requirements 后即可执行：

```bash
pip install -r requirements-docs.txt
mkdocs build --strict
```
