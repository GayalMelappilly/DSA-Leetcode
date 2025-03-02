class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        return None


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        return None
        

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()