class RandomizedSet:

    def __init__(self):
        self.indexMap = {}
        self.set = []

    def insert(self, val: int) -> bool:
        if(val in self.indexMap):
            return False
        self.set.append(val)
        self.indexMap[val] = len(self.set)-1
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.indexMap):
            return False
        else:
            currentIndex = self.indexMap[val]
            lastElement =self.set[-1]
            
            self.set[currentIndex] = lastElement
            self.indexMap[lastElement] = currentIndex
            del self.indexMap[val]
            self.set = self.set[0:len(self.set)-1]
            return True

    def getRandom(self) -> int:
        return random.choice(self.set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()