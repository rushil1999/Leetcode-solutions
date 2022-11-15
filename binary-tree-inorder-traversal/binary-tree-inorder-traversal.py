# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        def helper(node):
            if(node == None):
                return
            helper(node.left)
            final.append(node.val)
            helper(node.right)
        
        helper(root)
        return final