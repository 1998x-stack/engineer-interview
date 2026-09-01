from __future__ import annotations
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i, x in enumerate(nums):
            ans[i] = prefix
            prefix *= x
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans
