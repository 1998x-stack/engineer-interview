"""Educational reference implementation used by the Markdown questions.
Not intended to replace framework fused SDPA/FlashAttention in production.
"""
import math
import torch
import torch.nn as nn

class ReferenceMHA(nn.Module):
    def __init__(self,d_model:int,num_heads:int):
        super().__init__(); assert d_model%num_heads==0
        self.h=num_heads; self.dh=d_model//num_heads
        self.qkv=nn.Linear(d_model,3*d_model,bias=False)
        self.out=nn.Linear(d_model,d_model,bias=False)
    def forward(self,x,mask=None):
        B,T,D=x.shape
        q,k,v=self.qkv(x).chunk(3,-1)
        def split(z):return z.view(B,T,self.h,self.dh).transpose(1,2)
        q,k,v=map(split,(q,k,v))
        s=q@k.transpose(-2,-1)/math.sqrt(self.dh)
        if mask is not None:s=s.masked_fill(~mask,float('-inf'))
        p=torch.softmax(s,-1)
        y=p@v
        y=y.transpose(1,2).contiguous().view(B,T,D)
        return self.out(y)

def causal_mask(T:int,device=None):
    return torch.ones(T,T,dtype=torch.bool,device=device).tril()[None,None]
