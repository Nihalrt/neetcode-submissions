# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length+=1
        
        nth_node = length - n
        curr = head
        prev = None

        for i in range(nth_node):
            prev = curr
            curr = curr.next
        
        if prev == None:
            return head.next
        else:
            prev.next = curr.next
        
        return head

            





        