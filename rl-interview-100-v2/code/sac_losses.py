"""SAC loss skeleton for a tanh-squashed stochastic actor."""
import torch
import torch.nn.functional as F

def critic_target(actor,q1_t,q2_t,s2,r,done,alpha,gamma=0.99):
    with torch.no_grad():
        a2,logp2=actor.sample(s2)
        q2=torch.minimum(q1_t(s2,a2),q2_t(s2,a2)) - alpha*logp2
        return r+gamma*(1-done.float())*q2

def actor_loss(actor,q1,q2,s,alpha):
    a,logp=actor.sample(s)
    q=torch.minimum(q1(s,a),q2(s,a))
    return (alpha*logp-q).mean()
