class Solution:
    def check(self,nums,ind,curr,target):
        if(ind<0):
            return False
        if curr==target:
            return True

        return self.check(nums,ind-1,curr+nums[ind],target) or self.check(nums,ind-1,curr,target)



    def canPartition(self, nums: List[int]) -> bool:
        s=0
        for i in nums:
            s+=i
        
        if s%2!=0:
            return False
        
        ans=self.check(nums,len(nums)-1,0,s/2)

        return ans