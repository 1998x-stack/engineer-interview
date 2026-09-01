from __future__ import annotations
class TrieNode:
    def __init__(self): self.children={}; self.end=False

class Trie:
    def __init__(self): self.root=TrieNode()
    def insert(self, word: str) -> None:
        node=self.root
        for ch in word: node=node.children.setdefault(ch,TrieNode())
        node.end=True
    def search(self, word: str) -> bool:
        node=self._walk(word); return bool(node and node.end)
    def startsWith(self, prefix: str) -> bool: return self._walk(prefix) is not None
    def _walk(self, s):
        node=self.root
        for ch in s:
            if ch not in node.children: return None
            node=node.children[ch]
        return node
