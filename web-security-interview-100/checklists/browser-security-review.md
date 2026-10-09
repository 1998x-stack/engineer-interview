# Browser Security Review Checklist

- [ ] 区分 origin 与 site。
- [ ] 区分“请求能否发送 / 凭据是否附带 / 响应能否读取 / DOM 能否访问”。
- [ ] XSS 输出是否按最终上下文处理？
- [ ] 是否尽量使用 textContent 等非解释型 API？
- [ ] CSRF 是否验证 user intent，而非只依赖 POST/SOP？
- [ ] Credentialed CORS 是否使用严格 Origin allowlist？
- [ ] CSP/Trusted Types/SameSite 是否定位为纵深防御？


## Review Evidence

完成 checklist 不等于完成安全验证。评审结果至少应保留以下证据：

- 被评审的 commit / build / deployment version；
- 关键架构图或数据流图版本；
- 通过与失败的测试用例及对应日志；
- 发现问题的 owner、严重度、修复截止时间与复测结果；
- 对接受风险或例外控制的书面说明与到期时间；
- 能证明控制在生产运行的日志、指标或策略配置。

建议把 checklist 项目尽量转成 **可自动验证的 policy/test**，把人工 review 留给业务语义、复杂授权和跨组件边界等自动化难以覆盖的区域。
