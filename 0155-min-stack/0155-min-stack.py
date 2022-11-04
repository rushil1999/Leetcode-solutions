class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if(len(self.stack) == 0):
            self.stack.append((val, val))
        else:
            currentMinimum = self.stack[-1][1]
            newMinimum = min(currentMinimum, val)
            self.stack.append((val, newMinimum)) 

    def pop(self) -> None:
        if(len(self.stack) > 0):
            self.stack = self.stack[0:len(self.stack)-1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()