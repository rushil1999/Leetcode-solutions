class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def recurse(sr):
            if(len(sr) == 0):
                return 0
            if(sr == "0" or (len(sr)>1 and sr[0] == "0")):
                return 0
            elif(len(sr) == 1 and sr != "0"):
                return 1
        
            
            if(sr in memo):
                return memo[sr]
            
            val1 = sr[1:len(sr)]
            child1 = recurse(val1)
            
            
            val2 = sr[2:len(sr)]
            if(int(sr[0:2]) <= 26):
                child2 = recurse(val2)
            else:
                child2 = 0
            
            memo[val1] = child1
            memo[val2] = child2
            memo[sr] = child1+ child2
            if(len(sr) == 2 and int(sr)<=26):
                memo[sr] +=1
                        
            return memo[sr]
        
        ans = recurse(s)
        return ans
            