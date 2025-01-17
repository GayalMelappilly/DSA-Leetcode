# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # node.val = node.next.val
        # node.next = node.next.next

        nxt = node.next

        while nxt:
            if nxt.next:
                node.val = nxt.val
                node = nxt
                nxt = nxt.next
            else:
                node.val = nxt.val
                node.next = None
                nxt = nxt.next 

        