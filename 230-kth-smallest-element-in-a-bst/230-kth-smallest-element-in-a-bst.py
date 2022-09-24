# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, node, heap):
        if(node == None):
            return None
        heapq.heappush(heap, node.val)
        self.helper(node.left, heap)
        self.helper(node.right, heap)
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l1 = []
        heapq.heapify(l1)
        self.helper(root, l1)
        count = 0
        top = 0
        while(count < k):
            top = heapq.heappop(l1)
            count+=1
        return top