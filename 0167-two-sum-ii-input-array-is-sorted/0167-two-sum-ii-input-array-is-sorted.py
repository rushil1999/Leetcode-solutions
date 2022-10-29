class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while(left<right):
            sumOfPairs = numbers[left] + numbers[right]
            if(sumOfPairs < target):
                left += 1
            elif(sumOfPairs > target):
                right -=1
            else:
                return [left+1, right+1]
        