# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        arr = []

        arr.append(root)
        idx = 0
        leng = len(arr)

        while idx<len(arr):
            level = []
            for i in range(leng):
                node = arr[idx]
                if node:
                    level.append(node.val)
                    arr.append(node.left)
                    arr.append(node.right)
                idx+=1
            if level:
                res.append(level)
            leng = len(arr)-idx
        return res

        # Using queue

        # res = []
        # q = collections.deque()
        # q.append(root)

        # while q:
        #     leng = len(q)
        #     level = []
        #     for i in range(leng):
        #         node = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level)
        # return res        


            


