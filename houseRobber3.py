# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.memo = {}
        return self.search(root)
        
    def search(self,root:TreeNode):
        if root in self.memo:
            return self.memo[root]
        if not root:
            return 0
        
        val = 0
        if(root.left):
            val += self.search(root.left.left) + self.search(root.left.right)
        if(root.right):
            val += self.search(root.right.right) + self.search(root.right.left)
            
        ans = max(val + root.val, self.search(root.left) + self.search(root.right))
        self.memo[root] = ans
        
        return ans