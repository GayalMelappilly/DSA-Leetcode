class Solution:
    def trap(self, height: List[int]) -> int:
        
        leng = len(height)

        l, r = 0, leng-1

        left_top, right_top = height[l], height[r]

        units = 0

        while l<r:
            if left_top<right_top:
                l += 1
                if height[l]>left_top:
                    left_top = height[l]
                units += left_top-height[l]
            else:
                r -= 1
                if height[r]>right_top:
                    right_top = height[r]
                units += right_top-height[r]    
        return units