# 公开依据与经典参考

## A. 配套 PDF 中列出的公开依据/论文

这些链接来自 PDF 源题库，用于佐证题型或技术定义；公开面经仅证明题型出现过，不意味着仓库中每道同类题都来自某一家公司原题。

1. [公开面经：Conv2d/padding/R-CNN/Faster R-CNN/YOLO/FCN](https://www.nowcoder.com/discuss/353156063987965952)
2. [公开面经：MobileNet/ROIAlign/Smooth L1/NMS/BN/U-Net/Mask R-CNN](https://www.nowcoder.com/discuss/353158337850187776)
3. [2025 公开面经：CNN vs Transformer、SAM/SAM2、工业缺陷、YOLOv10](https://www.nowcoder.com/feed/main/detail/0358f324fd16467c8b711a3dd3e2882f)
4. [OpenAI：Multimodal Perception and Authentication](https://openai.com/careers/machine-learning-engineer-multimodal-perception-and-authentication-san-francisco/)
5. [OpenAI：Researcher, Multimodal Safety](https://openai.com/careers/researcher-multimodal-safety-san-francisco/)
6. [ViT](https://arxiv.org/abs/2010.11929)
7. [DETR](https://arxiv.org/abs/2005.12872)
8. [SAM](https://arxiv.org/abs/2304.02643)
9. [SAM 2](https://arxiv.org/abs/2408.00714)
10. [Faster R-CNN](https://arxiv.org/abs/1506.01497)
11. [FPN](https://arxiv.org/abs/1612.03144)
12. [Focal Loss](https://arxiv.org/abs/1708.02002)
13. [U-Net](https://arxiv.org/abs/1505.04597)
14. [DeepLabv3+](https://arxiv.org/abs/1802.02611)
15. [CLIP](https://arxiv.org/abs/2103.00020)
16. [MAE](https://arxiv.org/abs/2111.06377)
17. [DDPM](https://arxiv.org/abs/2006.11239)
18. [Latent Diffusion](https://arxiv.org/abs/2112.10752)
19. [ControlNet](https://arxiv.org/abs/2302.05543)

## B. Repo 扩展的经典论文

下面这些用于让独立 Markdown 页面有更完整的原始论文入口，属于仓库扩展阅读：

- [Batch Normalization](https://arxiv.org/abs/1502.03167)
- [ResNet](https://arxiv.org/abs/1512.03385)
- [MobileNetV1](https://arxiv.org/abs/1704.04861)
- [MobileNetV2](https://arxiv.org/abs/1801.04381)
- [AdamW](https://arxiv.org/abs/1711.05101)
- [Mask R-CNN](https://arxiv.org/abs/1703.06870)
- [CRNN](https://arxiv.org/abs/1507.05717)
- [Swin Transformer](https://arxiv.org/abs/2103.14030)
- [DiT](https://arxiv.org/abs/2212.09748)
- [mixup](https://arxiv.org/abs/1710.09412)
- [CutMix](https://arxiv.org/abs/1905.04899)

## 版本原则

- 题型来源和技术参考分开记录。
- 当前/前沿岗位要求不应被写成“历史原题”。
- 对会快速迭代的模型（如 SAM 系列、VLM、生成视觉），公开发布前应重新核验版本与论文。


## 如何使用论文列表

面试准备不需要逐篇复现所有论文。建议对每篇经典工作只回答五个问题：

1. 前一代方法的具体 failure mode 是什么？
2. 它提出的最小核心机制是什么？
3. 关键公式/信息流如何解释？
4. 代价或失败场景是什么？
5. 今天的后续工作保留了什么、替换了什么？

对于当前岗位/前沿方法，论文链接属于扩展阅读，不应把论文中的实验结论无条件迁移到自己的数据和硬件。
