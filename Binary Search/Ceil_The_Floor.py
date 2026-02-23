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
