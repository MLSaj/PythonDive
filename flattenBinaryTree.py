from collections import deque

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root is None):
            return -1
        stack = deque()
        stack.append(root)
        
        while(len(stack) != 0):
            current_node = stack.pop()
            if(current_node.right):
                stack.append(current_node.right)
            if(current_node.left):
                stack.append(current_node.left)
            if(len(stack) != 0):
                current_node.right = stack[-1]
            current_node.left = None
        return root
            