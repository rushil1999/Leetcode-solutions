# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if(root== None):
            return None
        if(root.val > p.val):
            leftSuccessor = self.inorderSuccessor(root.left, p)
            return leftSuccessor if leftSuccessor!= None else root 
        elif(root.val <= p.val):
            return self.inorderSuccessor(root.right, p)
        