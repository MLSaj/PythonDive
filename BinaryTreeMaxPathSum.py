# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def dfs(self,root):
        if root is None:
                return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        maxLR = max(left,right)
        maxSingle = max(maxLR + root.val, root.val)
        maxAll = max(maxSingle,root.val + left + right)
        self.max_path_sum = max(self.max_path_sum, maxAll)
        return maxSingle
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum = -1000000000000
        self.dfs(root)
        return self.max_path_sum