class Solution:
    def recu(self, i, j, m, n,dp):
        if(i>m or j>n):
            return 0
        if(i==m and j==n):
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]
        
        dp[i][j]=self.recu(i+1,j,m,n,dp)+self.recu(i,j+1,m,n,dp)

        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for _ in range(m)]
        ans=self.recu(0,0,m-1,n-1,dp)

        return ans
        