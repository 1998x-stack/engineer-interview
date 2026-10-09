# Access Control Review Checklist

- [ ] 是否明确 Subject / Resource / Action / Tenant / State？
- [ ] 是否所有入口（REST/GraphQL/WebSocket/job/RPC）调用同一授权策略？
- [ ] 是否覆盖对象级、函数级、属性级授权？
- [ ] 是否默认拒绝未知动作/资源？
- [ ] 是否存在客户端自报 role/tenant/owner 作为授权依据？
- [ ] 是否有跨账户、跨租户 negative tests？
- [ ] 权限/角色变化后缓存与长连接是否及时失效？


## Review Evidence

完成 checklist 不等于完成安全验证。评审结果至少应保留以下证据：

- 被评审的 commit / build / deployment version；
- 关键架构图或数据流图版本；
- 通过与失败的测试用例及对应日志；
- 发现问题的 owner、严重度、修复截止时间与复测结果；
- 对接受风险或例外控制的书面说明与到期时间；
- 能证明控制在生产运行的日志、指标或策略配置。

建议把 checklist 项目尽量转成 **可自动验证的 policy/test**，把人工 review 留给业务语义、复杂授权和跨组件边界等自动化难以覆盖的区域。
