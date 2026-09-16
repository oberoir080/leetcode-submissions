class Solution:
    def check(self, nums, ind, memo):
        if ind>=len(nums):
            return 0
        if memo[ind]!=-1:
            return memo[ind]
        
        memo[ind]=max(nums[ind]+self.check(nums,ind+2,memo), self.check(nums,ind+1,memo))
        
        return memo[ind]

    def rob(self, nums: List[int]) -> int:
        if(len(nums))==1:
            return nums[0]
        memo1=[-1]*(len(nums)+1)
        memo2=[-1]*(len(nums)+1)
        ans=max(self.check(nums[:-1],0,memo1), self.check(nums[1:],0,memo2))

        return ans
        