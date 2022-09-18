class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        indexList = arr.copy()
        rankMap = {}
        indexList.sort()
        if(len(arr) == 0):
            return []
        rankMap[indexList[0]] = 1
        for index in range(1,len(indexList)):
            rankMap[indexList[index]] = rankMap[indexList[index-1]]+1 if indexList[index] != indexList[index-1] else rankMap[indexList[index-1]]
        finalList = []
        for element in arr:
            finalList.append(rankMap[element]) 
        return finalList