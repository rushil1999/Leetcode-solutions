class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l1 = []
        heapq.heapify(l1)
        elementMap = {}
        for element in nums:
            elementMap[element] = 1 if element not in elementMap else elementMap[element]+1
        for element in elementMap:
            heapq.heappush(l1, (-1*elementMap[element], element))
    
        final = []
        while(len(final) < k):
            top = heapq.heappop(l1)
            final.append(top[1])
        return final