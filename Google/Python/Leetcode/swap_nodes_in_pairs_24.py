# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        curr = head
        head = ListNode(0, head)
        nxt = curr.next
        prev = head

        while nxt:
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt
            if curr.next is None:
                break
            prev = curr
            curr = curr.next
            nxt = curr.next
        return head.next
        

            
            
