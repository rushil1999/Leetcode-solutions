class Solution:
    
    
    def sol(self, src, target, graph, visited):
        print(src, target)
        
        if(src in visited):
            return 1.0
        else:
            visited[src] = True
        
        if(src not in graph or target not in graph):
            return -1.0
        
        if(src == target):
            return 1.0
        
        for child in graph[src]:
            if(child[0] not in visited):
                val = self.sol(child[0], target, graph, visited)
                visited[child[0]] = True
                print("Going Deep", src, child, val)
                if(val >=0.0 ):
                    return val*child[1]
        return -1.0
            
    
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        for index in range(0, len(equations)):
            value = values[index]
            src = equations[index][0]
            target = equations[index][1]
            
            if(src in graph):
                graph[src].append((target, value))
            else:
                graph[src] = [(target, value)]
            
            if(target in graph):
                graph[target].append((src, 1/value))
            else:
                graph[target] = [(src, 1/value)]
        print(graph)
        
        final = []
        for query in queries:
            src = query[0]
            target = query[1]
            val = self.sol(src, target, graph, {})
            final.append(val)
        return final
        
        
            