class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        hash_map = {}
        traversal = [] 
        while(len(stack) != 0):
            last_child = stack[-1]
            #are we at a leaf or did we already deal with its children
            if(len(last_child.children) == 0 or last_child.children[0] in hash_map):
                last_child = stack.pop()
                hash_map[last_child] = True
                traversal.append(last_child.val)
            else:
                for i in range(1,len(last_child.children)+1):
                    stack.append(last_child.children[-1*i])
        return traversal