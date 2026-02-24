class Solution:
    def findMin(self, arr):
        n=len(arr)
        i=0
        j=n-1
        while i <= j:
            mid=(i+j)//2
            if arr[i] <= arr[j]:
                return arr[i]
            prev=(mid-1+n)%n
            next=(mid+1)%n
            if arr[mid]<arr[next] and arr[mid] < arr[prev]:
                return arr[mid]
            elif arr[mid] < arr[j]:
                j=mid-1
            else:
                i=mid+1
