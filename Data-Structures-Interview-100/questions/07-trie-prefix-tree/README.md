# Trie / Prefix Tree

> 本章覆盖 **067-072**，共 6 题。

## 源书稿章节导语

> 把字符串集合压缩成公共前缀图；理解空间换查询与前缀剪枝。

## 章节能力目标

- 字符串长度 L 往往比词典规模更重要；注意节点空间、终止标记、Top-K 缓存和删除/剪枝。

## 深化版章节训练目标

**章节核心：** 共享前缀与字符串搜索剪枝

**主要 Pattern：** `Trie / Wildcard DFS / Top-K Cache`

### 面试前的三次检查

1. terminal 与 prefix node 分开
2. alphabet 决定 children 表示
3. 读优化通常带来写放大

### 难度分布

- `H`：3 题
- `M`：3 题

### 推荐训练顺序

1. **基础结构题**：先练接口与基本不变量，不追求花哨优化。
2. **Pattern 题**：把同一结构的 2–3 题连续做，找共同状态定义。
3. **Hard/变体题**：只看约束，不看题名，练从 baseline 推 structure。
4. **Follow-up 复盘**：不重写整题，只回答“哪个前提变了、哪一层结构要换”。

> 章节 README 只负责能力地图；真正的证明、代码审查与对抗测试都在各 `Qxxx.md` 的 §12 专业深化中。

## 题目列表

| ID | 题目 | 难度 | 核心 |
|---|---|---|---|
| Q067 | [实现 Trie：insert/search/startsWith](Q067-实现-Trie-insert-search-startsWith.md) | M | Trie / 字符串 |
| Q068 | [支持通配符 . 的词典](Q068-支持通配符-.-的词典.md) | M | Trie / DFS |
| Q069 | [Autocomplete：前缀返回 Top-K 候选](Q069-Autocomplete-前缀返回-Top-K-候选.md) | H | Trie / Heap |
| Q070 | [Word Search II：棋盘中查找多个单词](Q070-Word-Search-II-棋盘中查找多个单词.md) | H | Trie / DFS |
| Q071 | [最短词根替换句子](Q071-最短词根替换句子.md) | M | Trie / 字符串 |
| Q072 | [层级路径/域名祖先值聚合](Q072-层级路径-域名祖先值聚合.md) | H | Trie / Tree |
