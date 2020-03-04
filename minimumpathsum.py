#https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if(not grid or len(grid) == 0):
            return 0
        row_length = len(grid)
        column_length = len(grid[0])
        dp = [[0 for col in range(column_length)] for row in range(row_length)]
        #print(dp)
        for i in range(row_length):
            for j in range(column_length):
                dp[i][j] += grid[i][j]
                if(i > 0 and j > 0):
                    #look above us and right of us
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif(i > 0):
                    dp[i][j] += dp[i-1][j]
                elif(j > 0):
                    dp[i][j] += dp[i][j-1]
        #print(dp)
        return dp[row_length - 1][column_length -1]