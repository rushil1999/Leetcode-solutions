# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def helper(node1, node2, carry):
            if(node1 == None and node2 == None):
                if(carry == 0):
                    return None
                else:
                    return ListNode(carry)
            
            val1 = node1.val if node1 != None else 0
            val2 = node2.val if node2 != None else 0
            
            sumVal = val1 + val2 + carry
            sigVal = sumVal%10
            newCarry = sumVal//10
            node = ListNode(sigVal)
            nextNode1 = node1.next if node1 != None else None
            nextNode2 = node2.next if node2 != None else None
            
            childNode = helper(nextNode1, nextNode2, newCarry)
            node.next = childNode
            return node
        
        final = helper(l1, l2, 0)
        print(final.val)
        return final
            