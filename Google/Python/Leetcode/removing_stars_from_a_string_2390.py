class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        # res = ''

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        # for c in stack:
        #     res += c
        # return res

        return "".join(stack)
        