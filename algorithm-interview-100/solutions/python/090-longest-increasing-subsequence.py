from __future__ import annotations
import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails=[]
        for x in nums:
            i=bisect.bisect_left(tails,x)
            if i==len(tails): tails.append(x)
            else: tails[i]=x
        return len(tails)
