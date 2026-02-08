class Solution:
    def getSecondLargest(self, arr):
        l=arr[0]
        for i in arr:
            if i > l:
                l=i
        s=0
        for i in arr:
            if i < l and i > s:
                s=i
        if s!=0:
            return s
        return -1
