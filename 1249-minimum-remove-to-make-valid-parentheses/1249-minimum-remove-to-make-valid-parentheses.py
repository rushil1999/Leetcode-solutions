class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indicesToRemove = []
        for index in range(len(s)):
            if(s[index].isalpha() == False):
                if(len(stack) > 0):
                    top = stack[-1]
                    if(top[0] == '(' and s[index] == ')'):
                        stack = stack[0:len(stack)-1]
                    
                    else:
                        stack.append((s[index], index))
                else:
                    stack.append((s[index], index))
        # print(stack)
        indicesSet = set([])
        for element in stack:
            indicesSet.add(element[1])
        # print(indicesSet)
        
        
        final = "".join([char for idx, char in enumerate(s) if idx not in indicesSet])
        
        return final
