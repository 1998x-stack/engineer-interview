# PDF Source Map

该文件用于把拆分后的 Markdown 精确映射回仓库附带 PDF。`物理页`指 PDF 文件从封面开始计数的页码。

| Q | 标题 | PDF 物理页 | 来源口径 | refs |
|---|---|---:|---|---|
| [Q001](questions/01-cpp-object-model/Q001.md) | C++ 虚函数和运行时多态到底是怎么实现的？ | 10 | 公开面经/官方资料可核验 | M2, M5 |
| [Q002](questions/01-cpp-object-model/Q002.md) | 为什么基类析构函数经常必须是 virtual？ | 11 | 高频能力重构 | - |
| [Q003](questions/01-cpp-object-model/Q003.md) | 为什么构造函数不能是 virtual？构造期间调用 virtual function 会怎样？ | 12 | 公开面经/官方资料可核验 | M2 |
| [Q004](questions/01-cpp-object-model/Q004.md) | unique_ptr、shared_ptr、weak_ptr 底层有什么区别？ | 13 | 公开面经/官方资料可核验 | M2, M3, M5 |
| [Q005](questions/01-cpp-object-model/Q005.md) | shared_ptr 为什么会发生循环引用？如何从设计上避免？ | 14 | 公开面经/官方资料可核验 | M3 |
| [Q006](questions/01-cpp-object-model/Q006.md) | 左值、右值、std::move、移动构造究竟解决什么问题？ | 15 | 高频能力重构 | - |
| [Q007](questions/01-cpp-object-model/Q007.md) | std::vector 扩容时发生了什么？哪些引用会失效？ | 16 | 公开面经/官方资料可核验 | M2 |
| [Q008](questions/01-cpp-object-model/Q008.md) | vector 为什么常常比 list 更快，即使 list 插入是 O(1)？ | 17 | 公开面经/官方资料可核验 | M2 |
| [Q009](questions/01-cpp-object-model/Q009.md) | new/delete 与 malloc/free 有什么区别？为什么不能混用？ | 18 | 公开面经/官方资料可核验 | M2 |
| [Q010](questions/01-cpp-object-model/Q010.md) | C++ Reflection 为什么难？游戏引擎如何实现反射？ | 19 | 公开面经/官方资料可核验 | M1 |
| [Q011](questions/02-memory-data-oriented/Q011.md) | 游戏引擎为什么特别在意内存对齐？ | 21 | 公开面经/官方资料可核验 | M2, M3 |
| [Q012](questions/02-memory-data-oriented/Q012.md) | Stack 和 Heap 的区别是什么？实时引擎如何选择？ | 22 | 高频能力重构 | - |
| [Q013](questions/02-memory-data-oriented/Q013.md) | 如何设计一个固定大小 Memory Pool？ | 23 | 高频能力重构 | - |
| [Q014](questions/02-memory-data-oriented/Q014.md) | Arena / Linear Allocator 为什么适合每帧临时对象？ | 24 | 高频能力重构 | - |
| [Q015](questions/02-memory-data-oriented/Q015.md) | AoS 和 SoA 有什么区别？为什么 SoA 常用于热点系统？ | 25 | 高频能力重构 | - |
| [Q016](questions/02-memory-data-oriented/Q016.md) | ECS 为什么越来越常见？它解决了什么，又带来什么成本？ | 26 | 高频能力重构 | - |
| [Q017](questions/02-memory-data-oriented/Q017.md) | Hash Map 和红黑树怎么选？ | 27 | 公开面经/官方资料可核验 | M5 |
| [Q018](questions/02-memory-data-oriented/Q018.md) | Object Pool 适合什么场景？如何避免把它用成“内存垃圾场”？ | 28 | 高频能力重构 | - |
| [Q019](questions/02-memory-data-oriented/Q019.md) | 什么是 Cache Miss？为什么游戏引擎比普通业务代码更在意？ | 29 | 公开面经/官方资料可核验 | M3 |
| [Q020](questions/02-memory-data-oriented/Q020.md) | 什么是 False Sharing？如何定位与修复？ | 30 | 高频能力重构 | - |
| [Q021](questions/03-os-concurrency/Q021.md) | Process 与 Thread 的区别是什么？ | 32 | 公开面经/官方资料可核验 | M2, M3 |
| [Q022](questions/03-os-concurrency/Q022.md) | Context Switch 为什么贵？ | 33 | 公开面经/官方资料可核验 | M2 |
| [Q023](questions/03-os-concurrency/Q023.md) | 什么是 Job System？为什么比“一个子系统一个线程”更可扩展？ | 34 | 公开面经/官方资料可核验 | O1 |
| [Q024](questions/03-os-concurrency/Q024.md) | Mutex、Spinlock、Semaphore 怎么选？ | 35 | 高频能力重构 | - |
| [Q025](questions/03-os-concurrency/Q025.md) | 什么是 Deadlock？四个必要条件是什么？ | 36 | 高频能力重构 | - |
| [Q026](questions/03-os-concurrency/Q026.md) | 如何实现一个 SPSC 无锁环形队列？ | 37 | 高频能力重构 | - |
| [Q027](questions/03-os-concurrency/Q027.md) | memory_order_relaxed / acquire / release 是什么？ | 38 | 高频能力重构 | - |
| [Q028](questions/03-os-concurrency/Q028.md) | 虚拟地址如何转换成物理地址？Page Fault 发生了什么？ | 39 | 公开面经/官方资料可核验 | M3 |
| [Q029](questions/03-os-concurrency/Q029.md) | Game Thread 和 Render Thread 为什么要分开？ | 40 | 公开面经/官方资料可核验 | O2, O3 |
| [Q030](questions/03-os-concurrency/Q030.md) | Triple Buffering 与 Frames in Flight 有什么作用？ | 41 | 公开面经/官方资料可核验 | O3 |
| [Q031](questions/04-algorithms/Q031.md) | 10 万个数找最大的 1 万个，怎么做？ | 43 | 高频能力重构 | - |
| [Q032](questions/04-algorithms/Q032.md) | 实现 A*，为什么它比 Dijkstra 更适合游戏寻路？ | 44 | 高频能力重构 | - |
| [Q033](questions/04-algorithms/Q033.md) | A* 在开放世界地图里为什么仍可能很慢？ | 45 | 高频能力重构 | - |
| [Q034](questions/04-algorithms/Q034.md) | Bresenham 画线算法为什么能避免浮点数？ | 46 | 高频能力重构 | - |
| [Q035](questions/04-algorithms/Q035.md) | 二叉树最近公共祖先怎么做？ | 47 | 高频能力重构 | - |
| [Q036](questions/04-algorithms/Q036.md) | 最长合法括号如何做到 O(N)？ | 48 | 高频能力重构 | - |
| [Q037](questions/04-algorithms/Q037.md) | 所有节点出度 1，如何寻找最长环？ | 49 | 公开面经/官方资料可核验 | M3 |
| [Q038](questions/04-algorithms/Q038.md) | 如何设计空间哈希解决大量对象邻域查询？ | 50 | 高频能力重构 | - |
| [Q039](questions/04-algorithms/Q039.md) | Quadtree、Octree、BVH 有什么区别？ | 51 | 公开面经/官方资料可核验 | M5 |
| [Q040](questions/04-algorithms/Q040.md) | 动态对象很多时 BVH 怎么更新？ | 52 | 公开面经/官方资料可核验 | M2, M5 |
| [Q041](questions/05-3d-math/Q041.md) | 游戏渲染中有哪些坐标空间？ | 54 | 高频能力重构 | - |
| [Q042](questions/05-3d-math/Q042.md) | 齐次坐标为什么需要第四维？ | 55 | 高频能力重构 | - |
| [Q043](questions/05-3d-math/Q043.md) | 为什么 Normal 不能直接乘 Model Matrix？ | 56 | 高频能力重构 | - |
| [Q044](questions/05-3d-math/Q044.md) | Quaternion 为什么适合表示旋转？ | 57 | 高频能力重构 | - |
| [Q045](questions/05-3d-math/Q045.md) | SLERP 和 LERP 有什么区别？ | 58 | 高频能力重构 | - |
| [Q046](questions/05-3d-math/Q046.md) | 如何判断一个点/包围体是否在视锥体中？ | 59 | 高频能力重构 | - |
| [Q047](questions/05-3d-math/Q047.md) | Ray 与 Triangle 如何求交？ | 60 | 高频能力重构 | - |
| [Q048](questions/05-3d-math/Q048.md) | AABB 和 OBB 的区别？ | 61 | 高频能力重构 | - |
| [Q049](questions/05-3d-math/Q049.md) | 什么是重心坐标？ | 62 | 高频能力重构 | - |
| [Q050](questions/05-3d-math/Q050.md) | 为什么纹理属性必须做透视矫正插值？ | 63 | 公开面经/官方资料可核验 | M3 |
| [Q051](questions/06-real-time-rendering/Q051.md) | 请完整讲一遍现代 GPU Rasterization Pipeline。 | 65 | 公开面经/官方资料可核验 | M1, M2, M3, M5 |
| [Q052](questions/06-real-time-rendering/Q052.md) | Rasterization 本质上在做什么？ | 66 | 高频能力重构 | - |
| [Q053](questions/06-real-time-rendering/Q053.md) | Vertex Shader 与 Fragment Shader 谁调用次数更多？ | 67 | 高频能力重构 | - |
| [Q054](questions/06-real-time-rendering/Q054.md) | 什么是 Early-Z？它为什么能加速？ | 68 | 公开面经/官方资料可核验 | M2, M4, M6 |
| [Q055](questions/06-real-time-rendering/Q055.md) | Early-Z 什么时候可能失效或受限？ | 69 | 公开面经/官方资料可核验 | M4, M6 |
| [Q056](questions/06-real-time-rendering/Q056.md) | Hi-Z / Hierarchical Z 是什么？ | 70 | 公开面经/官方资料可核验 | M2 |
| [Q057](questions/06-real-time-rendering/Q057.md) | Forward 和 Deferred Rendering 如何比较？ | 71 | 公开面经/官方资料可核验 | M1, M6 |
| [Q058](questions/06-real-time-rendering/Q058.md) | Forward+ / Clustered Rendering 为什么出现？ | 72 | 高频能力重构 | - |
| [Q059](questions/06-real-time-rendering/Q059.md) | 为什么 Deferred GBuffer 可以不保存 World Position？ | 73 | 公开面经/官方资料可核验 | M6 |
| [Q060](questions/06-real-time-rendering/Q060.md) | Instancing 为什么能减少 Draw Call？ | 74 | 高频能力重构 | - |
| [Q061](questions/07-pbr-ray-tracing/Q061.md) | 写出 Rendering Equation，并解释每一项。 | 76 | 公开面经/官方资料可核验 | M4 |
| [Q062](questions/07-pbr-ray-tracing/Q062.md) | Cook-Torrance BRDF 怎么理解？ | 77 | 公开面经/官方资料可核验 | M1, M2, M3 |
| [Q063](questions/07-pbr-ray-tracing/Q063.md) | Metallic/Roughness PBR Workflow 是什么意思？ | 78 | 公开面经/官方资料可核验 | M2 |
| [Q064](questions/07-pbr-ray-tracing/Q064.md) | Normal Map 为什么通常存在 Tangent Space？ | 79 | 公开面经/官方资料可核验 | M2, M3 |
| [Q065](questions/07-pbr-ray-tracing/Q065.md) | Shadow Mapping 原理是什么？ | 80 | 公开面经/官方资料可核验 | M1, M2, M6 |
| [Q066](questions/07-pbr-ray-tracing/Q066.md) | Shadow Acne 和 Peter Panning 为什么出现？ | 81 | 公开面经/官方资料可核验 | M1 |
| [Q067](questions/07-pbr-ray-tracing/Q067.md) | PCF 和 PCSS 有什么区别？ | 82 | 公开面经/官方资料可核验 | M6 |
| [Q068](questions/07-pbr-ray-tracing/Q068.md) | Path Tracing 为什么会有噪声？收敛速度如何理解？ | 83 | 公开面经/官方资料可核验 | M4 |
| [Q069](questions/07-pbr-ray-tracing/Q069.md) | 什么是 Importance Sampling？ | 84 | 公开面经/官方资料可核验 | M4 |
| [Q070](questions/07-pbr-ray-tracing/Q070.md) | BVH 在 Ray Tracing 中解决什么问题？ | 85 | 公开面经/官方资料可核验 | M2, M5 |
| [Q071](questions/08-engine-architecture/Q071.md) | 如果从零设计游戏引擎，最核心模块有哪些？ | 87 | 公开面经/官方资料可核验 | M1, O1 |
| [Q072](questions/08-engine-architecture/Q072.md) | Scene Graph 和 ECS 有什么关系？ | 88 | 高频能力重构 | - |
| [Q073](questions/08-engine-architecture/Q073.md) | 游戏引擎 Serialization 系统如何设计？ | 89 | 公开面经/官方资料可核验 | M1 |
| [Q074](questions/08-engine-architecture/Q074.md) | Asset Pipeline 为什么不能直接运行时读取 FBX/PSD？ | 90 | 高频能力重构 | - |
| [Q075](questions/08-engine-architecture/Q075.md) | 如何设计 Asset GUID？ | 91 | 高频能力重构 | - |
| [Q076](questions/08-engine-architecture/Q076.md) | 什么是 Resource Streaming？ | 92 | 公开面经/官方资料可核验 | O4 |
| [Q077](questions/08-engine-architecture/Q077.md) | Game Thread、Render Thread、RHI Thread 如何交互？ | 93 | 公开面经/官方资料可核验 | O2, O3 |
| [Q078](questions/08-engine-architecture/Q078.md) | 什么是 Render Graph？ | 94 | 公开面经/官方资料可核验 | O3 |
| [Q079](questions/08-engine-architecture/Q079.md) | 为什么 Shader Variant 会爆炸？如何控制？ | 95 | 高频能力重构 | - |
| [Q080](questions/08-engine-architecture/Q080.md) | 如何设计跨平台 RHI？ | 96 | 公开面经/官方资料可核验 | M1, O3 |
| [Q081](questions/09-simulation-networking/Q081.md) | Skeletal Animation 如何工作？ | 98 | 高频能力重构 | - |
| [Q082](questions/09-simulation-networking/Q082.md) | 为什么 Linear Blend Skinning 会出现 Candy Wrapper？ | 99 | 高频能力重构 | - |
| [Q083](questions/09-simulation-networking/Q083.md) | FK 与 IK 有什么区别？ | 100 | 高频能力重构 | - |
| [Q084](questions/09-simulation-networking/Q084.md) | Animation State Machine 与 Blend Tree 分别解决什么？ | 101 | 高频能力重构 | - |
| [Q085](questions/09-simulation-networking/Q085.md) | Physics Fixed Timestep 为什么重要？ | 102 | 高频能力重构 | - |
| [Q086](questions/09-simulation-networking/Q086.md) | Collision Detection 为什么分 Broad Phase 和 Narrow Phase？ | 103 | 高频能力重构 | - |
| [Q087](questions/09-simulation-networking/Q087.md) | GJK 在解决什么问题？ | 104 | 高频能力重构 | - |
| [Q088](questions/09-simulation-networking/Q088.md) | NavMesh 为什么比规则 Grid 更适合 3D 游戏角色？ | 105 | 高频能力重构 | - |
| [Q089](questions/09-simulation-networking/Q089.md) | Client Prediction 为什么需要 Server Reconciliation？ | 106 | 高频能力重构 | - |
| [Q090](questions/09-simulation-networking/Q090.md) | Lockstep 和 State Replication 如何选择？ | 107 | 高频能力重构 | - |
| [Q091](questions/10-gpu-api-performance/Q091.md) | Vulkan 中 Fence、Semaphore、Barrier 分别解决什么？ | 109 | 公开面经/官方资料可核验 | O6 |
| [Q092](questions/10-gpu-api-performance/Q092.md) | 为什么 Pipeline Barrier 写得太保守会掉性能？ | 110 | 公开面经/官方资料可核验 | O6, O7 |
| [Q093](questions/10-gpu-api-performance/Q093.md) | 什么是 Bindless Rendering？ | 111 | 公开面经/官方资料可核验 | M3 |
| [Q094](questions/10-gpu-api-performance/Q094.md) | GPU-Driven Rendering 是什么？ | 112 | 高频能力重构 | - |
| [Q095](questions/10-gpu-api-performance/Q095.md) | Compute Shader 可以在游戏引擎里做什么？ | 113 | 公开面经/官方资料可核验 | M1 |
| [Q096](questions/10-gpu-api-performance/Q096.md) | 一帧只有 20 FPS，你如何定位问题？ | 114 | 公开面经/官方资料可核验 | M2, O7 |
| [Q097](questions/10-gpu-api-performance/Q097.md) | 为什么移动 GPU 和桌面 GPU 优化思路不同？ | 115 | 公开面经/官方资料可核验 | M2, M6 |
| [Q098](questions/10-gpu-api-performance/Q098.md) | Nanite 到底解决了什么问题？ | 116 | 公开面经/官方资料可核验 | O4 |
| [Q099](questions/10-gpu-api-performance/Q099.md) | Lumen 的设计目标是什么？ | 117 | 公开面经/官方资料可核验 | O5 |
| [Q100](questions/10-gpu-api-performance/Q100.md) | 系统设计：如何设计一个稳定 60 FPS 的开放世界引擎？ | 118 | 公开面经/官方资料可核验 | O1, O2, O3, O4, O5, O7 |