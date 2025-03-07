class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        primes = []
        min_diff = right
        res = [-1, -1]

        if left < 3 and right > 2:
            return [2, 3]

        for i in range(left, right+1):
            if i%2 != 0:
                
                flag = False

                for j in range(2, i//2):
                    if i%j == 0:
                        flag = True
                        break

                if flag is False:
                    primes.append(i)

                if len(primes) == 2:

                    p1 = primes[0]
                    p2 = primes[1]

                    if p2 - p1 < min_diff:
                        min_diff = p2 - p1
                        res = [p1, p2]
                        if min_diff == 2:
                            return res
                    primes = [p2] 

        return res