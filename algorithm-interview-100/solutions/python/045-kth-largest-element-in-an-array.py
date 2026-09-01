from __future__ import annotations
import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums)-k
        l, r = 0, len(nums)-1
        while True:
            pivot_i = random.randint(l, r)
            nums[pivot_i], nums[r] = nums[r], nums[pivot_i]
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]; p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == target: return nums[p]
            if p < target: l = p+1
            else: r = p-1
