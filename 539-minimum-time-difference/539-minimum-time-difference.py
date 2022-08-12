class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minList = []
        for time in timePoints:
            hour = int(time[0:2])
            minute = int(time[3:5])
            print(hour, minute)
            totalMinutes = hour*60 + minute
            
            minList.append(totalMinutes)
        print(minList)
        minList.sort()
#         print(minList)
#         print(abs(minList[1][0]-minList[0][1]))
        
#         print(abs(minList[1][0]- minList[0][0]))
#         print(abs(minList[1][1]- minList[0][0]))
#         print(abs(minList[1][1]- minList[0][1]))
        minVal = float("inf")
        for i in range(1, len(minList)):
            val = minList[i] - minList[i-1]
            minVal = min(minVal, val)
        
        val = 24*60 - minList[-1] + minList[0]
        minVal = min(minVal, val)
        return minVal