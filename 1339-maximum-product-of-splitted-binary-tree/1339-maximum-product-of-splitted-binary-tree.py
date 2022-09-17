# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,node, subtreeSumList):
        mod = 1000000007
        if(node == None):
            return 0
        leftSum = self.helper(node.left, subtreeSumList)
        rightSum = self.helper(node.right,  subtreeSumList)
        totalSum = leftSum + rightSum + node.val
        if(leftSum > 0):
            subtreeSumList.append(leftSum)
        if(rightSum > 0):
            subtreeSumList.append(rightSum)
        return totalSum
        
    
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 1000000007
        subtreeSumList = []
        totalSum = self.helper(root, subtreeSumList)
        maxVal = 0
        for subtreeSum in subtreeSumList:
            prod = subtreeSum%mod * (totalSum%mod-subtreeSum%mod)
            maxVal = max(maxVal, prod)
        
        return maxVal%mod
        