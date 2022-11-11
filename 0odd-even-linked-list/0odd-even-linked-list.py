# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    
    def printList(self, node):
        ptr = node
        while(ptr != None):
            print(ptr.val)
            ptr = ptr.next
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = ListNode(99)
        oddPtr = oddHead
        oddTail = None
        evenHead = ListNode(-99)
        evenPtr = evenHead
        ptr = head
        count = 1
        while(ptr!= None):
            
            if(count% 2 == 1):
                oddPtr.next = ptr
                oddPtr = oddPtr.next 
                oddTail = ptr
            else:
                evenPtr.next = ptr
                evenPtr = evenPtr.next
            
            
            ptr = ptr.next
            count += 1
            
        evenPtr.next = None
        self.printList(oddHead)
        self.printList(evenHead)
        # print(oddTail.val)
        if(oddTail == None):
            return None
        oddTail.next = evenHead.next
        return oddHead.next