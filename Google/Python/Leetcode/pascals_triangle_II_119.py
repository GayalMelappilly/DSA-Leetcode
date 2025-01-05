class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        arr = []

        for i in range(1,rowIndex+2):
            k = []
            for j in range(1,i+1):
                if j == 1 or j == i:
                    k.append(1)
                else: 
                    k.append(arr[j-1]+arr[j-2])
            if i == rowIndex+1:
                return k        
            arr = k