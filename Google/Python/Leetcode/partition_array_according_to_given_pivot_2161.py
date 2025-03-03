class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        big = []
        small = []
        pivot_count = 0

        res = []

        for num in nums:
            if num > pivot:
                big.append(num)
            elif num == pivot:
                pivot_count += 1  
            else:
                small.append(num)   

        return small + [pivot]*pivot_count + big
        
        
             