# 100 道题总目录

> 每题一个 Markdown；PDF 基线与扩展内容分层标识。

## 1. [C++ 对象模型与语言机制](01-cpp-object-model/README.md)

- [Q001 · C++ 虚函数和运行时多态到底是怎么实现的？](01-cpp-object-model/Q001.md) - `Advanced`
- [Q002 · 为什么基类析构函数经常必须是 virtual？](01-cpp-object-model/Q002.md) - `Intermediate`
- [Q003 · 为什么构造函数不能是 virtual？构造期间调用 virtual function 会怎样？](01-cpp-object-model/Q003.md) - `Intermediate`
- [Q004 · unique_ptr、shared_ptr、weak_ptr 底层有什么区别？](01-cpp-object-model/Q004.md) - `Advanced`
- [Q005 · shared_ptr 为什么会发生循环引用？如何从设计上避免？](01-cpp-object-model/Q005.md) - `Intermediate`
- [Q006 · 左值、右值、std::move、移动构造究竟解决什么问题？](01-cpp-object-model/Q006.md) - `Intermediate`
- [Q007 · std::vector 扩容时发生了什么？哪些引用会失效？](01-cpp-object-model/Q007.md) - `Intermediate`
- [Q008 · vector 为什么常常比 list 更快，即使 list 插入是 O(1)？](01-cpp-object-model/Q008.md) - `Intermediate`
- [Q009 · new/delete 与 malloc/free 有什么区别？为什么不能混用？](01-cpp-object-model/Q009.md) - `Intermediate`
- [Q010 · C++ Reflection 为什么难？游戏引擎如何实现反射？](01-cpp-object-model/Q010.md) - `Advanced`

## 2. [内存、STL 与数据导向设计](02-memory-data-oriented/README.md)

- [Q011 · 游戏引擎为什么特别在意内存对齐？](02-memory-data-oriented/Q011.md) - `Intermediate`
- [Q012 · Stack 和 Heap 的区别是什么？实时引擎如何选择？](02-memory-data-oriented/Q012.md) - `Intermediate`
- [Q013 · 如何设计一个固定大小 Memory Pool？](02-memory-data-oriented/Q013.md) - `Intermediate`
- [Q014 · Arena / Linear Allocator 为什么适合每帧临时对象？](02-memory-data-oriented/Q014.md) - `Intermediate`
- [Q015 · AoS 和 SoA 有什么区别？为什么 SoA 常用于热点系统？](02-memory-data-oriented/Q015.md) - `Intermediate`
- [Q016 · ECS 为什么越来越常见？它解决了什么，又带来什么成本？](02-memory-data-oriented/Q016.md) - `Advanced`
- [Q017 · Hash Map 和红黑树怎么选？](02-memory-data-oriented/Q017.md) - `Intermediate`
- [Q018 · Object Pool 适合什么场景？如何避免把它用成“内存垃圾场”？](02-memory-data-oriented/Q018.md) - `Intermediate`
- [Q019 · 什么是 Cache Miss？为什么游戏引擎比普通业务代码更在意？](02-memory-data-oriented/Q019.md) - `Intermediate`
- [Q020 · 什么是 False Sharing？如何定位与修复？](02-memory-data-oriented/Q020.md) - `Advanced`

## 3. [操作系统、多线程与并发](03-os-concurrency/README.md)

- [Q021 · Process 与 Thread 的区别是什么？](03-os-concurrency/Q021.md) - `Intermediate`
- [Q022 · Context Switch 为什么贵？](03-os-concurrency/Q022.md) - `Intermediate`
- [Q023 · 什么是 Job System？为什么比“一个子系统一个线程”更可扩展？](03-os-concurrency/Q023.md) - `Advanced`
- [Q024 · Mutex、Spinlock、Semaphore 怎么选？](03-os-concurrency/Q024.md) - `Intermediate`
- [Q025 · 什么是 Deadlock？四个必要条件是什么？](03-os-concurrency/Q025.md) - `Intermediate`
- [Q026 · 如何实现一个 SPSC 无锁环形队列？](03-os-concurrency/Q026.md) - `Advanced`
- [Q027 · memory_order_relaxed / acquire / release 是什么？](03-os-concurrency/Q027.md) - `Advanced`
- [Q028 · 虚拟地址如何转换成物理地址？Page Fault 发生了什么？](03-os-concurrency/Q028.md) - `Advanced`
- [Q029 · Game Thread 和 Render Thread 为什么要分开？](03-os-concurrency/Q029.md) - `Advanced`
- [Q030 · Triple Buffering 与 Frames in Flight 有什么作用？](03-os-concurrency/Q030.md) - `Advanced`

## 4. [数据结构与算法](04-algorithms/README.md)

- [Q031 · 10 万个数找最大的 1 万个，怎么做？](04-algorithms/Q031.md) - `Intermediate`
- [Q032 · 实现 A*，为什么它比 Dijkstra 更适合游戏寻路？](04-algorithms/Q032.md) - `Intermediate`
- [Q033 · A* 在开放世界地图里为什么仍可能很慢？](04-algorithms/Q033.md) - `Intermediate`
- [Q034 · Bresenham 画线算法为什么能避免浮点数？](04-algorithms/Q034.md) - `Intermediate`
- [Q035 · 二叉树最近公共祖先怎么做？](04-algorithms/Q035.md) - `Intermediate`
- [Q036 · 最长合法括号如何做到 O(N)？](04-algorithms/Q036.md) - `Intermediate`
- [Q037 · 所有节点出度 1，如何寻找最长环？](04-algorithms/Q037.md) - `Intermediate`
- [Q038 · 如何设计空间哈希解决大量对象邻域查询？](04-algorithms/Q038.md) - `Intermediate`
- [Q039 · Quadtree、Octree、BVH 有什么区别？](04-algorithms/Q039.md) - `Advanced`
- [Q040 · 动态对象很多时 BVH 怎么更新？](04-algorithms/Q040.md) - `Advanced`

## 5. [3D 数学与几何](05-3d-math/README.md)

- [Q041 · 游戏渲染中有哪些坐标空间？](05-3d-math/Q041.md) - `Intermediate`
- [Q042 · 齐次坐标为什么需要第四维？](05-3d-math/Q042.md) - `Intermediate`
- [Q043 · 为什么 Normal 不能直接乘 Model Matrix？](05-3d-math/Q043.md) - `Advanced`
- [Q044 · Quaternion 为什么适合表示旋转？](05-3d-math/Q044.md) - `Advanced`
- [Q045 · SLERP 和 LERP 有什么区别？](05-3d-math/Q045.md) - `Advanced`
- [Q046 · 如何判断一个点/包围体是否在视锥体中？](05-3d-math/Q046.md) - `Intermediate`
- [Q047 · Ray 与 Triangle 如何求交？](05-3d-math/Q047.md) - `Advanced`
- [Q048 · AABB 和 OBB 的区别？](05-3d-math/Q048.md) - `Intermediate`
- [Q049 · 什么是重心坐标？](05-3d-math/Q049.md) - `Intermediate`
- [Q050 · 为什么纹理属性必须做透视矫正插值？](05-3d-math/Q050.md) - `Advanced`

## 6. [实时渲染管线](06-real-time-rendering/README.md)

- [Q051 · 请完整讲一遍现代 GPU Rasterization Pipeline。](06-real-time-rendering/Q051.md) - `Advanced`
- [Q052 · Rasterization 本质上在做什么？](06-real-time-rendering/Q052.md) - `Intermediate`
- [Q053 · Vertex Shader 与 Fragment Shader 谁调用次数更多？](06-real-time-rendering/Q053.md) - `Intermediate`
- [Q054 · 什么是 Early-Z？它为什么能加速？](06-real-time-rendering/Q054.md) - `Advanced`
- [Q055 · Early-Z 什么时候可能失效或受限？](06-real-time-rendering/Q055.md) - `Advanced`
- [Q056 · Hi-Z / Hierarchical Z 是什么？](06-real-time-rendering/Q056.md) - `Advanced`
- [Q057 · Forward 和 Deferred Rendering 如何比较？](06-real-time-rendering/Q057.md) - `Intermediate`
- [Q058 · Forward+ / Clustered Rendering 为什么出现？](06-real-time-rendering/Q058.md) - `Advanced`
- [Q059 · 为什么 Deferred GBuffer 可以不保存 World Position？](06-real-time-rendering/Q059.md) - `Intermediate`
- [Q060 · Instancing 为什么能减少 Draw Call？](06-real-time-rendering/Q060.md) - `Intermediate`

## 7. [PBR、阴影、GI 与 Ray Tracing](07-pbr-ray-tracing/README.md)

- [Q061 · 写出 Rendering Equation，并解释每一项。](07-pbr-ray-tracing/Q061.md) - `Advanced`
- [Q062 · Cook-Torrance BRDF 怎么理解？](07-pbr-ray-tracing/Q062.md) - `Advanced`
- [Q063 · Metallic/Roughness PBR Workflow 是什么意思？](07-pbr-ray-tracing/Q063.md) - `Intermediate`
- [Q064 · Normal Map 为什么通常存在 Tangent Space？](07-pbr-ray-tracing/Q064.md) - `Intermediate`
- [Q065 · Shadow Mapping 原理是什么？](07-pbr-ray-tracing/Q065.md) - `Intermediate`
- [Q066 · Shadow Acne 和 Peter Panning 为什么出现？](07-pbr-ray-tracing/Q066.md) - `Intermediate`
- [Q067 · PCF 和 PCSS 有什么区别？](07-pbr-ray-tracing/Q067.md) - `Advanced`
- [Q068 · Path Tracing 为什么会有噪声？收敛速度如何理解？](07-pbr-ray-tracing/Q068.md) - `Advanced`
- [Q069 · 什么是 Importance Sampling？](07-pbr-ray-tracing/Q069.md) - `Advanced`
- [Q070 · BVH 在 Ray Tracing 中解决什么问题？](07-pbr-ray-tracing/Q070.md) - `Advanced`

## 8. [引擎架构与资源系统](08-engine-architecture/README.md)

- [Q071 · 如果从零设计游戏引擎，最核心模块有哪些？](08-engine-architecture/Q071.md) - `Advanced`
- [Q072 · Scene Graph 和 ECS 有什么关系？](08-engine-architecture/Q072.md) - `Intermediate`
- [Q073 · 游戏引擎 Serialization 系统如何设计？](08-engine-architecture/Q073.md) - `Advanced`
- [Q074 · Asset Pipeline 为什么不能直接运行时读取 FBX/PSD？](08-engine-architecture/Q074.md) - `Intermediate`
- [Q075 · 如何设计 Asset GUID？](08-engine-architecture/Q075.md) - `Intermediate`
- [Q076 · 什么是 Resource Streaming？](08-engine-architecture/Q076.md) - `Advanced`
- [Q077 · Game Thread、Render Thread、RHI Thread 如何交互？](08-engine-architecture/Q077.md) - `Advanced`
- [Q078 · 什么是 Render Graph？](08-engine-architecture/Q078.md) - `Advanced`
- [Q079 · 为什么 Shader Variant 会爆炸？如何控制？](08-engine-architecture/Q079.md) - `Advanced`
- [Q080 · 如何设计跨平台 RHI？](08-engine-architecture/Q080.md) - `Advanced`

## 9. [动画、物理、AI 与网络](09-simulation-networking/README.md)

- [Q081 · Skeletal Animation 如何工作？](09-simulation-networking/Q081.md) - `Intermediate`
- [Q082 · 为什么 Linear Blend Skinning 会出现 Candy Wrapper？](09-simulation-networking/Q082.md) - `Advanced`
- [Q083 · FK 与 IK 有什么区别？](09-simulation-networking/Q083.md) - `Intermediate`
- [Q084 · Animation State Machine 与 Blend Tree 分别解决什么？](09-simulation-networking/Q084.md) - `Intermediate`
- [Q085 · Physics Fixed Timestep 为什么重要？](09-simulation-networking/Q085.md) - `Advanced`
- [Q086 · Collision Detection 为什么分 Broad Phase 和 Narrow Phase？](09-simulation-networking/Q086.md) - `Intermediate`
- [Q087 · GJK 在解决什么问题？](09-simulation-networking/Q087.md) - `Advanced`
- [Q088 · NavMesh 为什么比规则 Grid 更适合 3D 游戏角色？](09-simulation-networking/Q088.md) - `Intermediate`
- [Q089 · Client Prediction 为什么需要 Server Reconciliation？](09-simulation-networking/Q089.md) - `Advanced`
- [Q090 · Lockstep 和 State Replication 如何选择？](09-simulation-networking/Q090.md) - `Advanced`

## 10. [GPU API、现代引擎与性能优化](10-gpu-api-performance/README.md)

- [Q091 · Vulkan 中 Fence、Semaphore、Barrier 分别解决什么？](10-gpu-api-performance/Q091.md) - `Advanced`
- [Q092 · 为什么 Pipeline Barrier 写得太保守会掉性能？](10-gpu-api-performance/Q092.md) - `Advanced`
- [Q093 · 什么是 Bindless Rendering？](10-gpu-api-performance/Q093.md) - `Advanced`
- [Q094 · GPU-Driven Rendering 是什么？](10-gpu-api-performance/Q094.md) - `Advanced`
- [Q095 · Compute Shader 可以在游戏引擎里做什么？](10-gpu-api-performance/Q095.md) - `Intermediate`
- [Q096 · 一帧只有 20 FPS，你如何定位问题？](10-gpu-api-performance/Q096.md) - `Advanced`
- [Q097 · 为什么移动 GPU 和桌面 GPU 优化思路不同？](10-gpu-api-performance/Q097.md) - `Advanced`
- [Q098 · Nanite 到底解决了什么问题？](10-gpu-api-performance/Q098.md) - `Advanced`
- [Q099 · Lumen 的设计目标是什么？](10-gpu-api-performance/Q099.md) - `Advanced`
- [Q100 · 系统设计：如何设计一个稳定 60 FPS 的开放世界引擎？](10-gpu-api-performance/Q100.md) - `Advanced`
