class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expectedHeights = heights.copy()
        
        while(True):
            swapped = False
            for i in range(len(expectedHeights)-1):
                if(expectedHeights[i+1] < expectedHeights[i]):
                    expectedHeights[i],expectedHeights[i+1] = expectedHeights[i+1], expectedHeights[i]
                    swapped = True
            if(swapped == False):
                break
        print(expectedHeights)
        changeCount = 0
        for i in range(len(expectedHeights)):
            if(heights[i] != expectedHeights[i]):
                changeCount += 1
        return changeCount