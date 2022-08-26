class Solution:
    def informEmployees(self, managerId, timeMap, informTime, orgMap):
        if(managerId not in orgMap):
            return 
        
        for j in orgMap[managerId]:
            # print(j)
            # print(j, timeMap, timeMap)
            # print(timeMap[managerId])
            # print(informTime[managerId])
            timeMap[j] = timeMap[managerId] + informTime[managerId]
            self.informEmployees(j, timeMap, informTime, orgMap)
    
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        timeMap = {}
        orgMap = {}
        for i in range(0, len(manager)):
            if(manager[i] == -1):
                continue
            if(manager[i] not in orgMap):
                orgMap[manager[i]] = [i]
            else:
                orgMap[manager[i]].append(i)
        # print(orgMap)
        timeMap[headID] = 0
        self.informEmployees(headID, timeMap, informTime,orgMap)
        maxTime = 0
        for empId in timeMap:
            maxTime = max(timeMap[empId], maxTime)
        # print(timeMap)
        return maxTime
        
        
        
        
                
        