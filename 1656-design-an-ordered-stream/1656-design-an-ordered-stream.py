class OrderedStream:

    def __init__(self, n: int):
        self.current = 0
        self.capacity = n
        self.arr = [""]*n

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.arr[idKey-1] = value
        if(self.current == idKey-1):
            while(self.current < self.capacity and len(self.arr[self.current]) > 0):
                ans.append(self.arr[self.current])
                self.current += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)