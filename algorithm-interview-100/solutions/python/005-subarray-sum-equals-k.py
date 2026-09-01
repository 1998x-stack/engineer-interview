from __future__ import annotations
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix = ans = 0
        for x in nums:
            prefix += x
            ans += freq[prefix - k]
            freq[prefix] += 1
        return ans
