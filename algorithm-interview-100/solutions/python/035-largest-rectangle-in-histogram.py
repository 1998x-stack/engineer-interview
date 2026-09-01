from __future__ import annotations
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []; ans = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop(); ans = max(ans, height*(i-idx)); start = idx
            stack.append((start, h))
        return ans
