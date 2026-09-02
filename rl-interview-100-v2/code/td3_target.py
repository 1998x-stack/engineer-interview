"""TD3 target: clipped double Q + target policy smoothing."""
import torch

def td3_target(actor_t,q1_t,q2_t,s2,r,done,gamma=0.99,sigma=0.2,noise_clip=0.5,action_low=-1.,action_high=1.):
    with torch.no_grad():
        noise=(torch.randn_like(actor_t(s2))*sigma).clamp(-noise_clip,noise_clip)
        a2=(actor_t(s2)+noise).clamp(action_low,action_high)
        q=torch.minimum(q1_t(s2,a2),q2_t(s2,a2))
        return r+gamma*(1-done.float())*q
