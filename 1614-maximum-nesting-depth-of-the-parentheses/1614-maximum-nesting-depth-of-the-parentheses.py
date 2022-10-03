class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        currentDepth = 0
        for character in s:
            if(character == '('):
                stack.append(character)
                currentDepth +=1
                maxDepth = max(maxDepth, currentDepth)
            elif(character == ')'):
                top = stack[-1]
                if(top != "("):
                    return -1
                else:
                    stack = stack[0:len(stack)-1]
                    currentDepth -= 1
        if(currentDepth > 0):
            maxDepth = max(currentDepth, maxDepth)
        return maxDepth
    