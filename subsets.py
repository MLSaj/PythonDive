#https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def findAllSubsets(nums,results,subset,startIndex):
            results.append(subset[:])
            for i in range(startIndex,len(nums)):
                subset.append(nums[i])
                findAllSubsets(nums,results,subset,i+1)
                subset.pop()
        
        res = []
        subset = []
        findAllSubsets(nums,res,subset, 0)
        return res