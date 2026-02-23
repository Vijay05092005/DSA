class Solution:
    def find(self, arr, x):
        i=0
        j=len(arr)-1
        if arr[0] > x or arr[-1] < x:
            return[-1,-1]
        f=l=-1
        while i<=j:
            mid=(i+j)//2
            if x==arr[mid]:
                f=mid
                j=mid-1
            elif x > arr[mid]:
                i=mid+1
            else:
                j=mid-1
        i=0
        j=len(arr)-1
        while i<=j:
            mid=(i+j)//2
            if x==arr[mid]:
                l=mid
                i=mid+1
            elif x > arr[mid]:
                i=mid+1
            else:
                j=mid-1
        return [f,l]
