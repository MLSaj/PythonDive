import heapq
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap,-1*num)
        heappush(self.min_heap,-1*self.max_heap[0])
        heappop(self.max_heap)
        
        while(len(self.max_heap) < len(self.min_heap)):
            heappush(self.max_heap,-1*self.min_heap[0])
            heappop(self.min_heap)
    
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -1*(self.max_heap[0])
        else:
            top = -1*self.max_heap[0]
            bottom = self.min_heap[0]
            return (top+bottom)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()