"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def func(self, node):
        ptr = node
        while((ptr and ptr.next != None) or (ptr and ptr.child!= None)):
            if(ptr.child != None):
                [childHead, childTail] = self.func(ptr.child)
                currentNext = ptr.next
                if(ptr.next != None):
                    currentNext.prev = childTail 
                childTail.next = currentNext
                ptr.next = childHead
                childHead.prev = ptr
                ptr.child = None
            else:
                ptr = ptr.next
        return [node, ptr]
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        [flattenedHead, flattenedTail] = self.func(head)
        return flattenedHead