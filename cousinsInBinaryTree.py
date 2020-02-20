class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.hash_map = {}
        def find_node(root,node,parent=None,depth=0):
            if root:
                if root.val != node:
                    find_node(root.left,node,root,depth +1)
                    find_node(root.right,node,root,depth + 1)
                elif root.val == node:
                     self.hash_map[node] = (parent,depth)
                     print("Found")
                
        find_node(root,x)
        find_node(root,y)
        if x in self.hash_map and y in self.hash_map:
            x_parent, x_depth = self.hash_map[x]
            y_parent, y_depth = self.hash_map[y]
            print("We are here")
            if(x_depth == y_depth and x_parent != y_parent):
                return True
        return False
        