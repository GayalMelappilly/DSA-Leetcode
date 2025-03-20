# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast = slow = head
        stack = []

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        while slow:
            nxt = slow.next
            slow.next = None
            stack.append(slow)
            slow = nxt

        curr = head    
        
        while len(stack) != 1:
            node = stack.pop()
            nxt = curr.next
            curr.next = node
            node.next = nxt
            curr = nxt         

        
        
    