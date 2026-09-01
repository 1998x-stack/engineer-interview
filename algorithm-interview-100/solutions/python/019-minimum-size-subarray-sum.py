from __future__ import annotations
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = total = 0; ans = len(nums) + 1
        for right, x in enumerate(nums):
            total += x
            while total >= target:
                ans = min(ans, right-left+1)
                total -= nums[left]; left += 1
        return 0 if ans == len(nums)+1 else ans
