class Solution:
    def calc(self,nums,ind,memo):
        if ind>=len(nums):
            return 0
        if (memo[ind]!=-1):
            return memo[ind]
        memo[ind]=max(nums[ind]+self.calc(nums,ind+2,memo), self.calc(nums,ind+1,memo))

        return memo[ind]

    def rob(self, nums: List[int]) -> int:
        memo=[-1]*(len(nums)+1)
        ans=(self.calc(nums,0,memo))

        return ans
        