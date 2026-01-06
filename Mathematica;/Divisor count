class Solution:
    def countDivisors(self, n):
        c=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                if i%3==0:
                    c+=1
                j=n//i
                if j!=i and j%3==0:
                    c+=1
        return c
