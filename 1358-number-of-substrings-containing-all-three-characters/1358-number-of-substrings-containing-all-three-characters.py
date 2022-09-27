class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right, prevLeft = 0,0, 0
        charMap = {s[0]:1}
        count = 0
        while(left<=right ):
            if(len(charMap) < 3 and right < len(s)-1):
                right += 1
                charMap[s[right]] = 1 if s[right] not in charMap else charMap[s[right]]+1
            elif(len(charMap) == 3):
                count += len(s) - right
                
                charMap[s[left]] -=1
                if(charMap[s[left]] == 0):
                    del charMap[s[left]]
                left += 1
            else: left+=1
        return count    
        
        
            
        