class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        if(len(tokens) == 0 or power < tokens[0]):
            return 0
        left, right = 0,len(tokens)-1
        maxScore = score = 0
        while(left<=right):
            while(left <len(tokens) and power >= tokens[left]):
                power = power - tokens[left]
                left +=1 
                score += 1
                maxScore = max(maxScore, score)
            power += tokens[right]
            right-=1
            score-=1
        return maxScore