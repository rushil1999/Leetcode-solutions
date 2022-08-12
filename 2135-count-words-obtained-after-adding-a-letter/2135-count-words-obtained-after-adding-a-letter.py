class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        wordMap = {}
        numMap = {}
        count = 0
        for word in startWords:
            sortedWord = ''.join(sorted(word))
            wordMap[sortedWord] = True
            numMap[len(word)] = True
        
        print(numMap)
        print(wordMap)
        for word in targetWords:
            sortedWord = ''.join(sorted(word))
            print(sortedWord)
            if(len(sortedWord)-1 not in numMap):
                print("Out", sortedWord)
                continue
            for index in range(0, len(sortedWord)):
                val = (sortedWord[0:index]+sortedWord[index+1:len(sortedWord)])
                print("Sublet")
                print(val)
                if((sortedWord[0:index]+sortedWord[index+1:len(sortedWord)]) in wordMap):
                    count+=1
                    print("Accepted", (sortedWord[0:index]+sortedWord[index+1:len(sortedWord)]))
                    break
                    
        return count