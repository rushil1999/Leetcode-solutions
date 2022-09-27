# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def treeTraversal(self, node, visited):
        if(node == None):
            return '#'
        pathString = str(node.val)
        leftChildPathString = self.treeTraversal(node.left, visited)
        pathString += "(" + leftChildPathString + ")"
        rightChildPathString = self.treeTraversal(node.right, visited)
        pathString += "(" + rightChildPathString + ")"
        
        visited[pathString] = (node, 1) if pathString in visited else (node, 0)
        
        return pathString
        
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        final = []
        visited = {}
        self.treeTraversal(root, visited)
        for key in visited:
            if(visited[key][1] == 1):
                final.append(visited[key][0])
        return final