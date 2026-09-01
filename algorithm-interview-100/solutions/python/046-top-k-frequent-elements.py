from __future__ import annotations
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums); buckets = [[] for _ in range(len(nums)+1)]
        for x, f in count.items(): buckets[f].append(x)
        ans = []
        for f in range(len(buckets)-1, 0, -1):
            for x in buckets[f]:
                ans.append(x)
                if len(ans) == k: return ans
        return ans
