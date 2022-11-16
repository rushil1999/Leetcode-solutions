# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Inorder traversal of BST gives a sorted array
    
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
        # return self.helper(root)[k-1]
        l1= []
        heapq.heapify(l1)
        stack = [root]
        while(len(stack) > 0):
            top = stack[-1]
            stack = stack[0:len(stack)-1]
            heapq.heappush(l1, top.val)
            if(top.left != None):
                stack.append(top.left)
            if(top.right!= None):
                stack.append(top.right)
        
        count = 0
        while(count < k):
            top = heapq.heappop(l1)
            count += 1
            
        return top

