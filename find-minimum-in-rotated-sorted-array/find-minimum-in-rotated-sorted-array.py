class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findPivot(left, right):
            print(left, right)
            if(left > right):return -1
            middle = (left+right)//2
            if(middle -1 >=0 and middle +1 < len(nums) and nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]):
                print("hey")
                return middle
            elif(middle -1 >=0 and nums[middle] < nums[middle-1] ):
                return middle-1
            elif(middle+1 < len(nums) and middle-1 <0 and nums[middle] > nums[middle+1]):
                return middle
            val1 = findPivot(left, middle-1)
            val2 = findPivot(middle+1, right)
            if(val1 > -1):
                return val1
            if(val2 > -1):
                return val2
            return -1
        pivot = findPivot(0, len(nums)-1)
        print(pivot)
        if(pivot == -1):
            return nums[0]
        else:
            return nums[pivot+1]
        
        
#      [3,4,5,1,2]
# [2,1]   
