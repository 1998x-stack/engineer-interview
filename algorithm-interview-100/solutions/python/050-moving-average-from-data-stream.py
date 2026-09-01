from __future__ import annotations
from collections import deque

class MovingAverage:
    def __init__(self, size: int): self.size=size; self.q=deque(); self.total=0
    def next(self, val: int) -> float:
        self.q.append(val); self.total += val
        if len(self.q) > self.size: self.total -= self.q.popleft()
        return self.total / len(self.q)
