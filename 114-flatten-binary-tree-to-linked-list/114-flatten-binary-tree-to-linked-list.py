# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, node):
        if(node == None):
            return [None, None]
        [leftHead, leftTail] = self.helper(node.left)
        [rightHead, rightTail] = self.helper(node.right)
        
        if(leftHead == None and rightHead == None):
            return [node, node]
        
        if(leftHead != None and rightHead != None):
            node.right = leftHead
            leftTail.right = rightHead
            rightTail.next = None
        elif(rightHead == None and leftHead != None):
            node.right = leftHead
            rightTail = leftTail
        node.left = None
        
        return [node, rightTail]
        
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        prev=None
        def rec(root):
            if root == None:
                return
            nonlocal prev
            rec(root.right)
            rec(root.left)

            root . right = prev
            root . left = None
            prev = root
        rec(root)
        