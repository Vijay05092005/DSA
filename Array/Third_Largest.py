class Solution:
    def thirdLargest(self,arr):
        f=s=t=-1
        if len(arr) < 3:
            return -1
        for a in arr:
            if a >= f:
                t=s
                s=f
                f=a
            elif a >= s:
                t=s
                s=a
            elif a>=t:
                t=a
        return t
