class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        memo = [[-1]* (l2) for _ in range(l1)]
        def recurse(p1, p2):
            if(p1 >= l1 or p2 >= l2):return 0
            if(memo[p1][p2] != -1):
                return memo[p1][p2]
            answer = 0
            if(text1[p1] == text2[p2]):
                answer = 1 + recurse(p1+1, p2+1)
            else:
                answer = max(recurse(p1+1, p2), recurse(p1, p2+1))
            memo[p1][p2] = answer
            return memo[p1][p2]
        return recurse(0,0)