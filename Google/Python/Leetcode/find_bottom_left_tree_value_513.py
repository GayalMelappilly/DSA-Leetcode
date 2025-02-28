# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # Iterative

        currLevel = [root]

        while currLevel:
            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            if not nextLevel:
                return currLevel[0].val
            else:
                currLevel = nextLevel
        
        # Recursive

        # def dfs(node, depth, max_val, max_depth):
        #     if not node:
        #         return 0
        #     if not node.right and not node.left:
        #         if depth>max_depth[0]:
        #             max_depth[0] = depth
        #             max_val[0] = node.val
        #     left_node = dfs(node.left, depth + 1, max_val, max_depth )
        #     right_node = dfs(node.right, depth + 1, max_val, max_depth)
        
        # max_val = [root.val]
        # max_depth = [0]

        # dfs(root, 0, max_val, max_depth)

        # return max_val[0]
                
