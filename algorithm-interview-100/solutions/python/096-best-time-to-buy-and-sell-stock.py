from __future__ import annotations
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=float('inf'); ans=0
        for p in prices:
            min_price=min(min_price,p); ans=max(ans,p-min_price)
        return ans
