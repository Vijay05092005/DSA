#User function Template for python3
class Solution:
    def search(self, n, arr):
        i=0
        j=len(arr)-2
        while i <= j:
            mid=(i+j)//2
            if mid%2==0:
                if arr[mid]==arr[mid+1]:
                    i=mid+1
                else:
                    j=mid-1
            else:
                if arr[mid]==arr[mid-1]:
                    i=mid+1
                else:
                    j=mid-1
        return arr[i]
