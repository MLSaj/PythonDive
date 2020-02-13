# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        hash_map = {}
        i = 1
        curr = head
        while(curr):
            hash_map[i] = curr
            curr = curr.next
            i += 1
        
        if(i - (n+1) >= 1) :
            previous =  hash_map[i - (n+1)]
            nth_from_last = i - n
            node_to_remove = hash_map[nth_from_last]
            next_one = node_to_remove.next 
            previous.next = next_one
            #node_to_remove.next = None
        else:
            head = head.next
        return head