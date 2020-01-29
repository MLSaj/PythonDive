import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if(nums == None or len(nums) == 0):
            return []
        Qi = collections.deque()
        n = len(nums)
        output = []
        for i in range(k):
               
            while(Qi and nums[i] >= nums[Qi[-1]]):
                Qi.pop()
                
            Qi.append(i)
        
        for i in range(k,n):
            output.append(nums[Qi[0]])
            
            while Qi and Qi[0] <= i - k :
                Qi.popleft()
                
            while Qi and nums[i] >= nums[Qi[-1]]:
                Qi.pop()
                
            Qi.append(i)
            
        output.append(nums[Qi[0]])
    
        return output        
            