from __future__ import annotations
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2=prev1=0
        for x in nums: prev2,prev1=prev1,max(prev1,prev2+x)
        return prev1
