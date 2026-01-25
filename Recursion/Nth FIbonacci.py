class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n==1:
            return 1
        if n==0:
            return 0
        return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
