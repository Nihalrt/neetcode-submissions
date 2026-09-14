class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites==[]:
            result = [i for i in range(numCourses)]
            return result

        def get_vertices(prerequisites):
            vertices = set()
            for source, destination in prerequisites:
                vertices.add(source)
                vertices.add(destination)
            return vertices
        
        courses = get_vertices(prerequisites)

        def topological_sort(nodes, edges):
            graph = [[] for _ in range(nodes)]
            indegree = [0]*nodes
            for before, after in edges:
                graph[after].append(before)
                indegree[before]+=1
            
            queue = deque()

            for ver in range(nodes):
                if indegree[ver]==0:
                    queue.append(ver)
            
            order = []

            while queue:
                course = queue.popleft()
                order.append(course)

                for neighbor in graph[course]:
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        queue.append(neighbor)

            return order

        result = topological_sort(numCourses,prerequisites)
        if len(result)==numCourses:
            return result
        else:
            return []
        