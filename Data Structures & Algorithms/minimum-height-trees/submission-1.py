class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        
        for node1, node2 in edges:
            graph[node2].append(node1)
            graph[node1].append(node2)
            degree[node1]+=1
            degree[node2]+=1
        
        leaves = deque()

        for node in range(n):
            if degree[node] == 1:
                leaves.append(node)
        
        remaining_nodes = n

        while remaining_nodes > 2:
            layer_size = len(leaves)
            remaining_nodes -= layer_size

            for _ in range(layer_size):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor]-=1

                    if degree[neighbor]==1:
                        leaves.append(neighbor)
        
        roots = list(leaves)
        return roots


    

        