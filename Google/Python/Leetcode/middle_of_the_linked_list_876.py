# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # curr = head
        # nodes = 0
        # middle = 0

        # if not curr or not curr.next:
        #     return curr

        # while curr:
        #     curr = curr.next
        #     nodes += 1

        # curr = head    

        # middle = (nodes//2)

        # nodes = 1

        # while curr:
        #     curr = curr.next
        #     if nodes == middle:
        #         return curr
        #     nodes += 1   

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow    

                    
                   


        