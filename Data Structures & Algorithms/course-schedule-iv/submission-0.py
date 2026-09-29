from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        result = [False] * len(queries)

        def find_prereq(num_of_courses, prereqs):
            graph = [[] for _ in range(num_of_courses)]
            indegree = [0] * num_of_courses
            prereq_position = { c: set() for c in range(num_of_courses)}

            for pre, course in prereqs:
                graph[pre].append(course)
                indegree[course]+=1
                prereq_position[course].add(pre)
            
            queue = deque([i for i in range(num_of_courses) if indegree[i] == 0])
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    prereq_position[neighbor].update(prereq_position[curr])
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        queue.append(neighbor)
            return prereq_position

        
        pres = find_prereq(numCourses, prerequisites)
        
        for i in range(len(queries)):
            if queries[i][0] in pres[queries[i][1]]:
                result[i] = True
        return result


                
            
        