from __future__ import annotations
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in pos:
                return [pos[need], i]
            pos[x] = i
        return []
