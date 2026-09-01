from __future__ import annotations
import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos: return False
        self.pos[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos: return False
        i = self.pos[val]
        last = self.values[-1]
        self.values[i] = last
        self.pos[last] = i
        self.values.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
