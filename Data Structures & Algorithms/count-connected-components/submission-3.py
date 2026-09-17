class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        self.components = n
        answer = 0

        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x,y):
            answer = 0
            rootx = find(x)
            rooty = find(y)

            if rooty!=rootx:
                parent[rooty] = rootx
                self.components-=1
                return self.components
            else:
                return self.components
        
        for a,b in edges:
            answer = union(a,b)
        return answer
            
                
        