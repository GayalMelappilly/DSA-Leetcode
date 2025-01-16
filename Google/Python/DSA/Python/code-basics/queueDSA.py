from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(25)
q.appendleft(65)

q.pop()


from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    