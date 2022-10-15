class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def recurse(index):
            if(index == len(s)):
                return 1
            if(s[index] == "0"):
                return 0
            if(index == len(s)-1 ):
                return 1
            # print(index)
            if(index in memo):
                return memo[index]
        
            
            
            num = int(s[index] + s[index+1])
            val = recurse(index+1)
            if(num <= 26):
                val +=  recurse(index+2) 
            memo[index] = val
            return val
        val = recurse(0)
        # print(val)
        return val
        
            