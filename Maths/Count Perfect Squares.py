#User function Template for python3

class Solution:
    def countSquares(self, n):
        count=0
        for i in range(1,n+1):
            if i**2 < n:
                count+=1
            else:
                break
        return count
# Another method
def countSquares(self, n):
        return int((n-1)**0.5)
