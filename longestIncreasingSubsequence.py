class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        dp = [1]*(len(nums))
        for k in range(len(dp)):
            i = 0
            j = k
            current_max = dp[k]
            while(i != j):
                if(nums[j] > nums[i]):
                    dp[k] = max(dp[i] + 1, dp[k])
                i += 1
        return max(dp)