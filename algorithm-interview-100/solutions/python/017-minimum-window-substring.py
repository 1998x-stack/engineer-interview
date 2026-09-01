from __future__ import annotations
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ''
        need = Counter(t); have = defaultdict(int)
        required = len(need); formed = 0; left = 0
        best = (float('inf'), -1, -1)
        for right, ch in enumerate(s):
            have[ch] += 1
            if ch in need and have[ch] == need[ch]: formed += 1
            while formed == required:
                if right - left + 1 < best[0]: best = (right-left+1, left, right)
                c = s[left]; have[c] -= 1; left += 1
                if c in need and have[c] < need[c]: formed -= 1
        return '' if best[0] == float('inf') else s[best[1]:best[2]+1]
