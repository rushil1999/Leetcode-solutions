class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [(1,0)] if s[0] != "0" else [(0,0)]
        for index in range(1,len(s)):
            if(s[index-1] == "0" and s[index] != "0" ):
                dp.append(((dp[-1][0]+dp[-1][1]), 0))
                continue
            elif(s[index-1]!="0" and s[index] == "0"):
                if(s[index-1] == "1" or s[index-1] == "2"):
                    dp.append((0, dp[-1][0]))
                else:
                    dp.append((0,0))
                continue
            elif(s[index-1] == "0" and s[index] == "0"):
                dp.append((0,0))
                continue
            
            
            
            num = int(s[index-1] + s[index])
            if(num <= 26 ):
                dp.append(((dp[-1][0]+dp[-1][1]), dp[-1][0]))
            else:
                dp.append(((dp[-1][0]+dp[-1][1]), 0))
        val = dp[-1]
        print(val)
        return val[0]+val[1]
            