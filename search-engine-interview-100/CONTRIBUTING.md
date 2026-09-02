# Contributing

欢迎修正公式、补充反例、工程案例与新参考资料。

## 修改原则

- 一题一 Markdown，不改变 `Qxxx` ID。
- 新增事实性参数（例如 Lucene/Faiss/LightGBM 当前默认值）请给官方文档或论文链接。
- 区分“算法定义”“具体库实现”“经验性工程建议”。
- 不把未经核验的公开面经写成“公司官方真题”。
- 任何代码片段尽量保持最小可运行或明确标记伪代码。

## 提交前

```bash
python scripts/validate_repo.py
```
