class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        foundFlag = False
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid] > target):
                right = mid-1
            elif(nums[mid] < target):
                left = mid+1
            else:
                foundFlag = True
                final = []
                flag = False
                for j in range(mid,-1, -1):
                    if(nums[j]!= nums[mid]):
                        final.append(j+1)
                        flag = True
                        break
                if(flag == False):
                    final.append(0)
                flag = False    
                for j in range(mid,len(nums)):
                    if(nums[j]!= nums[mid]):
                        final.append(j-1)
                        flag = True
                        break
                if(flag == False):
                    final.append(len(nums)-1)
                    
                break
        return final if foundFlag == True else [-1, -1]