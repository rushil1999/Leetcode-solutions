class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        changes = []
        for index in range(len(s1)):
            if(s1[index] != s2[index]):
                changes.append((s1[index], s2[index]))
            if(len(changes)>2):
                return False
        
        if(len(changes) == 0):
            return True
        elif(len(changes) == 2):   
            if(changes[0][1] == changes[1][0] and changes[0][0] == changes[1][1]):
                return True
        return False
                
 
        
            