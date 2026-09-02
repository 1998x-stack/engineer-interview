"""GAE + PPO clipped loss skeleton. Shapes are [B,T] for scalar token/step values."""
import torch

def gae(reward, value, next_value, done, gamma=0.99, lam=0.95):
    adv = torch.zeros_like(reward)
    last = torch.zeros_like(reward[:,0])
    for t in reversed(range(reward.size(1))):
        nv = next_value[:,t] if t == reward.size(1)-1 else value[:,t+1]
        nonterminal = 1.0 - done[:,t].float()
        delta = reward[:,t] + gamma*nonterminal*nv - value[:,t]
        last = delta + gamma*lam*nonterminal*last
        adv[:,t] = last
    return adv

def ppo_policy_loss(new_logp, old_logp, adv, eps=0.2):
    ratio = torch.exp(new_logp-old_logp)
    s1 = ratio*adv
    s2 = torch.clamp(ratio,1-eps,1+eps)*adv
    return -torch.minimum(s1,s2).mean()
