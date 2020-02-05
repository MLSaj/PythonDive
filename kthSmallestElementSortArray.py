import heapq
from heapq import heappush, heappop,heapify
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][y],0,y) for y in range(len(matrix))]
        heapify(heap)
        res = 0 
        for i in range(k):
            res, x, y = heappop(heap)
            if x + 1 < len(matrix):
                heappush(heap,(matrix[x+1][y], x+1,y))
        return res