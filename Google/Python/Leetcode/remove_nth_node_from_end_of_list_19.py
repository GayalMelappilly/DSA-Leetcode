# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast, slow = head, head
        fast_count = 1
        slow_count = 1

        while fast:
            if fast.next:
                fast = fast.next.next
                if fast:
                    fast_count += 2
                else:
                    fast_count += 1    
            else:
                break    

        pos = (fast_count - n)

        while slow:
            if not slow:
                return None
            if pos == 1:
                slow.next = slow.next.next
                return head    
            slow = slow.next
            slow_count += 1
            if pos == 0:
                return slow
            if slow_count == pos:
                if slow.next:
                    slow.next = slow.next.next 
                else:
                    slow = None
                return head

        return head

        