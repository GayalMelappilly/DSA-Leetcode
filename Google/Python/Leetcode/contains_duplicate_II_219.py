class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}

        for idx in range(len(nums)):
            if nums[idx] in hashset and abs(idx - hashset[nums[idx]]) <= k:
                return True

            hashset[nums[idx]] = idx
        
        return False