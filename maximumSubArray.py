class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        dp = [0] * (len(nums)+1)
        dp[0] = 0
        for i in range(1,len(nums)+1):
            new_sum = dp[i-1] + nums[i-1]
            dp[i] = max(new_sum,nums[i-1])
        
        return max(dp[1:])