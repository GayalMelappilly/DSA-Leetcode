class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr)<3:
            return False

        prev_num = -1
        increasing = True if arr[1]>arr[0] else False

        for num in arr:
            if prev_num == num:
                return False
            if increasing is True:
                if num<=prev_num:
                    increasing = False
            else:
                if num>=prev_num:
                    return False        
            prev_num = num        
        
        if increasing is False:
            return True           
        else:
            return False
        