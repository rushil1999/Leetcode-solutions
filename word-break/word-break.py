class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordMap = defaultdict(lambda: False)
        for word in wordDict:
            wordMap[word] = True
        
        memo = defaultdict(lambda: False)
        def recurse(word):
            if(len(word) == 0):
                return True
            if(word in memo):
                return memo[word]
            for i in range(1, len(word)+1):
                subWord = word[0:i]
                nextWord = word[i:len(word)]
                if(wordMap[subWord] == True and recurse(nextWord) == True):
                    memo[word] = True
                    return memo[word]
            memo[word] = False
            return memo[word]

                    
            
        val = recurse(s)
        return val