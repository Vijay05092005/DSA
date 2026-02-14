#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        n=len(arr)
        a=[]
        k=0
        for i in range(n):
            if arr[i] < 0:
                a.append(arr[i])
            else:
                arr[k]=arr[i]
                k+=1
        l=0
        for i in range(k,n):
            arr[i]=a[l]
            l+=1
