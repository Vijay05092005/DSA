class Solution:
    def search(self, arr, key):
        i=0
        j=len(arr)-1
        while i <= j:
            mid=(i+j)//2
            if arr[mid]==key:
                return mid
            if arr[mid] >= arr[i]:
                if key < arr[mid] and key >= arr[i]:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if key > arr[mid] and key <= arr[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1
