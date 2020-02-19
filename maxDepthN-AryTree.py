"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def helper(root,depth=0):
            if not root:
                return depth
            #max_depth = 0
            for child in root.children:
                if child:
                    current_depth = helper(child, depth + 1)
                    self.max_depth = max(self.max_depth,current_depth)
            
            return depth
            
        self.max_depth = 0
        helper(root,0)
        return self.max_depth + 1