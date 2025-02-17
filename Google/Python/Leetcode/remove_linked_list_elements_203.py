# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            if curr.val == val:
                if prev is None:
                    head = head.next
                    curr = head
                    continue
                prev.next = nxt
                curr = nxt
            else:
                prev = curr
                curr = nxt
        return head