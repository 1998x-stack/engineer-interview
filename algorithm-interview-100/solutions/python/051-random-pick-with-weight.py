from __future__ import annotations
import bisect, random

class Solution:
    def __init__(self, w: list[int]):
        self.prefix=[]; total=0
        for x in w:
            total += x; self.prefix.append(total)
        self.total=total
    def pickIndex(self) -> int:
        ticket = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, ticket)
