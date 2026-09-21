class Solution:
    def recu(self,s,t,ind1,ind2,dp):
        if(ind2<0):
            return 1
        if(ind1<0):
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if(s[ind1]==t[ind2]):
            dp[ind1][ind2]=self.recu(s,t,ind1-1,ind2-1,dp) + self.recu(s,t,ind1-1,ind2,dp)
            return dp[ind1][ind2]

        dp[ind1][ind2]=self.recu(s,t,ind1-1,ind2,dp)

        return dp[ind1][ind2]

    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1]*(len(t)+1) for _ in range(len(s))]
        res=self.recu(s,t,len(s)-1,len(t)-1,dp)

        return res


        