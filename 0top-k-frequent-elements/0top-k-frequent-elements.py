class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([])
        print(dp)
        freqMap = defaultdict(lambda: 0)
        for num in nums:
            freqMap[num] += 1
        
        for element in freqMap:
            print(element, freqMap[element])
            dp[freqMap[element]-1].append(element)
        print(dp)
        final = []
        count = 0
        index = n-1
        while(count < k):
            print("here", dp[index])
            if(len(dp[index]) > 0):
                while(len(dp[index]) >0):
                    count += 1
                    final.append(dp[index][-1])
                    dp[index] = dp[index][:-1]
            index -=1
                
        return final
            