from itertools import zip_longest
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        result1 = []
        result2 = []
        dummy = ListNode(0, None)
        last = dummy

        while curr:
            result1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            result2.append(curr.val)
            curr = curr.next
        result = []
        carry = 0

        for x,y in zip_longest(result1, result2, fillvalue=0):
            total = x + y + carry
            result.append(total % 10)
            carry = total // 10
        
        if carry > 0:
            result.append(carry)

        for num in result:
            last.next = ListNode(num)
            last = last.next
        return dummy.next

        
            

        

        
        