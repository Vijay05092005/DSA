#User function Template for python3
class Solution:
    def sumOfTheSeries (self, n):
        series=0
        su=0
        for i in range(1,n+1):
            su+=i
            series+=su
        return series
