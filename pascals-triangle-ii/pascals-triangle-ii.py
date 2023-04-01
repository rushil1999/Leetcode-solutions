class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if(rowIndex == 0):
            return [1]
        if(rowIndex == 1):
            return [1,1]
        current = [1, 1]
        for i in range(2, rowIndex+1):
            temp = current[0]
            for j in range(1, len(current)):
                val = current[j]+temp
                temp = current[j]
                current[j] = val
            current.append(1)
        return current
            
                
            