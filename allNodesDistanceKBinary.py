# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.hash_map = {}
        
        def dfs(root,parent= None):
            if root:
                self.hash_map[root] = parent
                dfs(root.left,root)
                dfs(root.right,root)
                
        dfs(root)
        
        queue = deque()
        queue.append((target,0))
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node,d in queue]
            node, d = queue.popleft()
            for nei in (node.left,node.right,self.hash_map[node]):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei,d+1))
        return []