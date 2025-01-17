# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head.next
        merged_curr = head
        s = 0

        while curr:
            if curr.val == 0:
                merged_curr.val = s
                if curr.next:
                    merged_curr = merged_curr.next
                else:
                    merged_curr.next = None    
                s = 0

            s += curr.val
            curr = curr.next

        return head  
        