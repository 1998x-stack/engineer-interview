"""Bradley-Terry pairwise reward-model loss."""
import torch.nn.functional as F

def preference_loss(reward_chosen,reward_rejected):
    return -F.logsigmoid(reward_chosen-reward_rejected).mean()
