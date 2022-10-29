# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def helper(node, count):
            if(node.next != None):
                [childNode, count] = helper(node.next, count)
            count += 1
            if(count == n+1):
                node.next = node.next.next
            return [node, count]
        
        [root, count] = helper(head, 0)
        if(count == n):
            return head.next
        return root
            
            