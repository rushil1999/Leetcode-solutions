class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        finalArray = [0 for _ in range(len(digits)+1)]
        for i in range(len(digits)-1, -1, -1):
            val = carry + digits[i]
            carry = val//10
            finalArray[i+1] = val%10
        if(carry >0):
            finalArray[0] = carry
        else:
            finalArray = finalArray[1:len(finalArray)]
        return finalArray