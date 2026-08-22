class Solution:
    def nextLargerElement(self, arr):
        stack=[]
        sol=[-1]*(len(arr))
        for i in range(-1,-len(arr)-1,-1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            if stack :
                sol[i]=stack[-1]
            stack.append(arr[i])
        return sol
