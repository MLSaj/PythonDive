class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        def helper(root,L,R):
            if root:
                if root.val >= L and root.val <= R: 
                    self.sum += root.val
                    helper(root.right,L,R)
                    helper(root.left,L,R)
                elif root.val < L:
                    helper(root.right,L,R)
                elif root.val > R:
                    helper(root.left,L,R)
            else:
                return 0
        helper(root,L,R) 
        return self.sum