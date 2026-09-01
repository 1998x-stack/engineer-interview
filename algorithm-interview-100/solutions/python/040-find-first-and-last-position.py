from __future__ import annotations
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower(x):
            l, r = 0, len(nums)
            while l < r:
                m = (l+r)//2
                if nums[m] < x: l = m+1
                else: r = m
            return l
        left = lower(target); right = lower(target+1)-1
        if left == len(nums) or nums[left] != target: return [-1,-1]
        return [left, right]
