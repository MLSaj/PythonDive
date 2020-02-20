# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def helper(root,current_sum=0):        
            if root:
                current_sum += root.val
                if root.left == None and root.right == None:
                    if(current_sum == sum):
                        return True
                right = helper(root.left, current_sum)
                left = helper(root.right, current_sum)
                return right or left
            
        return helper(root)