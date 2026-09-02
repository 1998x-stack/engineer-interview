from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))

EXPERIMENT={
'01-foundations':('构造一个 3~5 状态的 tabular MDP，手工给定转移和奖励。', '用枚举/矩阵解作为 ground truth，再比较 MC/TD/DP 或对应公式的数值结果。', '目标不是跑出高分，而是验证公式、terminal 处理和期望的维度是否正确。'),
'02-value-based':('选择 CartPole/小型 GridWorld，固定随机种子并记录 replay 中的 transition。', '对 target、TD error、online/target Q、buffer age 做可视化；针对本题只改一个组件做 ablation。', '预期结果应能解释该组件解决的 failure mode，而不是只比较最终 return。'),
'03-policy-gradient-ppo':('先用一个离散两动作 toy policy 手工设 old/new logits 与 advantage，再运行一批 PPO 数值测试。', '打印 new/old logp、ratio、clipped ratio、sample objective、KL、entropy；再在小环境跑完整训练。', '先验证分段目标和梯度方向，再谈大规模训练稳定性。'),
'04-continuous-control':('在 Pendulum 或自定义一维连续控制环境建立小实验。', '记录 action distribution、Q1/Q2、target Q、actor output、entropy/temperature（若适用）以及 replay age。', '重点验证连续动作优化、Q 偏差与探索机制，而不是追求 benchmark 最优分。'),
'05-offline-model-marl-robotics':('构造可控的数据覆盖差异：例如只收集某一部分 action/state 的静态 dataset。', '比较 BC、普通 off-policy 方法与本题算法在 in-distribution / OOD action 上的 Q、动作分布与 return。', '让 distribution shift、conservatism 或 model bias 变成可观测现象。'),
'06-llm-post-training-rl':('用少量 prompt，每个 prompt 采 G 个短 completion，并使用可重复的 toy verifier/reward。', '保存 prompt/response mask、old/ref/new logp、group reward、advantage、ratio、KL、entropy、length。', '先在极小 batch 上逐元素核对 loss，再扩到真实 rollout；这能捕获绝大多数 silent bug。'),
'07-debug-infra-system-design':('构造一个故意注入故障的最小 pipeline：错误 mask、极端长度、stale policy 或错误 reward parser。', '观察指标联动，并验证监控能否在最终 reward 明显下降前发现异常。', '系统题的“实验”应证明可观测性、背压、版本一致性与故障恢复设计有效。'),
}

for q in DATA:
    p=ROOT/q['path']; t=p.read_text(encoding='utf-8')
    t=re.sub(r'\n## 12\. 90 秒专业回答.*?(?=\n## 13\.)','',t,flags=re.S)
    t=re.sub(r'\n## 13\. 最小可验证实验.*?(?=\n---\n)','',t,flags=re.S)
    ch=q['chapter_slug']; exp=EXPERIMENT[ch]
    deep='；'.join(q.get('deep',[])[:2])
    block=f'''\n## 12. 90 秒专业回答\n\n> **结论先行**：{q['quick']}\n\n继续展开时，先把它放回本章的统一问题框架：**{deep or q['title']}**。随后写出本题最关键的数学对象：`{q.get('formula') or '见上文推导'}`。最后必须补一句工程判断：公式成立不代表实现健康，需要用本页列出的分布指标、边界条件和 failure mode 验证。\n\n一个高质量的 90 秒回答应满足：\n\n- **前 15 秒**：明确“这个方法解决什么问题”；\n- **15–45 秒**：给核心公式，并解释符号来自哪个数据分布；\n- **45–70 秒**：讲一个典型失败模式或 tradeoff；\n- **70–90 秒**：落到实现/日志，并说明如何验证。\n\n> **不要这样答**：只按论文顺序背名词。面试官通常更在意你能否从 failure mode 推回设计，再从设计推到可观测指标。\n\n## 13. 最小可验证实验\n\n**实验目标**：不是做 leaderboard，而是把本题的核心机制变成可以 falsify 的小实验。\n\n1. **环境/数据**：{exp[0]}\n2. **记录与对照**：{exp[1]}\n3. **验收标准**：{exp[2]}\n\n针对本题额外要求：把 **“{q['title']}”** 对应的关键变量单独画分布或写断言；如果实验结果和理论预期相反，优先检查数据定义、mask/terminal、旧策略版本和归一化维度，再讨论超参数。\n'''
    idx=t.rfind('\n---\n')
    if idx<0: raise RuntimeError(p)
    t=t[:idx]+block+t[idx:]
    p.write_text(t,encoding='utf-8')
print('added blocks',len(DATA))
