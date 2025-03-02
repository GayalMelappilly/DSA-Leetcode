class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = collections.deque()

        res = []
        left = 0

        for right, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if (right+1) >= k:
                res.append(nums[q[0]])
                left += 1
        return res



        
            

            
        





        