# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = [root]
        currentMin = float('inf')
        currentMinNode = None
        while(len(stack) > 0):
            node = stack[-1]
            stack = stack[:-1]
            if(node.val > p.val):
                if(node.val < currentMin):
                    currentMin = node.val
                    currentMinNode = node
            if(node.left != None):
                stack.append(node.left)
            if(node.right != None):
                stack.append(node.right)
        return currentMinNode
                