# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = ""
    
    def func(self, parent, target):
        if(parent.val == target):
            return True
        if(parent.left != None):
            left = self.func(parent.left, target)
            if(left == True):
                
                self.path += "L"
                # print("Left here", path)
                return True
        
        if(parent.right != None):
            right = self.func(parent.right, target)
            if(right == True):
                self.path += "R"
                return True
        else: 
            return False
            
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        self.path = ""
        self.func(root, startValue)
        sourcePath = self.path[::-1]
        self.path = ""
        self.func(root, destValue)
        destinationPath = self.path[::-1]
        print(sourcePath, destinationPath)
        
        optimizedPath = ""
        sourcePathIndex = 0
        destinationPathIndex = 0
        
        while(sourcePathIndex < len(sourcePath) and destinationPathIndex < len(destinationPath)):
            if(sourcePath[sourcePathIndex] != destinationPath[destinationPathIndex]):
                break
            sourcePathIndex += 1
            destinationPathIndex += 1
        
        for index in range(sourcePathIndex, len(sourcePath)):
            optimizedPath += "U"
        # print(optmizedPath)
        optimizedPath += destinationPath[destinationPathIndex: len(destinationPath)]
        return optimizedPath