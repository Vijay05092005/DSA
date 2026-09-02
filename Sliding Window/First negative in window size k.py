class Solution:
    def firstNegInt(self, arr, k):
        q=[]
        j=0
        res=[]
        for i in range(len(arr)):
            if arr[i]<0:
                q.append(i)
            if q and q[0] <= i-k:
                q.pop(0)
            if i >= k-1:
                if q:
                    res.append(arr[q[0]])
                else:
                    res.append(0)
        return res
