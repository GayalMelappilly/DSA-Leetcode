class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, val):
            if not node:
                return False

            val += node.val

            if not node.left and not node.right:
                return val == targetSum

            return dfs(node.left, val) or dfs(node.right, val)
            
        return dfs(root, 0) 
            