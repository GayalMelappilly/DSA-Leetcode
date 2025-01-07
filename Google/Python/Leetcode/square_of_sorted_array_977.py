class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            leftSQ = nums[left] ** 2
            rightSQ = nums[right] ** 2
            if rightSQ >= leftSQ:
                result.append(rightSQ)
                right -= 1
            elif leftSQ >= rightSQ:
                result.append(leftSQ)
                left += 1

        return result[::-1]