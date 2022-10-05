class MaxStack:    
    def __init__(self):
        self.stack = []
        self.heapList = []
        heapq.heapify(self.heapList)
        self.removed = {}
        self.counter = 1
        
    def push(self, x: int) -> None:
        self.stack.append((self.counter, x))
        heapq.heappush(self.heapList, (-x, -self.counter))
        self.counter += 1
        
    def pop(self) -> int:
        while(len(self.stack) > 0 and self.stack[-1][0] in self.removed):
            self.stack = self.stack[0:len(self.stack)-1]
        poppedElement = self.stack[-1]
        self.removed[poppedElement[0]] = True
        self.stack = self.stack[0:len(self.stack)-1]
        return poppedElement[1]
    def top(self) -> int:
        while(len(self.stack) > 0 and self.stack[-1][0] in self.removed):
            self.stack = self.stack[0:len(self.stack)-1]
        return self.stack[-1][1] if len(self.stack) > 0 else []
    def peekMax(self) -> int:
        while(len(self.heapList) > 0 and -self.heapList[0][1] in self.removed):
            heapq.heappop(self.heapList)
        return -self.heapList[0][0] if len(self.heapList) > 0 else []
    def popMax(self) -> int:
        while(len(self.heapList) > 0 and -self.heapList[0][1] in self.removed):
            heapq.heappop(self.heapList)
        poppedElement = heapq.heappop(self.heapList)
        self.removed[-poppedElement[1]] = True
        
        return -poppedElement[0]
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()