# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right or not head:
            return head

        curr = head
        prev = None
        pos = 1
        if pos == left:
            end_point = curr

        while curr:
            if pos + 1 == left:
                end_point = curr
            if pos >= left and pos <= right:
                if pos == left:
                    start = curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            else:
                if pos > right:
                    pos = curr
                    break
                curr = curr.next 
            pos += 1 

        end_point.next = prev
        start.next = curr

        if left == 1:
            return prev

        return head     
