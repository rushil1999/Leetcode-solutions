class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.rangeMap = {}
        self.pointer = 0
        prev = 0
        for index in range(0, len(encoding), 2):
            if(encoding[index] <= 0):
                continue
            self.rangeMap[(prev, prev+encoding[index]-1)] = encoding[index+1]
            prev = prev+encoding[index]
        print(self.rangeMap)
    def next(self, n: int) -> int:
        self.pointer += (n)
        
        for key in self.rangeMap:
            if(self.pointer-1 >= key[0] and self.pointer-1 <= key[1]):
                return self.rangeMap[key]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)