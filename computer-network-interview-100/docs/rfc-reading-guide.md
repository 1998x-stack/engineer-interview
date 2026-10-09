# RFC 阅读方法

不要从 RFC 第 1 页开始线性背诵。推荐“问题驱动阅读”：

1. 先写下具体问题，例如“TIME_WAIT 的正确性目的是什么？”
2. 在 RFC 中定位状态机/术语/规范性要求（MUST/SHOULD/MAY）。
3. 分清 **协议规范** 与 **Linux 实现**。
4. 用最小实验或抓包验证实现行为。
5. 对随版本变化的默认值，不写成协议永久事实。

## 推荐入口

- TCP：RFC 9293 → RFC 5681 → RFC 9438。
- HTTP：RFC 9110（语义）→ RFC 9111（缓存）→ RFC 9112/9113/9114。
- QUIC：RFC 9000 + RFC 9002。
- TLS：RFC 9846（现行 TLS 1.3 规范）+ RFC 5280；RFC 8446 作为历史版本对照。
- Linux：Kernel networking docs + man-pages。
