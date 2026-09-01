from __future__ import annotations
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words=set(wordDict); max_len=max(map(len,words), default=0); dp=[False]*(len(s)+1); dp[0]=True
        for i in range(1,len(s)+1):
            for l in range(1,min(max_len,i)+1):
                if dp[i-l] and s[i-l:i] in words:
                    dp[i]=True; break
        return dp[-1]
