# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, node):
        temp = []
        if(node == None):
            return []
        left = self.helper(node.left)
        temp = left
        temp.append(node.val)
        right = self.helper(node.right)
        temp += right
        return temp
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.helper(root)[k-1]
        
