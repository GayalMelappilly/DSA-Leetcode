# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leafNodes1 = []
        leafNodes2 = []

        def dfs(node, leafNodes):
            if not node:
                return
            if node.left == None and node.right == None:
                leafNodes.append(node.val)
            dfs(node.left, leafNodes)
            dfs(node.right, leafNodes)
        
        dfs(root1, leafNodes1)
        dfs(root2, leafNodes2)

        return leafNodes1 == leafNodes2
        