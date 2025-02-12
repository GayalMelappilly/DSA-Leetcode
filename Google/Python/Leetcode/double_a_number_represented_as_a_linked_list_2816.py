# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        carry = 0
        doubled_llist = 0

        while head:
            stack.append(head)
            head = head.next

        while stack:
            node = stack.pop()
            node.val = node.val*2
            node.val += carry
            carry = 0
            if node.val >= 10:
                carry = node.val//10
                node.val = node.val%10
            if doubled_llist == 0:
                doubled_llist = node
            else:
                node.next = doubled_llist
                doubled_llist = node
            if carry > 0:
                continue
        if carry > 0:
            node = ListNode(carry)
            node.next = doubled_llist
            return node
        return doubled_llist
                



        