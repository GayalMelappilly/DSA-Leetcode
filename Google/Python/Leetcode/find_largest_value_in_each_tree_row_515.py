# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        curr_level = [root]
        res = [root.val]
        
        while curr_level:

            next_level = []
            highest = -2147483648

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                    if node.left.val > highest: highest = node.left.val
                if node.right:
                    next_level.append(node.right)
                    if node.right.val > highest: highest = node.right.val

            if not next_level:
                return res
            else:
                curr_level = next_level
                
            res.append(highest)
            highest = -2147483648



