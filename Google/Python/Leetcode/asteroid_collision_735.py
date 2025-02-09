class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        count = 0
        n = 0

        while n < len(asteroids):
            if asteroids[n] > 0:
                stack.append(asteroids[n])
                count += 1
                n += 1
                continue
            if stack and count > 0:
                if stack[-1] < abs(asteroids[n]):
                    stack.pop()
                    count -= 1
                    if stack and count>0:
                        continue
                    else:
                        stack.append(asteroids[n])
                        n += 1
                        continue
                elif stack[-1] == abs(asteroids[n]):
                    stack.pop()
                    count -= 1
            else:
                stack.append(asteroids[n])
            n += 1
            
        return stack        