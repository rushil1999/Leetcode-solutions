class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        currentIndex = 0
        for i in range(len(nums)):
            minValue = nums[i]
            minIndex = i
            for j in range(i+1, len(nums)):
                if(nums[j] < minValue):
                    minValue = nums[j]
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        print(nums)