# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        count = 1

        if not head or not head.next or k==0:
            return head

        while curr.next:
            curr = curr.next
            count += 1  

        if k == count:
            return head
 
        curr.next = head

        if k>count:
            k = k%count
        pos = count-k

        curr = head
        count = 1

        if pos == count:
            head = curr.next
            curr.next = None
            return head

        while curr.next:
            curr = curr.next
            count += 1
            if count == pos:
                head = curr.next
                curr.next = None
                return head