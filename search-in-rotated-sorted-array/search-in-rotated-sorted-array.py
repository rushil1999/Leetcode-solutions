class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchUsingBinarySearch(left, right):
            while(left<= right):
                middle = (left+right)//2
                if(nums[middle] == target):
                    return middle
                elif(nums[middle]> target):
                    right = middle-1
                else:
                    left = middle+1
            return -1
        
        def searchForPivot(left, right):
            middle = (left+right)//2    
            if(middle+1 < len(nums)):
                if(nums[middle] >= nums[middle+1]):
                    return middle
            elif(middle-1>=0):
                if(nums[middle-1] >= nums[middle]):
                    return middle-1
            if(right> left):
                val1 = searchForPivot(left, middle-1)
                val2 = searchForPivot(middle+1, right)
                
                if(val1 > -1):
                    return val1
                if(val2 > -1):
                    return val2
            return -1
        
        
        pivot = searchForPivot(0, len(nums)-1)
        if(pivot == -1):
            return searchUsingBinarySearch(0, len(nums)-1)
        if(nums[pivot] == target):
            return pivot
        
        val1 = searchUsingBinarySearch(0, pivot-1)
        val2 = searchUsingBinarySearch(pivot+1, len(nums)-1)
        return val1 if val1>-1 else val2    
        return -1
          
        