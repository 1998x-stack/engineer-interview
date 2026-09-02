"""Minimal DPO loss from sequence log-probabilities."""
import torch
import torch.nn.functional as F

def dpo_loss(pi_w,pi_l,ref_w,ref_l,beta=0.1):
    logits=beta*((pi_w-ref_w)-(pi_l-ref_l))
    return -F.logsigmoid(logits).mean()
