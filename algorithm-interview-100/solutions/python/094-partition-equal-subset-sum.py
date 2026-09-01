from __future__ import annotations
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total=sum(nums)
        if total%2: return False
        target=total//2; possible={0}
        for x in nums:
            possible |= {s+x for s in possible if s+x<=target}
            if target in possible: return True
        return False
