class Solution:
    def findKRotation(self, arr):
        low=0
        high=len(arr)-1
        while low <= high:
            if arr[low] < arr[high]:
                return low
            mid=(low+high)//2
            next=(mid+1)%len(arr)
            prev=(mid-1+len(arr))%len(arr)
            if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
                return mid
            elif arr[mid] <= arr[high]:
                high=mid-1
            else:
                low=mid+1
