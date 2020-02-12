class Solution:
    def helper(self,index,nums):
        if(index == len(nums) -1):
            return True
        if(index >= len(nums)):
            return False
        if(nums[index] == 0):
            return False
        jumps = nums[index]
        while(jumps > 0):
            land = self.helper(index+jumps,nums)
            if(land == True):
                return True
            else:
                jumps -=1
        return False
    
    def canJump(self, nums: List[int]) -> bool:
        land = self.helper(0,nums)
        return land
                