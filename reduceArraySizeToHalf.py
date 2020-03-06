#https://leetcode.com/problems/reduce-array-size-to-the-half/
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if(not arr or len(arr) == 0):
            return 0
        hash_table = {}
        for num in arr:
            if num in hash_table:
                hash_table[num] -= 1
            else:
                hash_table[num] = -1
        heap = []
        for key in hash_table:
            heapq.heappush(heap,hash_table[key])
        
        elements_taken_out = 0
        half_array = len(arr) / 2
        counter = 0
        while(elements_taken_out < half_array):
            elements_taken_out += -(heapq.heappop(heap))
            counter += 1
        return counter