from __future__ import annotations
class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', ']':'[', '}':'{'}; stack = []
        for ch in s:
            if ch in match:
                if not stack or stack.pop() != match[ch]: return False
            else: stack.append(ch)
        return not stack
