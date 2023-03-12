class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0,0
        while(slow < len(nums)):
            if(nums[slow] == val or nums[slow] == -1):
                if(fast <= slow):
                    fast = slow+1
                while(fast < len(nums)):
                    if(nums[fast] != val and nums[fast]!= -1):
                        nums[slow] = nums[fast]
                        nums[fast] = -1
                        fast += 1
                        break
                    else:
                        fast += 1
            slow+=1
            if(slow > fast):
                fast = slow
        print(nums)
        
        for i in range(len(nums)):
            if(nums[i] == -1 or nums[i] ==val):
                return i
        return len(nums)