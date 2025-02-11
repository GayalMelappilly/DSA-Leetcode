# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        head = nodes.pop()

        for node in nodes[::-1]:
            if node.val >= head.val:
                node.next = head
                head = node
        return head




            

                    

                
        