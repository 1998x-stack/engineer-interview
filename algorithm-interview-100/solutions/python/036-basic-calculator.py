from __future__ import annotations
class Solution:
    def calculate(self, s: str) -> int:
        ans = num = 0; sign = 1; stack = []
        for ch in s + '+':
            if ch.isdigit(): num = num*10 + int(ch)
            elif ch in '+-':
                ans += sign*num; num = 0; sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append((ans, sign)); ans = 0; sign = 1
            elif ch == ')':
                ans += sign*num; num = 0
                prev, outer_sign = stack.pop(); ans = prev + outer_sign*ans
        return ans
