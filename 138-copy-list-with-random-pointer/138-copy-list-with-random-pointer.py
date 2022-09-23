"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def helper(self, node, nodeMap):
        if(node == None):
            return None
        newNode = Node(node.val)
        nodeMap[node] = newNode
        if(node.next == None):
            newNode.next = None
        elif(node.next in nodeMap):
            newNode.next = nodeMap[node.next]
        else:
            newNode.next = self.helper(node.next, nodeMap)
        if(node.random == None):
            newNode.radom = None
        elif(node.random in nodeMap):
            newNode.random = nodeMap[node.random]
        else:
            newNode.random = self.helper(node.random, nodeMap)
        return newNode
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.helper(head, {})