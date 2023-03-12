class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        numStr = len(strs)
        strIndex = 0
        index = 0
        finalIndex = -1
        # if(strs[0] == ""):
        #     return ""
        while(True):
            
            if(strIndex < numStr and index < len(strs[strIndex])):
                if(strIndex ==0):
                    ch = strs[strIndex][index]
                else:
                    if(ch != strs[strIndex][index]):
                        finalIndex = index-1
                        break
                strIndex += 1
                if(strIndex >= numStr):
                    strIndex = 0
                    finalIndex = index
                    index += 1
                    
            else:
                break
        return strs[0][0:finalIndex+1]
        