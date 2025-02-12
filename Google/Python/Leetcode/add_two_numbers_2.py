# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum_llist = ListNode()
        curr = sum_llist
        carry = 0

        while l1 or l2:
            v1 = v2 = num = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            val = v1+v2+carry
            if val>=10:
                num = val%10
                carry = val//10
                curr.next = ListNode(num)
                curr = curr.next
                continue
            curr.next = ListNode(val)
            curr = curr.next
            carry = 0
        if carry > 0:
            curr.next = ListNode(carry)
        
        return sum_llist.next


            


        


        
        