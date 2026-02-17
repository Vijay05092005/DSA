class Solution:
    def findDuplicates(self, arr):
        a=[]
        for i in range(len(arr)):
            s=abs(arr[i])-1
            if arr[s] < 0:
                a.append(abs(arr[i]))
            else:
                arr[s]=-arr[s]
        return a
