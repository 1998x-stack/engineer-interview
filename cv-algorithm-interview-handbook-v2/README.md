# Computer Vision Algorithm Interview Handbook

> 图像算法岗 100 道真题型面试题 · 2026 Edition  
> 基础原理 × 真题追问 × 工程落地 × 前沿视觉

这个仓库把配套 PDF 完整拆分为 **100 个独立 Markdown 问题页**，并在 PDF 原有内容上增加更适合 GitHub 长期维护的扩展解析：30 秒回答、2-5 分钟口述框架、公式、追问参考答案、代码/伪代码、工程诊断、自测清单与关联题。

> [!NOTE]
> “剑指 Offer”仅用于描述**题目驱动、递进追问、方法总结**的组织风格。本仓库不复刻任何同名书籍受版权保护的原文，与其作者/出版社无关联。

## 仓库特点

- **100/100 一题一文件**：`Q001` 到 `Q100` 连续编号，可独立链接和复习。
- **10 个知识章节**：传统 CV、CNN、检测、分割、OCR、视觉基础模型、生成视觉、视频/3D/多模态、数据评测、部署系统。
- **面试口述导向**：每题均有 30 秒结论、2-5 分钟展开、追问链和失分点。
- **工程导向**：不是只背网络结构，强调数据、指标、失败模式、部署与 SLA。
- **可维护**：YAML front matter、问题元数据 JSON/CSV、MkDocs 导航、CI 完整性校验。
- **原始 PDF 随仓库保留**：[下载/查看 PDF](assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf)。


## V2 深度版新增内容

第二版对 100 个问题页进行了系统深化，不再只提供“答案骨架”：

- **每题专属技术补充**：公式口径、shape、复杂度、边界和实现细节；
- **专业推理链**：从现象→机制→收益→代价→失败模式→验证；
- **工程诊断矩阵**：看到某类线上/训练异常时，优先怀疑什么、如何最小验证；
- **消融模板**：control、slice、cost、regression、repeatability；
- **专家级追问**：把已有追问继续推到反例、数据分布和部署后果；
- **章节学习目标**：10 章 README 现在同时承担课程 syllabus；
- **强化速查**：公式、手撕、项目拷问和 30 天路线均升级。

本仓库把 PDF 作为题目基线；V2 的“专业深化”明确标注为通用 CV/工程知识扩展，不把扩展内容伪装成某家公司逐字真题。

## 建议阅读顺序

1. 第一次：先读 [`Top 30`](docs/11-cheatsheets/top30.md)，建立面试地图。
2. 第二次：逐章刷题，每题先遮住正文口述 3 分钟。
3. 第三次：只看“高频追问”，强迫自己回答为什么、边界条件和工程代价。
4. 面试前 48 小时：公式速查 + IoU/NMS/BN 手撕 + 项目拷问。

## 章节导航

| # | 章节 | 题号 | 定位 |
|---:|---|---|---|
| 01 | [传统图像处理与视觉基础](docs/01-traditional-cv/README.md) | Q001-Q010 | 把图像看成信号：卷积、频域、边缘、颜色、尺度与几何。 |
| 02 | [CNN 与深度学习基本功](docs/02-cnn-fundamentals/README.md) | Q011-Q025 | 把经典模块讲到“公式 - 直觉 - 优缺点 - 工程后果”。 |
| 03 | [目标检测](docs/03-object-detection/README.md) | Q026-Q040 | 从 R-CNN 到 YOLO/DETR：检测是图像算法岗最常见主战场。 |
| 04 | [图像分割](docs/04-segmentation/README.md) | Q041-Q050 | 语义、实例、全景分割，以及工业/医学中的边界与长尾问题。 |
| 05 | [OCR 与文档视觉](docs/05-ocr-document-vision/README.md) | Q051-Q058 | 文本检测、识别、CTC、几何矫正与线上域偏移。 |
| 06 | [ViT、自监督、CLIP 与 SAM](docs/06-vision-foundation-models/README.md) | Q059-Q067 | 从 CNN inductive bias 走向视觉基础模型和 promptable perception。 |
| 07 | [Diffusion 与生成视觉](docs/07-generative-vision/README.md) | Q068-Q075 | 理解扩散模型的训练目标、latent、guidance、可控生成和评价。 |
| 08 | [视频、3D 与多模态](docs/08-video-3d-multimodal/README.md) | Q076-Q082 | 时间、几何、传感器融合与 VLM：面向 2026 岗位能力结构。 |
| 09 | [数据、训练与 Evaluation](docs/09-data-training-evaluation/README.md) | Q083-Q089 | 真正区分候选人的往往是数据诊断、实验设计与误差分析。 |
| 10 | [压缩、部署、系统设计与手撕](docs/10-deployment-system-coding/README.md) | Q090-Q100 | 从 FLOPs 到真实延迟，从 PyTorch 到 TensorRT，从模型到可上线系统。 |

## 高频速查

- [Top 30 必会](docs/11-cheatsheets/top30.md)
- [公式速查](docs/11-cheatsheets/formulas.md)
- [三段高频手撕](docs/11-cheatsheets/coding-drills.md)
- [项目拷问 30 题](docs/11-cheatsheets/project-grilling.md)
- [30 天复习路线](docs/11-cheatsheets/30-day-plan.md)
- [面试回答框架](docs/00-guide/answer-framework.md)
- [经典论文与公开依据](references/papers.md)

## 本地文档站

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

然后访问终端提示的本地地址。GitHub CI 还会检查：问题总数、连续编号、YAML 元数据、章节范围、PDF 是否存在。

## 内容来源与扩展边界

问题标题、核心结论、PDF 中的标准回答要点、高频追问、失分点、工程视角与一句话记忆来自仓库配套 PDF 的源题库。Markdown 中标记为“深入解析 / 追问参考答案 / 工程扩展”的内容是在这些材料基础上的通用 CV 知识扩展，用于把 PDF 的复习提纲升级为可独立学习的题解。

公开面经只用于佐证题型；ViT、SAM、VLM、生成视觉等用于覆盖 2026 岗位能力结构，不将无法核实的问题冒充某家公司原题。

## Repository statistics

- Questions: **100**
- Chapters: **10**
- Top 30: **30**
- Original PDF: **65 pages**

---

如果用于正式公开发布，请在发布前再次检查招聘面经链接的可访问性及所选内容许可证。
