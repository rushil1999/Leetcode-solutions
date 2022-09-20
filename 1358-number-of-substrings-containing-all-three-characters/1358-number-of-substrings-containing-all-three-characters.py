class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        characterSet = set(['a','b','c'])
        freqMap = {}
        # for char in s:
        #     characterSet.add(char)
        
        left = 0
#         for index in range(len(s)):
#             freqMap[s[index]] = 1 if s[index] not in freqMap else freqMap[s[index]]+1
            
#             if(len(freqMap) == len(characterSet)):
#                 index+1
#                 break
        
        count = 0
        # print("Length of character set", len(characterSet))
        left, right = 0,0
        
        print(left, right, count, len(characterSet), len(freqMap))
        while(left<=right):
            freqMap[s[right]] = 1 if s[right] not in freqMap else freqMap[s[right]]+1
            # print("Outer Loop", left, right, freqMap)
            while(len(freqMap) ==len(characterSet) ):
                count += len(s)- right
                # print("Caught", left, right, s[left:right+1], count, freqMap)
                freqMap[s[left]] -=1
                if(freqMap[s[left]] == 0):
                    del freqMap[s[left]]
                left += 1
                
            right+= 1
            if(right >= len(s) ):
                break
                
                
                
        return count
            
        
        
            
        