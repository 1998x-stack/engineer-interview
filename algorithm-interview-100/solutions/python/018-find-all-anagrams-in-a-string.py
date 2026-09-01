from __future__ import annotations
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s): return []
        need = Counter(p); window = Counter(s[:len(p)])
        ans = [0] if window == need else []
        for r in range(len(p), len(s)):
            window[s[r]] += 1
            left_ch = s[r-len(p)]
            window[left_ch] -= 1
            if window[left_ch] == 0: del window[left_ch]
            if window == need: ans.append(r-len(p)+1)
        return ans
