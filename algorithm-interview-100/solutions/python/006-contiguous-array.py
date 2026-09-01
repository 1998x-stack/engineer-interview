from __future__ import annotations
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        first = {0: -1}
        balance = ans = 0
        for i, x in enumerate(nums):
            balance += 1 if x == 1 else -1
            if balance in first:
                ans = max(ans, i - first[balance])
            else:
                first[balance] = i
        return ans
