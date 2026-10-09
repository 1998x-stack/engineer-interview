# HTTP Infrastructure Review Checklist

- [ ] CDN/LB/WAF/Proxy/Backend 的 HTTP 版本与 parser 是否明确？
- [ ] 是否拒绝歧义 framing/header/parameter？
- [ ] URL/query/header normalization 是否一致？
- [ ] Cache key 是否覆盖所有会影响安全响应的输入？
- [ ] Host/X-Forwarded-* 是否只信任明确 proxy chain？
- [ ] 私有响应是否不会进入公共缓存？
- [ ] 关键并发业务不变量是否原子化？


## Review Evidence

完成 checklist 不等于完成安全验证。评审结果至少应保留以下证据：

- 被评审的 commit / build / deployment version；
- 关键架构图或数据流图版本；
- 通过与失败的测试用例及对应日志；
- 发现问题的 owner、严重度、修复截止时间与复测结果；
- 对接受风险或例外控制的书面说明与到期时间；
- 能证明控制在生产运行的日志、指标或策略配置。

建议把 checklist 项目尽量转成 **可自动验证的 policy/test**，把人工 review 留给业务语义、复杂授权和跨组件边界等自动化难以覆盖的区域。
