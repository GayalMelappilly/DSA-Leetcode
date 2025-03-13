# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head
        max_sum = 0
        stack = []

        while slow:
            if fast:
                fast = fast.next.next
                stack.append(slow.val)
            else:
                val = stack.pop()
                if val + slow.val > max_sum:
                    max_sum = val + slow.val
            slow = slow.next
                
        return max_sum
        

        