class Solution:
    
    def __init__(self):
        self.stepsMap = {}
    
    def calculatePower(self, num):
        if(num == 1):
            return 0
        if(num in self.stepsMap):
            return self.stepsMap[num]
        if(num%2 == 0):
            val = num/2
        else:
            val = (3*num)+1
        power = self.calculatePower(val) + 1
        self.stepsMap[num] = power
        return power
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        numPowerList = []
        for num in range(lo, hi+1):
            power = self.calculatePower(num)
            numPowerList.append((num,power))
        finalList = sorted(numPowerList, key=lambda x: x[1])
        
        return finalList[k-1][0]