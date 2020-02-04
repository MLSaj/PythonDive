"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head == None):
            return None
        hash_table = {}
        curr = head
        while(curr):
            hash_table[curr] = Node(curr.val)
            print(curr.val)
            curr = curr.next
            
        curr = head
        while(curr):
            node = hash_table[curr]
            if(curr.next):
                node.next = hash_table[curr.next]
            if(curr.random):
                node.random = hash_table[curr.random]
            curr = curr.next

        return hash_table[head]
        
        