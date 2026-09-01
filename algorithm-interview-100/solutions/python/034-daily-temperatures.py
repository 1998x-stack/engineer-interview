from __future__ import annotations
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures); stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop(); ans[j] = i-j
            stack.append(i)
        return ans
