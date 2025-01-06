class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        i = 0
        j = 0

        while i <len(nums1) or j < len(nums2):
            if i == len(nums1):
                result.append(nums2[j])
                j += 1
            elif j == len(nums2):
                result.append(nums1[i])
                i += 1
            else:
                if nums1[i][0] == nums2[j][0]:
                    result.append([nums1[i][0],nums1[i][1] + nums2[j][1]])
                    j += 1
                    i += 1
                elif nums1[i][0] < nums2[j][0]:
                    result.append(nums1[i])
                    i+=1
                else:
                    result.append(nums2[j])
                    j+=1
        return result