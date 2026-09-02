"""Minimal DQN loss skeleton for interview practice."""
import torch
import torch.nn.functional as F

def dqn_loss(q_net, target_net, batch, gamma=0.99):
    s,a,r,s2,terminated = batch
    q = q_net(s).gather(-1, a.long().unsqueeze(-1)).squeeze(-1)
    with torch.no_grad():
        next_q = target_net(s2).max(dim=-1).values
        y = r + gamma * (1.0-terminated.float()) * next_q
    return F.smooth_l1_loss(q, y)
