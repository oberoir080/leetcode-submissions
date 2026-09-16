class Solution:
    def lcs(self, text1, text2, ind1, ind2,dp):
        if(ind1>=len(text1) or ind2>=len(text2)):
            return 0
        if(dp[ind1][ind2]!=-1):
            return dp[ind1][ind2]
        if(text1[ind1]==text2[ind2]):
            dp[ind1][ind2] = 1+self.lcs(text1, text2,ind1+1,ind2+1,dp)
            return dp[ind1][ind2]
        
        dp[ind1][ind2]=max(self.lcs(text1, text2,ind1+1,ind2,dp), self.lcs(text1, text2,ind1,ind2+1,dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*(len(text2)+1) for _ in range(len(text1)+1)]
        ans=self.lcs(text1,text2,0,0,dp)

        return ans

        