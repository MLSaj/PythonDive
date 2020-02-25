class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        rows = len(coins) + 1
        columns = amount + 1
        dp = [[0 for i in range(0, columns)] for j in range(0, rows)]


        for i in range(0, rows):
            dp[i][0] = 1

        for i in range(1, columns):
            dp[0][i] = 0

        for row in range(1, rows):
            for column in range(0, columns):
                if coins[row-1] <= column:
                    dp[row][column] = dp[row-1][column] + dp[row][column - coins[row-1]]
                else:
                    dp[row][column] = dp[row-1][column]

        return dp[rows-1][columns-1]