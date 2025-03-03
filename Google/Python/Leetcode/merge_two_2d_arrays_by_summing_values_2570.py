class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        l1 = len(nums1)
        l2 = len(nums2)

        res = []
        i = 0
        j = 0

        while i < l1 or j < l2:
            if i < l1:
                id1 = nums1[i][0]
                val1 = nums1[i][1]
            else:
                for k in range(j, l2):
                    res.append(nums2[k])
                return res

            if j < l2:
                id2 = nums2[j][0]
                val2 = nums2[j][1]
            else:
                for k in range(i, l1):
                    res.append(nums1[k])
                return res
            
            if id1 == id2:
                res.append([id1, val1+val2])
                i += 1
                j += 1
            elif id1 > id2 or id1 == -1:
                res.append([id2, val2])
                j += 1
            elif id1 < id2 or id2 == -1:
                res.append([id1, val1]) 
                i += 1  
        return res

        