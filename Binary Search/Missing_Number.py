class Solution:
    def missingNum(self, arr):
        i=0
        j=len(arr)-1
        arr.sort()
        while i <= j:
            mid=(i+j)//2
            if arr[mid] == mid+1:
                i = mid+1
            else:
                j=mid-1
        return i+1
