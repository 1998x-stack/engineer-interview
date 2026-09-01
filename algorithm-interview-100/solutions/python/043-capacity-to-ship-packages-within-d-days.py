from __future__ import annotations
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def feasible(cap):
            used = 1; cur = 0
            for w in weights:
                if cur + w > cap: used += 1; cur = 0
                cur += w
            return used <= days
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l+r)//2
            if feasible(m): r = m
            else: l = m+1
        return l
