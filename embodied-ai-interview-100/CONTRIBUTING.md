# Contributing

感谢参与改进。

## 推荐贡献类型

- 修正公式、坐标系、算法定义；
- 补充公开可核验的面试题来源；
- 增加实机 Gotcha / failure case；
- 增加论文复现和最小实验；
- 更新 2026+ VLA / World Model / Robot Learning 资料。

## Question Markdown 规范

每题必须保留：

1. `PDF Core` 与 `Repository Expansion` 的边界；
2. 面试官意图与 30 秒回答；
3. 至少一个工程指标或验证实验；
4. 对高风险/不确定事实提供一手来源；
5. 不把自拟题冒充公开公司真题。

提交前运行：

```bash
python scripts/validate_repo.py
```
