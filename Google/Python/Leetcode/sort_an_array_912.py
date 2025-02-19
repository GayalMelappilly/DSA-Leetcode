class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr: List[int]) -> List[int]:
            leng = len(arr)
            if leng <= 1:
                return arr
            mid = leng//2
            leftHalf = arr[0:mid]
            rightHalf = arr[mid:leng]
            return merge(mergeSort(leftHalf), mergeSort(rightHalf))
            

        def merge(leftHalf: List[int], rightHalf: List[int]) -> List[int]:
            leng_left = len(leftHalf)
            leng_right = len(rightHalf)
            joinedArray = [None]*(leng_left+leng_right)
            i = 0
            j = 0
            k = 0

            while i < leng_left and j < leng_right:
                if leftHalf[i]>=rightHalf[j]:
                    joinedArray[k] = rightHalf[j]
                    k += 1
                    j += 1
                else:
                    joinedArray[k] = leftHalf[i]
                    k += 1 
                    i += 1

            while i < leng_left:
                joinedArray[k] = leftHalf[i]
                i += 1
                k += 1
            while j < leng_right:
                joinedArray[k] = rightHalf[j]
                k += 1
                j += 1
            return joinedArray
                    

        return mergeSort(nums)
        