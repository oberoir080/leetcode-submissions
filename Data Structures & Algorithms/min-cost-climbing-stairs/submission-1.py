class Solution:
    def calc(self, cost, ind, memo):
        if ind>=len(cost):
            return 0
        if memo[ind]!=-1:
            return memo[ind]
        
        #curr+min of ind+1 and ind+2
        memo[ind]= cost[ind]+min(self.calc(cost, ind+1,memo),self.calc(cost,ind+2,memo))

        return memo[ind]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo=[-1]*(len(cost)+1)
        ans=min(self.calc(cost,0,memo),self.calc(cost,1,memo))

        return ans
        