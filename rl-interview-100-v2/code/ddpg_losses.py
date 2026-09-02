"""DDPG actor/critic loss skeleton."""
import torch
import torch.nn.functional as F

def critic_loss(actor_t, critic, critic_t, batch, gamma=0.99):
    s,a,r,s2,done=batch
    with torch.no_grad():
        a2=actor_t(s2); y=r+gamma*(1-done.float())*critic_t(s2,a2)
    return F.mse_loss(critic(s,a),y)

def actor_loss(actor,critic,s):
    return -critic(s,actor(s)).mean()
