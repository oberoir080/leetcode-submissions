class Solution:
    def check(self,nums, ind, target, curr,dp, offset):
        if(target==curr and ind<0):
            return 1
        if dp[ind][curr+offset]!=-1:
            return dp[ind][curr+offset]
        if(ind<0):
            return 0
        
        dp[ind][curr+offset]=self.check(nums, ind-1, target, curr+nums[ind],dp, offset) + self.check(nums, ind-1, target, curr-nums[ind],dp,offset)

        return dp[ind][curr+offset]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset=sum(nums)
        dp=[[-1]*(2*offset+1) for _ in range(len(nums))]
        ans = self.check(nums, len(nums)-1, target, 0,dp,offset)

        return ans

        