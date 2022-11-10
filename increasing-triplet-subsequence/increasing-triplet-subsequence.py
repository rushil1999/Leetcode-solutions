class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float('inf')
        for num in nums:
            if(num < num1):
                num1 = num
            elif(num < num2 and num > num1):
                num2 = num
            elif(num > num1 and num > num2):
                return True
        return False