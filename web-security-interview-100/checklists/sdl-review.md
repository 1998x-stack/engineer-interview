# SDL / AppSec Program Checklist

- [ ] 安全要求是否映射到 ASVS/内部标准？
- [ ] 是否有 threat model / trust boundary / asset inventory？
- [ ] SAST/SCA/DAST/Secrets/IaC/Container 等工具是否有 owner 与修复闭环？
- [ ] 高风险业务是否有定制授权与业务逻辑测试？
- [ ] 生产日志、告警与 incident runbook 是否演练过？
- [ ] 风险接受是否有期限、owner、补偿控制？
- [ ] 事件/漏洞复盘是否回馈到 secure-by-default 平台？


## Review Evidence

完成 checklist 不等于完成安全验证。评审结果至少应保留以下证据：

- 被评审的 commit / build / deployment version；
- 关键架构图或数据流图版本；
- 通过与失败的测试用例及对应日志；
- 发现问题的 owner、严重度、修复截止时间与复测结果；
- 对接受风险或例外控制的书面说明与到期时间；
- 能证明控制在生产运行的日志、指标或策略配置。

建议把 checklist 项目尽量转成 **可自动验证的 policy/test**，把人工 review 留给业务语义、复杂授权和跨组件边界等自动化难以覆盖的区域。
