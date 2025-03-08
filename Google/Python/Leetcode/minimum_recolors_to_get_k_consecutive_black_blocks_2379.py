class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        opr = 0
        res = k+1

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                opr += 1
            if r >= k-1:
                if opr < res:
                    res = opr
                if blocks[l] == 'W':
                    opr -= 1
                l += 1
            r += 1
            
        if res == k+1:
            if opr > 0:
                return opr
            return 0
        return res
                