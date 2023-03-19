class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            temp = []
            for index in range(1, len(ans[i-1])):
                val = ans[i-1][index] + ans[i-1][index-1]
                temp.append(val)
            temp = [1]+ temp + [1]
            ans.append(temp)
           
        return ans
                