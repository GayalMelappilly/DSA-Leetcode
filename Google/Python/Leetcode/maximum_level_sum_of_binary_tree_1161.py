# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = collections.deque()

        q.append(root)

        max_val = [1, root.val]
        level = 0

        while q:
            qlen = len(q)
            level_sum = 0
            level += 1
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:    
                        q.append(node.right)
                    if node.val:
                        level_sum += node.val

            if level_sum > max_val[1]:
                max_val = [level, level_sum]
            
        return max_val[0]

            
            
        