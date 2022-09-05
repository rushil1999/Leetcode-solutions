from functools import cmp_to_key
class Solution:
    
    
 
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        n = len(costs)
        
        
        costs.sort(key = lambda x : x[0] - x[1])
        total = 0
        for i in range(n//2):
            print(i)
            total += costs[i][0] + costs[i+(n//2)][1]
            
        
        
        return total