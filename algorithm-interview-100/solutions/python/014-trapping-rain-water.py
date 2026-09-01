from __future__ import annotations
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = ans = 0
        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                ans += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                ans += right_max - height[r]
                r -= 1
        return ans
