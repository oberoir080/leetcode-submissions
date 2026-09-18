class Solution:
    def recu(self, coins, ind, amount, dp):
        if(ind<0 or amount<0):
            return 0
        if amount==0:
            return 1
        if dp[ind][amount]!=-1:
            return dp[ind][amount]
        
        dp[ind][amount]=self.recu(coins, ind, amount-coins[ind],dp) + self.recu(coins, ind-1, amount,dp)

        return dp[ind][amount]

        
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        ans=self.recu(coins, len(coins)-1, amount, dp)
        
        return ans