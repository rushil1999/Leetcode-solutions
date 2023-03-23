class Solution:
        
    def reverseWords(self, s: str) -> str:
        arr = []
        i = 0
        while(i<len(s)):
            print(i, s[i])
            if(s[i]!= ' '):
                print(s[i])
                start = i
                found = False
                for j in range(i,len(s)):
                    if(s[j] == ' '):
                        found = True
                        word = s[i:j]
                        arr.append(word)
                        i = j
                        break
                if(found == False):
                    word = s[i:j+1]
                    arr.append(word)
                    i = j
                    break
            else:
                i+= 1
        finalStr = ""
        for i in range(len(arr)-1, -1, -1):
            finalStr += arr[i] + " "
        print(finalStr)
        return finalStr[:-1]
                
        