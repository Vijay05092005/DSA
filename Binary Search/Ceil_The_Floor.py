#Brute Force Approach
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        a=[]
        for i in range(-1,-len(arr)-1,-1):
            if arr[i] <= x:
                a.append(arr[i])
                break
        else:
            a.append(-1)
        for i in range(0,len(arr)):
            if arr[i] >= x:
                a.append(arr[i])
                break
        else:
            a.append(-1)
        return a
#Binary Search
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        a=-1
        b=-1
        if arr[-1] < x:
            pass
        if arr[0] > x:
            pass
        i=0
        j=len(arr)-1
        while i <= j:
            mid=(i+j)//2
            if arr[mid]==x:
                a=b=arr[mid]
                break
            elif arr[mid] > x:
                b=arr[mid]
                j=mid-1
            else:
                a=arr[mid]
                i=mid+1
        return [a,b]
