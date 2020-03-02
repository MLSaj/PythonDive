#https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if(len(nums) <= 1):
            return False
        def helper(i, nums):
            if(i >= len(nums)):
                return False
            last_sum = nums[i]
            j = i + 1
            while(j < len(nums)):
                last_sum += nums[j]
                if(k != 0 and last_sum % k == 0):
                    return True
                if(k == 0 and last_sum == 0):
                    return True
                if(last_sum == 0):
                    return True
                else:
                    j += 1
            if(j >= len(nums)):
                return helper(i+1,nums)
             
        return helper(0,nums)
        