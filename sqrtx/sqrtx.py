class Solution:
    def mySqrt(self, x: int) -> int:
        if(x < 2):
            return x
        left, right = 1, x//2
        while(left<=right):
            middle = (left+right)//2
            print(left, middle, right)
            
            if(middle*middle == x ):
                return middle
            if(middle*middle > x):
                right = middle-1
            else:
                left = middle+1
        return right