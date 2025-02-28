# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, num, total):
            if not node:
                return
            num = (num*10)+node.val
            dfs(node.left, num, total)
            dfs(node.right, num, total)
            if not node.left and not node.right:
                total[0] += num
            num = num-(node.val*10)
        
        total = [0]

        dfs(root, 0, total)

        return total[0]
        