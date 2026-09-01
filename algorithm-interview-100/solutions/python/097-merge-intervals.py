from __future__ import annotations
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0]); ans=[]
        for s,e in intervals:
            if not ans or s>ans[-1][1]: ans.append([s,e])
            else: ans[-1][1]=max(ans[-1][1],e)
        return ans
