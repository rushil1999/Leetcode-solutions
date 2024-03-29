class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = 0
        while(left<right):
            minHeight = min(height[right], height[left])
            maxArea = max(maxArea, ((right-left))*(min(height[right], height[left])))
            if(minHeight == height[left]):
                left += 1
            else:
                right -= 1
        return maxArea