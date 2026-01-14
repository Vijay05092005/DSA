class Solution:
    def isPrime(self, n):
        if n == 1:
            return False
        elif n==2 or n==3:
            return True
        else:
            for i in range(2,int(n**(1/2))+1):
                if n%i==0:
                    return False
            return True
