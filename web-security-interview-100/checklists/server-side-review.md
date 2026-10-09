# Server-side Capability Review Checklist

- [ ] 是否盘点所有 URL fetch / webhook / file / archive / deserialization 能力？
- [ ] SSRF 是否采用 allowlist + 解析后网络策略 + redirect 重校验？
- [ ] 文件路径是否 canonicalize 后做 containment？
- [ ] 上传是否隔离存储、不可执行、限制资源？
- [ ] 反序列化是否禁止任意类型/副作用？
- [ ] 云工作负载 IAM 与 egress 是否最小权限？


## Review Evidence

完成 checklist 不等于完成安全验证。评审结果至少应保留以下证据：

- 被评审的 commit / build / deployment version；
- 关键架构图或数据流图版本；
- 通过与失败的测试用例及对应日志；
- 发现问题的 owner、严重度、修复截止时间与复测结果；
- 对接受风险或例外控制的书面说明与到期时间；
- 能证明控制在生产运行的日志、指标或策略配置。

建议把 checklist 项目尽量转成 **可自动验证的 policy/test**，把人工 review 留给业务语义、复杂授权和跨组件边界等自动化难以覆盖的区域。
