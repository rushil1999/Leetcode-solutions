# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        queue = [(root,0)]
        maxWidth = 0
        while(len(queue) > 0): 
            queueLength = len(queue)
            head = queue[0][1]
            for _ in range(queueLength):
                node, index = queue[0][0], queue[0][1]
                queue = queue[1:len(queue)]
                if(node.left != None):
                    queue.append((node.left, 2*index))
                if(node.right != None):
                    queue.append((node.right, (2*index)+1))
            print(index, head)
            maxWidth = max(maxWidth, index - head+1)
        return maxWidth
            