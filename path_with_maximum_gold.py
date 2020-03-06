#https://leetcode.com/problems/path-with-maximum-gold/submissions/
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        def do_something(row,column,visited,max_value):
            key = 'row ' + str(row) + ' column ' + str(column)

            if(row >= len(grid) or column >= len(grid[0]) or row < 0 or column < 0):
                return max_value
            elif(grid[row][column] == 0 or key in visited):
                return max_value


            max_value += grid[row][column]
            visited[key] = True

            bottom = do_something(row + 1, column, visited.copy(),max_value)
            top = do_something(row - 1, column, visited.copy(),max_value)
            right = do_something(row, column + 1, visited.copy(), max_value)
            left = do_something(row,column - 1, visited.copy(),max_value)
            return max(bottom,top,right,left)
        
        max_val = -999999999999
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] != 0):
                    visited = {}
                    current_val = do_something(i,j, {},0)
                    max_val = max(current_val,max_val)
        return max_val
        