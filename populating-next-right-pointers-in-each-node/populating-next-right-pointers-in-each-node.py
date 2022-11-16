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
    def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if(node == None):
            return None
        if(node.left != None):
            node.left.next = node.right
        if(node.right != None and node.next != None):
            node.right.next = node.next.left
        self.connect(node.left)
        self.connect(node.right)
        return node
        
        
               
                
                
            