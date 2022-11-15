# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ptr = 0
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        indexMap = {}
        for index in range(len(inorder)):
            indexMap[inorder[index]] = index
            
        def helper(left, right):
            if(left > right):
                return None
            
            if(self.ptr >= len(preorder)):
                return None
            val = preorder[self.ptr]
            self.ptr += 1
            node = TreeNode(val)
            
            node.left = helper(left, indexMap[val] - 1)
            node.right = helper(indexMap[val]+1, right)
            
            return node
        
        return helper(0, len(preorder))