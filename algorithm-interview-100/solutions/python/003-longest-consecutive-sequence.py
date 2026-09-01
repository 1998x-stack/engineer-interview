from __future__ import annotations
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        best = 0
        for x in values:
            if x - 1 in values:
                continue
            y = x
            while y in values:
                y += 1
            best = max(best, y - x)
        return best
