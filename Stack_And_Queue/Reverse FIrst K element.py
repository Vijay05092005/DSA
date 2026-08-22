class Solution:
    def reverseFirstK(self, q, k):
        stack=[]
        if k > len(q):
            return q
        for i in range(k):
            stack.append(q.popleft())
            
        for i in range(k):
            q.append(stack.pop())
        for i in range(len(q)-k):
            x=q.popleft()
            q.append(x)
        return q
