class Solution:

    def __init__(self, w: List[int]):
        self.sumArray = []
        runningSum = 0
        for weight in w:
            runningSum += weight
            self.sumArray.append(runningSum)
        self.totalSum = runningSum

    def pickIndex(self) -> int:
        target = self.totalSum * random.random()
        for i, val in enumerate(self.sumArray):
            if(target < val):
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()