class Solution:
    
    def createTimeArray(self,minutes, seconds):
        time = []
        time.append(minutes//10)
        time.append(minutes%10)
        time.append(seconds//10)
        time.append(seconds%10)
        
        for index in range(0,4):
            if(time[index] > 0):
                break
        time = time[index: len(time)]
        return time
    
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        timeConfigurations = []
        
        minutes = targetSeconds//60
        seconds = targetSeconds%60
        
        if(minutes > 99):
            minutes = 99
            seconds = seconds + 60
        timeConfigurations.append(self.createTimeArray(minutes, seconds))
        
        if(seconds + 60 <= 99 and minutes > 0):
            minutes = minutes - 1
            seconds = seconds + 60
            if(minutes > 99):
                minutes = 99
                seconds = seconds + 60
            timeConfigurations.append(self.createTimeArray(minutes, seconds))
            
            
        minCost = float("inf")
        
        for configuration in timeConfigurations:
            currentPosition = startAt
            cost = 0
            for unit in configuration:
                if(currentPosition != unit):
                    currentPosition = unit
                    cost += moveCost
                cost += pushCost
            if(cost < minCost):
                minCost = cost
                
        return minCost