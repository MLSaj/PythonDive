class LinkedList:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkedList(99999999999,0)
        self.tail = LinkedList(-999999999,0)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {}
        
    
        

    def get(self, key: int) -> int:
        if(key in self.hash_map):
            node = self.hash_map[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if(key in self.hash_map):
            node = self.hash_map[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if(len(self.hash_map) == self.capacity):
                node = self.hash_map[self.tail.prev.key]
                del self.hash_map[self.tail.prev.key]
                self.remove(node)    
            node = LinkedList(key,value)
            self.hash_map[key] = node
            self.add(node) 
            
    def add(self,node):
        head_next = self.head.next
        head_next.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = head_next
    
    def remove(self,node):
        next_node = node.next
        previous_node = node.prev
        next_node.prev = previous_node
        previous_node.next = next_node        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)