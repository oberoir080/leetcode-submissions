class Solution:
    def lis(self, nums, ind, prev,dp):
        if ind>=len(nums): 
            return 0
        
        if dp[ind][prev]!=-1:
            return dp[ind][prev]
        
        dp[ind][prev]= self.lis(nums, ind+1, prev,dp)
        if(prev==-1 or nums[ind]>nums[prev]):
            dp[ind][prev]=max(dp[ind][prev],1+self.lis(nums, ind+1, ind,dp))

        return dp[ind][prev]
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[[-1]*(len(nums)+1) for _ in range(len(nums)+1)]
        ans=self.lis(nums, 0, -1,dp)

        return ans
        