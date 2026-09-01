from __future__ import annotations
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort(); ans = []
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        return ans
