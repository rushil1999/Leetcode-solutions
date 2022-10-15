class Solution:
    def countAndSay(self, n: int) -> str:
        def recurse(n):
            if(n == 1):
                return "1"
            childStr = recurse(n-1)
            charStack = []
            for char in childStr:
                if(len(charStack) == 0):
                    charStack.append((char, 1))
                else:
                    top = charStack[-1]
                    if(char == top[0]):
                        charStack[-1] = (charStack[-1][0], charStack[-1][1]+1)
                    else:
                        charStack.append((char, 1))
            newStr = ""
            for element in charStack:
                newStr = newStr + str(element[1]) + element[0]
            # print(n, newStr)
            return newStr
    
        finalStr = recurse(n)
        # print(finalStr)
        return finalStr