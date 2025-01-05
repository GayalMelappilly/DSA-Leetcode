class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        arr = []

        for i in range(1,numRows+1):
            k = []
            for j in range(1,i+1):
                if j == 1 or j == i:
                    k.append(1)
                else: 
                    k.append(arr[i-2][j-1]+arr[i-2][j-2])
            arr.append(k) 

        return arr

        