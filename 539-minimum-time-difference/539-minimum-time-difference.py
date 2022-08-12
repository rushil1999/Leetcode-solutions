class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minList = []
        for time in timePoints:
            hour = int(time[0:2])
            minute = int(time[3:5])
            totalMinutes = hour*60 + minute
            minList.append(totalMinutes)
        minList.sort()
        minVal = float("inf")
        for i in range(1, len(minList)):
            val = minList[i] - minList[i-1]
            minVal = min(minVal, val)
        
        val = 24*60 - minList[-1] + minList[0]
        minVal = min(minVal, val)
        return minVal