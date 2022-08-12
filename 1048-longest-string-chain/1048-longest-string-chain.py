class Solution:
    
    def sortByLengthUtil(self,e):
        return len(e)
    
    def longestStrChain(self, words: List[str]) -> int:
        globalCount = 1
        words.sort(key=self.sortByLengthUtil)
        m = {}
        initialLen = len(words[0])
        for index in range(0, len(words)):
            pushIndex = index
            if(len(words[index]) > initialLen):
                pushIndex = index 
                break
            m[words[index]] = 1
            
            
        for index in range(pushIndex, len(words)):
            maxVal = 0
            e = words[index]
            for j in range(0, len(e)):
                sub = e[0:j]+e[j+1:len(e)]

                if(sub not in m):
                    continue
                else:
                    if(m[sub] == len(sub)):
                        maxVal = len(sub)
                        break
                    if(m[sub] >= maxVal):
                        maxVal = m[sub]
            
            m[e] = maxVal+1
            if(maxVal +1 >= globalCount):
                globalCount = maxVal+1
        return globalCount