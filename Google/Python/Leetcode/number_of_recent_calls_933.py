class RecentCounter:

    def __init__(self):
        self.q = deque()
        return None        

    def ping(self, t: int) -> int:

        s = t-3000
        count = 0
        self.q.append(t)
        for i in range(len(self.q)):
            if self.q[i] < s:
                count += 1
            if self.q[i] > s:
                break

        for i in range(count):
            self.q.popleft()

        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)