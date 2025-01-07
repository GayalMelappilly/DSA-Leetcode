class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        leng = len(flowerbed)

        if flowerbed[leng-1]==0 and flowerbed[leng-2]==0:
            flowerbed[leng-1] = 1
            n -= 1

        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0] = 1
            n -= 1

        if n <= 0:
            return True

        for i in range(leng):
            if flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -= 1

        if n <= 0:
            return True


        return False                 
        
        