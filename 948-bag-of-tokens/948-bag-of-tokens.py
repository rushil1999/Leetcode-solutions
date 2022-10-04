class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if(len(tokens) == 0 or power < tokens[0]):
            return 0
        deque = collections.deque(tokens)
        
        maxScore = score = 0
        while(deque):
            while( len(deque) > 0 and power >= deque[0]):
                top = deque.popleft()
                power = power - top
                score += 1
                maxScore = max(maxScore, score)
            if(len(deque) > 0):
                power += deque.pop()
                score-=1
        return maxScore