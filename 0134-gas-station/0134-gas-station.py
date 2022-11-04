class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        totalTank, currTank = 0,0
        startStation = 0
        for i in range(n):
            totalTank += gas[i] - cost[i]
            currTank += gas[i] - cost[i]
            
            if(currTank < 0):
                startStation = i+1
                currTank = 0
        return startStation if totalTank >= 0 else -1