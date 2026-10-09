# 第九章 Socket、epoll 与 Linux 网络栈

把协议知识落到系统调用、事件循环与内核收包路径。

## 本章能力目标

- 高并发网络程序的关键是把“等待就绪”和“真正读写数据”分开，epoll 通知 readiness，而不是替应用完成 read/write。
- ET 模式的正确性依赖 nonblocking + drain-until-EAGAIN；任何阻塞系统调用都可能卡住整个 event loop。
- 性能优化必须追踪数据路径：NIC queue → softirq/NAPI → protocol stack → socket queue → userspace。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **Readiness 不是 Completion**：epoll 告诉“现在可做 IO”，应用仍要正确处理 partial read/write/EAGAIN。
- **Event loop 正确性优先于 API 名字**：ET/LT、nonblocking、EPOLLOUT、ONESHOT 都服务于 fd 状态机与所有权。
- **网络栈瓶颈可能在 softirq/NIC queue**：业务线程不忙并不代表机器网络处理还有余量。

### 本章白板题

1. 画 `socket→bind→listen→accept4→recv/send→close`，标 listener/connected fd 区别。
2. 写 ET read loop 伪代码，包含 EAGAIN/EOF/error/SSL WANT_READ-WANT_WRITE。
3. 画 NIC RX→NAPI→GRO→IP/TCP→socket queue→recv，并解释 RSS/RPS/RFS。

### 最小实验组合

`strace -e network`、`ss`、`perf top`、`/proc/softirqs`、`ethtool -l/-x/-S`、`tcpdump`。目标是把 syscall、socket queue、softirq 和 packet timeline 连起来。
<!-- CHAPTER-V2-END -->

## 题目目录

- [081. 一个 TCP Server 从 socket() 到处理请求的系统调用流程是什么？](081-tcp-server-socket-syscalls.md) · 基础 · ★★★★★
- [082. Blocking Socket 与 Non-blocking Socket 的核心区别是什么？](082-blocking-vs-nonblocking-socket.md) · 基础 · ★★★★★
- [083. 经典五种 I/O Model 是什么？readiness 与 completion 的区别是什么？](083-five-io-models.md) · 进阶 · ★★★★☆
- [084. select、poll、epoll 的核心差异是什么？](084-select-poll-epoll.md) · 进阶 · ★★★★★
- [085. epoll LT 与 ET 有什么区别？ET 为什么要求“读到 EAGAIN”？](085-epoll-lt-vs-et.md) · 进阶 · ★★★★★
- [086. 为什么 epoll ET 几乎总与 nonblocking socket 搭配？](086-epoll-et-nonblocking.md) · 进阶 · ★★★★★
- [087. 为什么 epoll 对普通磁盘文件意义有限？](087-epoll-regular-files.md) · 进阶 · ★★★☆☆
- [088. send() 返回成功，是否意味着对端已经收到或处理？](088-send-success-semantics.md) · 工程 · ★★★★★
- [089. Zero Copy 的目标是什么？sendfile、splice、mmap 各自大致减少了什么？](089-zero-copy-sendfile-splice-mmap.md) · 进阶 · ★★★★☆
- [090. 一个 Packet 从 NIC 到应用 recv() 大致经过哪些 Linux 网络栈阶段？](090-linux-packet-receive-path.md) · 高级 · ★★★★☆

## 推荐实践工具

- `ss -tanp`
- `strace`
- `perf top`
- `cat /proc/softirqs`

[← 返回全书目录](../../README.md)
