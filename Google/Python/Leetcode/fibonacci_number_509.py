class Solution:
    def fib(self, n: int) -> int:

        prev_num = 0
        curr_num = 1

        if n == 0:
            return 0

        for i in range(n-1):
            curr_num, prev_num = prev_num + curr_num, curr_num

        return curr_num    