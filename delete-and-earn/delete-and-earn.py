class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        size = len(nums)
        count = defaultdict(lambda: 0)
        for i in range(size):
            count[nums[i]] += 1
        arr = []
        for key in list(count.keys()):
            arr.append((key, count[key]))
        arr.sort(key = lambda x: x[0])
        subSize = len(arr)
        dp = [[0]*2 for _ in range(subSize)]
        dp[0][0] = 0
        dp[0][1] = arr[0][0]*arr[0][1]
        
        for i in range(1, subSize):
            currentVal = arr[i][0]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            if(currentVal-arr[i-1][0] == 1):
                dp[i][1] = currentVal * arr[i][1] + dp[i-1][0]
            else:
                dp[i][1] = currentVal*arr[i][1] + dp[i][0]
        return max(dp[subSize-1][0], dp[subSize-1][1])
        
        