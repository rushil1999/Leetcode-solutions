class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        startingElement = 0
        m = set([])
        count = 0
        for index in range(len(arr)):
            m.add(arr[index])
            flag = False
            for j in range(startingElement, index+1):   
                if(j not in m):
                    flag = True
                    break
            if(flag == False):
                count += 1
                startingElement = index+1
        return count