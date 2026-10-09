# Chapter 02 · 底层编码与内存机制

理解 SDS、listpack、quicklist、哈希表、跳表以及编码切换，建立 Big Key / Hot Key / 碎片治理能力。

## 本章目标

完成 Q011–Q020 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q011](q011.md) | Redis String 底层为什么不用普通 C 字符串？ | 中级 | PDF p.16 |
| [Q012](q012.md) | embstr、raw、int 有什么区别？ | 中级 | PDF p.17 |
| [Q013](q013.md) | List 的底层结构是什么？ | 中级 | PDF p.18 |
| [Q014](q014.md) | Hash 的底层结构是什么？ | 中级 | PDF p.19 |
| [Q015](q015.md) | Redis 为什么会自动改变 encoding？ | 中级 | PDF p.20 |
| [Q016](q016.md) | 什么是 Big Key？ | 基础必会 | PDF p.21 |
| [Q017](q017.md) | Big Key 如何治理？ | 中级 | PDF p.22 |
| [Q018](q018.md) | 什么是 Hot Key？ | 基础必会 | PDF p.23 |
| [Q019](q019.md) | Hot Key 怎么解决？ | 中级 | PDF p.24 |
| [Q020](q020.md) | Redis 为什么可能出现内存碎片？ | 中级 | PDF p.25 |

## 本章工程主线

- 使用 `OBJECT ENCODING`、`MEMORY USAGE` 和真实数据分布验证内部编码假设。
- 不要把内部 encoding 当稳定 API；版本升级后实现可能变化。

## 官方参考

- [object_encoding](https://redis.io/docs/latest/commands/object-encoding/)
- [data_types](https://redis.io/docs/latest/develop/data-types/)
- [cli](https://redis.io/docs/latest/develop/tools/cli/)

[← 返回总目录](../../README.md)
