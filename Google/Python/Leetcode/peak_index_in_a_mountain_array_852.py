class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        mid = len(arr)//2
        peak = 0

        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid   

        counter = 1 if arr[mid+1]>arr[mid-1] else -1 

        while mid != 0 or mid != len(arr)-1:
            if arr[mid+counter]>arr[peak]:
                peak = mid+counter
            else:
                return peak    
            mid+=counter               
            
        