class Solution:
    def calc(self,n,arr):
        if(n==0):
            return 1
        if(n<0):
            return 0
        if(arr[n]!=0):
            return arr[n]
        
        arr[n]=self.calc(n-1,arr)+self.calc(n-2,arr)
        
        return arr[n]
        


    def climbStairs(self, n: int) -> int:
        arr=[0]*(n+1)
        ans=self.calc(n,arr)
        
        return ans

        