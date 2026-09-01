from __future__ import annotations
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[amount+1]*(amount+1); dp[0]=0
        for x in range(1,amount+1):
            for c in coins:
                if c<=x: dp[x]=min(dp[x],dp[x-c]+1)
        return -1 if dp[amount]>amount else dp[amount]
