class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        self.components = n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rooty] = rootx
            self.components-=1
            return True
            
        
        for a,b in edges:
            if not union(a,b):
                return False
        if self.components>1:
            return False
        return True
        

            
