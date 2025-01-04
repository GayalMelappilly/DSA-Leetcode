class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements_set = set()

        for num in nums:
            if num in elements_set:
                return True
            else:
                elements_set.add(num)
        return False