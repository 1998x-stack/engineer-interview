from __future__ import annotations
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] <= height[r]: l += 1
            else: r -= 1
        return ans
