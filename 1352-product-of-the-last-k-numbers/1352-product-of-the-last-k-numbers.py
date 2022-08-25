class ProductOfNumbers:

    def __init__(self):
        self.prodList = []

    def add(self, num: int) -> None:
        if(num == 0):
            self.prodList = [] 
        else:
            if(len(self.prodList) == 0):
                self.prodList.append(num)
            else:
                self.prodList.append(self.prodList[-1]*num)

    def getProduct(self, k: int) -> int:
        # print(k, self.prodList)
        if(k > len(self.prodList)):
            return 0
        elif(k == len(self.prodList)):
            return self.prodList[-1]
        else:
            return self.prodList[-1]//self.prodList[len(self.prodList)-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)