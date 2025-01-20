# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
            
        even = head.next

        odd_curr = head
        even_curr = even

        while even_curr and even_curr.next:
            odd_curr.next = even_curr.next
            odd_curr = odd_curr.next

            even_curr.next = even_curr.next.next
            even_curr = even_curr.next

        odd_curr.next = even

        return head
        