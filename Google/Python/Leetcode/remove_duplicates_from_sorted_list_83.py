# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        prev = head
        curr = head.next

        while curr:
            if prev.val != curr.val:
                    prev.next = curr
                    prev = prev.next
                    curr = curr.next
            else:
                if not curr.next:
                    prev.next = None
                    return head
                curr = curr.next              
        return head        