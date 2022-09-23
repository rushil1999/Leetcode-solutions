class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        l1 = []
        heapq.heapify(l1)
        wordMap = {}
        for word in words:
            wordMap[word] = 1 if word not in wordMap else wordMap[word]+1

        for word in wordMap:
            heapq.heappush(l1, ((-1*wordMap[word]), word))
        print(list(l1))
        final = []
        while(len(final) < k):
            top = heapq.heappop(l1)
            final.append(top[1])
        return final
                    
                    