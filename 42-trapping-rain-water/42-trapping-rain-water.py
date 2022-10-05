class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        totalUnitsOfRainTrapped = 0 
        currentMaxHeight = height[0]
        left[0] = height[0]
        for index in range(1,len(height)):
            currentMaxHeight = max(currentMaxHeight, height[index])
            left[index] = currentMaxHeight
        currentMaxHeight = right[-1] = height[-1]
        for index in range(len(height)-2, -1 ,-1):
            currentMaxHeight = max(currentMaxHeight, height[index])
            right[index] = currentMaxHeight
        print(left, right)
        
        
        for index in range(len(height)):
            totalUnitsOfRainTrapped += max(0, min(left[index], right[index])-height[index])
            
        return totalUnitsOfRainTrapped