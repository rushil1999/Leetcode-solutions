"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def getRightForChild(self, node):
        if(node == None):
            return None
        if(node.left != None):
            return node.left
        if(node.right != None):
            return node.right
        else:
            return self.getRightForChild(node.next)
    
    def connect(self, node: 'Node') -> 'Node':
        if(node == None):
            return None
        # print(node.val)
        childNext = self.getRightForChild(node.next)
        print(node.val, node.next, childNext)
        if(node.right != None):
            node.right.next = childNext
            self.connect(node.right)
        if(node.left != None):
            if(node.right != None):
                node.left.next = node.right
            else:
                node.left.next = childNext
            self.connect(node.left) 
        return node
            
        
       
        