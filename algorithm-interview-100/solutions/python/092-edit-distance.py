from __future__ import annotations
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev=list(range(len(word2)+1))
        for i,a in enumerate(word1,1):
            cur=[i]+[0]*len(word2)
            for j,b in enumerate(word2,1):
                if a==b: cur[j]=prev[j-1]
                else: cur[j]=1+min(prev[j],cur[j-1],prev[j-1])
            prev=cur
        return prev[-1]
