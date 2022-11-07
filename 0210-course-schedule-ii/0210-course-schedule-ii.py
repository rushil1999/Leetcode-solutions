class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for courses in prerequisites:
            course = courses[0]
            prereq = courses[1]
            if prereq in graph:
                graph[prereq].append(course)
            else:
                graph[prereq] = [course]
        
        visited = {}
        for k in range(numCourses):
            visited[k] = 0
        final = []
        flag = False
        print(graph)
        
        def dfs(node):
            
            nonlocal flag
            
            if(flag == True):
                return
            visited[node] = 1
            
            if(node in graph):
                for course in graph[node]:
                    if(visited[course] == 0):
                        dfs(course)
                    elif(visited[course] == 1):
                        flag = True
                        break
            visited[node] = 2
            final.append(node)
        
        for course in range(numCourses):
            if(visited[course] == 0):
                dfs(course)
        return final[::-1] if flag == False else []
                        
        
        
                
        