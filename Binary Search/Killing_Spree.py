class Solution:
    def killinSpree (self, n):
        l=1
        h=int(n**0.5)
        a=0
        while l <= h:
            m=(l+h)//2
            kill=(m*(m+1)*((2*m)+1))//6
            if kill > n:
                h=m-1
            else:
                a=m
                l=m+1
        return a
