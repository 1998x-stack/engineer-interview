"""GRPO core: group advantage + token-level PPO-style clipped loss.
Inputs rewards:[B,G], logp:[B,G,T], mask:[B,G,T].
"""
import torch

def group_advantage(rewards,eps=1e-6):
    mean=rewards.mean(dim=1,keepdim=True)
    std=rewards.std(dim=1,keepdim=True,unbiased=False)
    return (rewards-mean)/(std+eps)

def grpo_loss(new_logp,old_logp,rewards,mask,clip_low=0.2,clip_high=0.2):
    adv=group_advantage(rewards).unsqueeze(-1)
    ratio=torch.exp(new_logp-old_logp)
    unclipped=ratio*adv
    clipped=torch.clamp(ratio,1-clip_low,1+clip_high)*adv
    token_obj=torch.minimum(unclipped,clipped)
    return -(token_obj*mask).sum()/mask.sum().clamp_min(1)
