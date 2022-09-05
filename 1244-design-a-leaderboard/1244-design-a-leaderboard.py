import heapq
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap, score)
            if(len(heap) > K):
                heapq.heappop(heap)
        finalScore = 0
        while(heap):
            finalScore += heapq.heappop(heap)
        return finalScore

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)