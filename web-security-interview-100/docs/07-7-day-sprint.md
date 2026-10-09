# 7 天冲刺复习计划

| 日期 | 范围 | 主题 | 验收标准 |
|---|---|---|---|
| Day 1 | Q001-Q020 | HTTP/浏览器基础 + Access Control | SOP/CORS/AuthN/AuthZ/IDOR/BOLA 能脱稿讲清 |
| Day 2 | Q021-Q042 | Session/JWT/OAuth + Injection | 能解释生命周期与解释器边界 |
| Day 3 | Q043-Q064 | XSS/CSRF + SSRF/文件/反序列化 | 能区分浏览器与服务器能力边界 |
| Day 4 | Q065-Q084 | HTTP 高阶 + API/GraphQL/WebSocket | 能解释 parser differential 与现代 API 风险 |
| Day 5 | Q085-Q100 | 供应链/日志/异常 + SDL/代码审计 | 能从漏洞上升到工程体系 |
| Day 6 | 随机 50 题 | 只看题目口述 1 分钟 | 找到“会看不会说”的知识 |
| Day 7 | 100 题二刷 | 每题回答根因/防御/验证/追问 | 形成稳定面试表达 |

## 每天的复习动作

1. 先只读题目，30 秒给一句话结论。
2. 关掉答案，用白板画 trust boundary / data flow。
3. 写一条 security invariant。
4. 回答“错误防御为什么错”。
5. 最后对照 GitHub 增强版审计清单补缺。


## 每日固定训练动作

每天除了阅读题目，再固定完成：

- 选 3 题画出简化数据流/信任边界图；
- 选 2 题写出 Security Invariant；
- 选 2 题设计 negative regression test；
- 选 1 题用 5 分钟做 Senior 级回答；
- 当天结束前复盘：哪些回答仍停留在“背最佳实践”，没有说明为什么。
