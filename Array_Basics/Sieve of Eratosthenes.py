class Solution:
    def sieve(self, n):
        a=[1]*(n+1)
        a[0]=a[1]=0
        b=[]
        m=len(a)
        for i in range(2,int(n**0.5)+1):
            if a[i]==1:
                for j in range(i*i,m,i):
                    a[j]=0
        for i in range(2,m):
            if a[i]==1:
                b.append(i)
        return b
