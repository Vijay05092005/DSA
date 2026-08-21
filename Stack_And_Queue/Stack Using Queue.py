from collections import deque
class myStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    def pop(self):
        if len(self.q) > 0:
            return self.q.popleft()
        return -1
    def top(self):
        if len(self.q) > 0:
            return self.q[0]
        return -1
    def size(self):
        return len(self.q)
