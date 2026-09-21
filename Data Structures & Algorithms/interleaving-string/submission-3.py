class Solution:
    def check(self,s1,s2,s3,ind1,ind2,dp):
        if(ind1+ind2==len(s3)):
            return True
        if(ind2==len(s2)):
            return s1[ind1:] == s3[ind1+ind2:] 
        if(ind1==len(s1)):
            return s2[ind2:] == s3[ind1+ind2:]
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2] 

        if(s1[ind1]==s3[ind1+ind2] and s2[ind2]!=s3[ind1+ind2]):
            dp[ind1][ind2]=self.check(s1,s2,s3,ind1+1,ind2,dp)
            return dp[ind1][ind2]
        if(s2[ind2]==s3[ind1+ind2] and s1[ind1]!=s3[ind1+ind2]):
            dp[ind1][ind2]=self.check(s1,s2,s3,ind1,ind2+1,dp)
            return dp[ind1][ind2]
        if(s1[ind1]!=s3[ind1+ind2] and s2[ind2]!=s3[ind1+ind2]):
            return False
        
        dp[ind1][ind2]=(self.check(s1,s2,s3,ind1+1,ind2,dp) or self.check(s1,s2,s3,ind1,ind2+1,dp))
        return dp[ind1][ind2]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)>len(s3):
            return False
        dp=[[-1]*(len(s2)+1) for _ in range(len(s1))]
        ans=self.check(s1,s2,s3,0,0,dp)

        return ans
        