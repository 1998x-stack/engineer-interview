from __future__ import annotations
class MinStack:
    def __init__(self): self.stack = []
    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))
    def pop(self) -> None: self.stack.pop()
    def top(self) -> int: return self.stack[-1][0]
    def getMin(self) -> int: return self.stack[-1][1]
