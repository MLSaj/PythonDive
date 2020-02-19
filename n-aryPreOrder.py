"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        traversal = []
        stack = [root]
        while stack:
            cur = stack.pop()
            traversal.append(cur.val)
            stack.extend(reversed(cur.children))
        return traversal