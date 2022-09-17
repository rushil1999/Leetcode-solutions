class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        populationMap = {}
        for log in logs:
            for year in range(log[0], log[1]):
                populationMap[year]= populationMap[year] + 1 if year in populationMap else 1
        maxCount = 0
        maxYear = float("inf")
        for year in populationMap:
            if(populationMap[year] > maxCount):
                maxCount = populationMap[year]
                maxYear = year
            elif(populationMap[year] == maxCount):
                maxYear = min(year, maxYear)
        return maxYear