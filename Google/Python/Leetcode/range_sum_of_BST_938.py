# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        curr_level = []
        curr_level.append(root)

        res = 0

        while curr_level:
            
            next_level = []

            for node in curr_level:
                if node.val>=low and node.val<=high:
                    res+=node.val
                if node.left and node.val>=high:
                    next_level.append(node.left)
                elif node.right and node.val<=low:    
                    next_level.append(node.right)
                else:
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)

            if not next_level:
                return res
            else:
                curr_level = next_level

        