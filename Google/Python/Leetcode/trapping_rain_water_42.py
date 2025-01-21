class Solution:
    def trap(self, height: List[int]) -> int:
        
        leng = len(height)

        l, r = 0, leng-1

        left_top, right_top = height[l], height[r]

        units = 0

        while l<r:
            if left_top<right_top:
                if height[l]>left_top:
                    left_top = height[l]
                units += left_top-height[l]
                l += 1
            else:
                if height[r]>right_top:
                    right_top = height[r]
                units += right_top-height[r]    
                r -= 1
        return units