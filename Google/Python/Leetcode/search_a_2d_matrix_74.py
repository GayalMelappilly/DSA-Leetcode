class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  

        leng = len(matrix[0])

        for arr in matrix:
            if target <= arr[leng-1] and target >= arr[0]:
                l, r = 0, leng-1
                while l<=r:
                    mid = (l+r)//2
                    if target == arr[mid]:
                        return True
                    elif target > arr[mid]:
                        l = mid+1
                    else:
                        r = mid-1
        return False        

            
                        

                            

        