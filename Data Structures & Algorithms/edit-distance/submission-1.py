class Solution:

    def recursion(self, word1, word2, ind1, ind2,dp):
        if(ind1<0):
            return ind2+1
        if(ind2<0):
            return ind1+1
        if(dp[ind1][ind2]!=-1):
            return dp[ind1][ind2]
        if(word1[ind1]==word2[ind2]):
            dp[ind1][ind2]=self.recursion(word1, word2, ind1-1, ind2-1,dp)
            return dp[ind1][ind2]
        
        dp[ind1][ind2]=1+min(self.recursion(word1, word2, ind1-1, ind2,dp), 
                    self.recursion(word1, word2, ind1, ind2-1,dp), 
                    self.recursion(word1, word2, ind1-1, ind2-1,dp))
        return dp[ind1][ind2]

    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*(len(word2)+1) for _ in range(len(word1))]
        ans=self.recursion(word1,word2, len(word1)-1, len(word2)-1,dp)

        return ans
        