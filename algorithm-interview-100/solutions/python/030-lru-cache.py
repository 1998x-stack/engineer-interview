from __future__ import annotations
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity; self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next = self.right; self.right.prev = self.left

    def _remove(self, node):
        node.prev.next = node.next; node.next.prev = node.prev

    def _append(self, node):
        prev = self.right.prev
        prev.next = node; node.prev = prev
        node.next = self.right; self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]; self._remove(node); self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value); self.cache[key] = node; self._append(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next; self._remove(lru); del self.cache[lru.key]
