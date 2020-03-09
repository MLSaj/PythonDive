#https://leetcode.com/problems/partition-equal-subset-sum/submissions/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def helper(nums,index,asum,total,hash_map):
            current = str(index) + "" + str(asum)
            if(current in hash_map):
                return hash_map[current]
            
            if(asum*2 == total):
                return True
            
            if(asum > total/2 or index >= len(nums)):
                return False
            answer = helper(nums,index+1,asum,total,hash_map)  or           helper(nums,index+1,asum+nums[index],total,hash_map)
            hash_map[current] = answer
            return answer
        
        
        total = sum(nums)
        if(total % 2 != 0):
            return False
        hash_map = {}
        return helper(nums,0,0,total,hash_map)
        