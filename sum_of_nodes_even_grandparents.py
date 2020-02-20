# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.val = 0
        def helper(root):
            if(root):
                if(root.val % 2 == 0):
                    #check if it has grandkids
                    grandkid_1 = 0
                    grandkid_2 = 0
                    grandkid_3 = 0 
                    grandkid_4 = 0
                    if root.left:
                        grandkid_1 = root.left.left.val if root.left.left else 0
                        grandkid_2 = root.left.right.val if root.left.right else 0
                    if root.right:
                        grandkid_3 = root.right.left.val if root.right.left else 0
                        grandkid_4 = root.right.right.val if root.right.right else 0
                    self.val += grandkid_1 + grandkid_2 + grandkid_3 + grandkid_4
                helper(root.left)
                helper(root.right)
                    
        helper(root)
        return self.val
        
