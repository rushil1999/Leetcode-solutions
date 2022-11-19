class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = -1, -1
        l = 0
        r = len(nums)-1
        found = False
        foundIndex = -1
        while(l <= r):
            mid = (l+r)//2
            if(nums[mid] > target):
                r = mid-1
            elif(nums[mid] < target):
                l = mid+1
            else:
                foundIndex = mid
                break
        if(foundIndex == -1):
            return [leftPtr, rightPtr]
        
        
        # print("Found Index", foundIndex)
        leftPtr = rightPtr = foundIndex
        # For left side
        r = foundIndex - 1
        l = 0
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] != target):
                l = mid+1
            else:
                if(mid-1>=0 and nums[mid-1]!= target):
                    leftPtr = mid
                    break
                elif(mid-1 >= 0 and nums[mid-1] == target):
                    r = mid-1
                elif(mid-1 < 0):
                    leftPtr = mid
                    break
        # print('left Pointer', leftPtr)
                
        # For right side
        r = len(nums)-1
        l = foundIndex+1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] != target):
                r = mid-1
            else:
                if(mid+1 < len(nums) and nums[mid+1]!= target):
                    rightPtr = mid
                    break
                elif(mid+1 < len(nums) and nums[mid+1] == target):
                    l = mid+1
                elif(mid + 1 >= len(nums)):
                    rightPtr = mid
                    break
                    
                    
        return [leftPtr, rightPtr]
            