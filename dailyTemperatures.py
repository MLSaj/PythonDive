#https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if(not T or len(T) == 0):
            return []
        output = [0] * len(T)
        stack = []
        current_day = 0
        while(current_day < len(T)):
            while(len(stack) == 0 or T[current_day] <= T[stack[-1]]):
                #print(current_day)
                stack.append(current_day)
                current_day += 1
                if(current_day >= len(T)):
                    return output
            while(len(stack) > 0 and T[current_day] > T[stack[-1]]):
                last_day = stack.pop()
                output[last_day] = current_day - last_day
        return output            
                    