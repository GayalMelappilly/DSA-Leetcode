# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        currLevel = [root]
        rightView = []

        while currLevel:

            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            rightMost = currLevel.pop()
            rightView.append(rightMost.val)

            if not nextLevel:
                return rightView
            else:
                currLevel = nextLevel    
            
        return rightView

        