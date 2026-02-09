class Solution:
    def rotate(self, arr):
        temp=arr[-1]
        for i in range(-1,-len(arr),-1):
            arr[i]=arr[i-1]
        arr[0]=temp
