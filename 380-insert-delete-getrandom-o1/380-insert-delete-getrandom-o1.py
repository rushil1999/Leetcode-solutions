class RandomizedSet:

    def __init__(self):
        self.indexMap = {}
        self.keyList = []
    
    def insert(self, val: int) -> bool:
        if val not in self.indexMap:
            self.keyList.append(val)
            self.indexMap[val] = len(self.keyList)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if(val not in self.indexMap):
            return False
        else:
            index = self.indexMap[val]
            self.keyList.remove(val)
            del self.indexMap[val]
            return True

    def getRandom(self) -> int:
        randomNum = random.choice(self.keyList)
        # for index, key in enumerate(self.store):
        #     if(index == randomIndex):
        #         return key
        
        return randomNum
            


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()