# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        versionMap = {}
        left, right = 1, n
        while(left<= right):
            middle = (left+right)//2
            response = isBadVersion(middle)
            versionMap[middle] = response
            if(response == False):
                left = middle+1
            elif(response == True):
                if(middle-1>0):
                    if(middle-1 not in versionMap):
                        resp = isBadVersion(middle-1)
                    else:
                        resp = versionMap[middle-1]
                    
                    if(resp == False):
                        return middle
                    else:
                        right = middle-1
                else:
                    return middle
        