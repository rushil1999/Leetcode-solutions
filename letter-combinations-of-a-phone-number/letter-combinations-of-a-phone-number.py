class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        print(digits)
        if(len(digits) == 0):
            return []
        
        letterMap = {}
        letterMap['2'] = ['a','b','c']
        letterMap['3'] = ['d','e','f']
        letterMap['4'] = ['g','h','i']
        letterMap['5'] = ['j','k','l']
        letterMap['6'] = ['m','n','o']
        letterMap['7'] = ['p','q','r', 's']
        letterMap['8'] = ['t','u','v']
        letterMap['9'] = ['w','x','y','z']
        
        
        lowerTemp = self.letterCombinations(digits[1:])
        if(len(lowerTemp) == 0):
            return letterMap[digits[0]]
        final = []
        for element in letterMap[digits[0]]:
            for e in lowerTemp:
                final.append(element+e)
        return final
                
                
        