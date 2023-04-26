# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def printResult(self, head):
        ptr = head
        while(ptr):
            print(ptr.val)
            ptr = ptr.next
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = head
        
        while(current):
            prev = result
            while(prev.next and prev.next.val < current.val):
                prev = prev.next
            
            nextInOriginalList = current.next
            
            current.next = prev.next
            prev.next = current
            
            current = nextInOriginalList
            # print("Result")
            # self.printResult(result)
        return result.next