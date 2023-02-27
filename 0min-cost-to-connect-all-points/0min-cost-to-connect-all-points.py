import heapq
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
    
    def findRoot(self, x):
        while(x != self.parent[x]):
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if(rootX != rootY ):
            if(self.rank[rootX] > self.rank[rootY]):
                self.parent[rootY] = rootX
            elif(self.rank[rootY] > self.rank[rootX]):
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                
    def connected(self, x, y):
        return self.findRoot(x) == self.findRoot(y)
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edgesQueue = []
        heapq.heapify(edgesQueue)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                [x1, y1] = points[i]
                [x2, y2] = points[j]
                distance = abs(x1 - x2) + abs(y1-y2)
                
                heapq.heappush(edgesQueue, (distance, i, j))
        
        uf = UnionFind(len(points))
        minimumCost = 0
        count = 0
        while(len(edgesQueue)>0 and count < len(points)):
            (distance, i, j) = heapq.heappop(edgesQueue)
            if(uf.connected(i,j) == False):
                
                uf.union(i,j)
                minimumCost += distance
                count += 1
        return minimumCost
                
            
        
        
        
       

    
            