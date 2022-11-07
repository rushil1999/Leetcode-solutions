class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.outerPtr = 0
        self.innerPtr = 0
        self.nestedList = vec.copy()
    
    def next(self) -> int:
        # print(self.nestedList, self.outerPtr, self.innerPtr)
        val = self.nestedList[self.outerPtr][self.innerPtr]
        self.innerPtr += 1
        if(self.innerPtr >= len(self.nestedList[self.outerPtr])):
            self.outerPtr += 1
            self.innerPtr = 0
        return val

    def hasNext(self) -> bool:
        if(self.outerPtr < len(self.nestedList)):
            if(self.innerPtr < len(self.nestedList[self.outerPtr])):
                return True
            else:
                found = False
                while(self.outerPtr < len(self.nestedList)):
                    if(len(self.nestedList[self.outerPtr]) > 0):
                        self.innerPtr = 0
                        found = True
                        break
                    self.outerPtr += 1
                if(found):
                    return True
                else:
                    return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()