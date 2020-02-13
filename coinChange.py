class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            current_min = 999999999999
            for coin in coins:
                if(i - coin >= 0 and dp[i-coin] != -1):
                    current_min = min(dp[i-coin] + 1, current_min)
                    dp[i] = current_min
            if(dp[i] == 0):
                dp[i] = -1
                
        return dp[amount]