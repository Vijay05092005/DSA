class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        arr.sort()
        i=0
        j=1
        while j < len(arr):
            if i==j:
                j+=1
            elif arr[j]-arr[i] < x:
                j+=1
            elif arr[j]-arr[i] > x:
                i+=1
            else:
                return True
        return False
