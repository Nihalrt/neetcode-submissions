class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        # Fixed: attached explicitly to the instance object via self
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        # Link them together cleanly
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        # Case 1: the key already exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
        # Case 2: the key doesn't exist
        elif key not in self.cache:
            new_node = Node(key, value)
            self.cache[key] = new_node
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                del self.cache[lru_node.key]
                self.tail.prev = lru_node.prev
                lru_node.prev.next = self.tail



        
