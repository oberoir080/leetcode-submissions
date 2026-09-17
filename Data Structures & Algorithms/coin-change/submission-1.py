class Solution:
    def recu(self, coins, amount, ind,dp):
        if(amount<0 or ind<0):
            return float('inf')
        if(amount==0):
            return 0
        if dp[ind][amount]!=-1:
            return dp[ind][amount]
        dp[ind][amount]=self.recu(coins, amount, ind-1,dp)
        if(coins[ind]<=amount):
            dp[ind][amount]=min(dp[ind][amount], self.recu(coins, amount-coins[ind], ind,dp)+1)
        
        return dp[ind][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        res=self.recu(coins, amount, len(coins)-1,dp)
        if res==float('inf'):
            return -1
        return res
        