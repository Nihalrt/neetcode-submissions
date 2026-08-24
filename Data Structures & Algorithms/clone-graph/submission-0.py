"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        map_track = {}
        clone_start = Node(node.val)
        map_track[node] = clone_start
        queue = deque([node])
        while queue:
            current_node = queue.popleft()
            for n in current_node.neighbors:
                if n not in map_track:
                    map_track[n] = Node(n.val)
                    queue.append(n)
                map_track[current_node].neighbors.append(map_track[n])
        return clone_start

            


        


        