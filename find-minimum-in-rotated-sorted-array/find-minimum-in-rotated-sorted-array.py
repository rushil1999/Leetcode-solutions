class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if(len(nums) == 1):
            return nums[0]
        while(left<=right):
            middle = (left+right)//2
            if(nums[middle] > nums[middle+1]):
                return nums[middle+1]
            elif(nums[middle] < nums[middle-1]):
                return nums[middle]
            elif(nums[right] > nums[middle]):
                right = middle-1
            else:
                left = middle+1
        
            
        
        
  
