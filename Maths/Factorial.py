class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        fac=1
        for i in range(2,n+1):
            fac=fac*i
        return fac
