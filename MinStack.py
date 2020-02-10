class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 100000000000000000000000
        

    def push(self, x: int) -> None:
        if(x < self.min):
            self.min = x
        self.stack.append({x:self.min})
        
        
                
        

    def pop(self) -> None:
        element = self.stack.pop(len(self.stack) - 1)
        top_value = None
        for key in element:
            top_value = key
        
        #What if we removed the max_value
        if(key == self.min):
            if(len(self.stack) > 0):
                new_top_stack = self.stack[-1]
                new_max = None
                for key in new_top_stack:
                    new_max = key
                self.min = new_top_stack[new_max]
            else:
                self.min = 10000000000000000
            
    
    def top(self) -> int:
        element = self.stack[len(self.stack) - 1]
        for key in element:
            return key
        

    def getMin(self) -> int:
        return self.min
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()