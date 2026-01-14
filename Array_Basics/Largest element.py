class Solution:
    def largest(self, arr):
        # code here
        l=0
        for x in arr:
            if l < x:
                l=x
        return l
