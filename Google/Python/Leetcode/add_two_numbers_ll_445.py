# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1 = []
        stack2 = []
        carry = 0
        prev = None
        curr = ListNode()
        
        while l1 or l2:
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
        
        len1 = len(stack1)-1
        len2 = len(stack2)-1

        largest = len1 if len1>=len2 else len2

        for i in range(largest+1):  
            if len1-i > -1:
                val = stack1[len1-i]
            if len2-i > -1:    
                val = val + stack2[len2-i]
            val = val+carry
            if val >= 10:
                carry = val//10
                val = val%10
                curr, prev = self.rev_linked_list(val, prev, curr)
                if largest-i > 0:
                    val = 0
                    continue
                else:
                    val = carry  
            curr, prev = self.rev_linked_list(val, prev, curr)  
            carry = 0
            val = 0
        return prev
    
    def rev_linked_list(self, val, prev: Optional[ListNode], curr: Optional[ListNode])-> Optional[ListNode]:
        curr.val = val
        nxt = ListNode()
        curr.next = prev
        prev = curr
        curr = nxt
        return curr,prev