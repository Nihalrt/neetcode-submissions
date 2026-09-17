class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = len({node for edge in edges for node in edge})
        parent = list(range(1, len({n for e in edges for n in e}) + 1))
        self.result = []

        def find(x):
            if parent[x-1]!=x:
                parent[x-1] = find(parent[x-1])
            return parent[x-1]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx==rooty:
                self.result.append([x,y])
            else:
                parent[rooty-1] = rootx
        
        for a,b in edges:
            union(a,b)
        
        return self.result[-1]
        
        



        