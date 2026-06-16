"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        new = {None:None}

        while curr:
            new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            clone = new[curr]
            clone.next = new[curr.next]
            clone.random = new[curr.random]
            curr = curr.next
        return new[head]
        