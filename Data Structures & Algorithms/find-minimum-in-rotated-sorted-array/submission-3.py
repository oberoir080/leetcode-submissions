class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        ans=float('inf')

        while(lo<=hi):
            mid=(lo+hi)//2
            if(nums[lo]<= nums[mid]):
                ans=min(nums[lo],ans)
                lo=mid+1
            else:
                ans=min(nums[mid],ans)
                hi=mid-1
                
            
        return ans

        