# Repository Architecture

## 为什么一题一文件

- 可以独立 review / issue / PR；
- 链接稳定，便于 Anki、知识库或 RAG 索引；
- front matter 可用于生成题单、难度筛选和学习进度工具；
- 章节目录只表达知识域，不把内容重新耦合成一本大文件。

## 元数据

`metadata/questions.json` 和 `questions.jsonl` 保存 ID、章节、难度、优先级、PDF 页码、tags 与路径，可直接用于：

- 生成静态站点导航；
- 导入向量数据库 / RAG；
- 构建随机 mock interview；
- 统计复习进度。

## 内容分层

每题固定为“口述层 → 原理层 → 数学/shape → 代码 → 工程 → 追问 → 复盘”。固定 schema 的好处是面试训练时形成稳定认知模板，而不是每道题重新决定如何学习。
