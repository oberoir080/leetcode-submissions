class Solution:
    def recursion(self, matrix, r, c,dp):
        if dp[r][c]!=-1:
            return dp[r][c]

        row=[-1,1,0,0]
        col=[0,0,-1,1]

        dp[r][c]=1

        for i in range(4):
            nR=row[i]+r
            nC=col[i]+c

            if(nR>=0 and nR<len(matrix) and nC>=0 and nC<len(matrix[0]) and matrix[nR][nC]>matrix[r][c]):
                dp[r][c]=max(dp[r][c], 1+self.recursion(matrix,nR,nC,dp))
        
        return dp[r][c]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res=0
        dp=[[-1]*(len(matrix[0])+1) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res=max(res,self.recursion(matrix,i,j,dp))

        return res
        