class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        temp = high
        finalLength = 0
        while(temp>0):
            temp//=10
            finalLength+= 1
        print(finalLength)
        dp = [[0]*100]*11
        for index in range(1, 10):
            dp[1][index] = index
        
        for size in range(2, finalLength+1):
            for index in range(1, 9-size+2):
                dp[size][index] = (dp[size-1][index]*10)+((dp[size-1][index]%10)+1)
                if(dp[size][index]>=low and dp[size][index]<=high):
                    ans.append(dp[size][index])
                # print(size, dp[size][index])
        return ans