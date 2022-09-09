class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.store):
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.store):
            return ""
        arr = self.store[key] 
        
        l, r = 0, len(arr)-1
        val = 0
        # print("Store ", self.store, timestamp)
        while(l<=r):
            
            mid = (l+r)//2
            print(timestamp, arr[mid])
            if(timestamp == arr[mid][1]):
                return arr[mid][0]
            elif(timestamp > arr[mid][1]):
                val = arr[l]
                l = mid+1
            else:
                r = mid-1
        # print(val)
        return val[0] if val != 0 else ""
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)