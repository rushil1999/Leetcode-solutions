class Solution:
    
    def recurse(self, m, n):
        mod = 1000000007

        if(n==1):
            return [1,1,1,1,1,1,1,1,1,1]
        val = [0]*10
        arr = self.recurse(m, n-1)
        for i in range(0, 10):
            for k in m[i]:
                val[k] = (val[k]%mod + arr[i]%mod)%mod
        return val
    
    def knightDialer(self, n: int) -> int:
        # dp = [[0]*(10)]*(n+1)
        mod = 1000000007
        # print("After initialization", dp)
        
        stepsMap= {
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [7,1,0],
            7: [2,6],
            8: [1,3],
            9: [4,2],
            0: [4,6],
        }
        
        dp = self.recurse(stepsMap, n)
        # print(dp)
        total = 0
        for i in range(0, 10):
            # print(dp[i])
            total += dp[i]%mod
        return total%mod
            