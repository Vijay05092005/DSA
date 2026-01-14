#User function Template for python3
class Solution:
    def sumOfTheSeries (self, n):
        series=0
        s=0
        for i in range(1,2*n,2):
            s+=i
            series+=s
        return series
