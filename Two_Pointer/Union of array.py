class Solution:
    def findUnion(self, a, b):
        i=j=0
        res=[]
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if not res or a[i] != res[-1]:
                    res.append(a[i])
                i+=1
            elif a[i] > b[j]:
                if not res or b[j] != res[-1]:
                    res.append(b[j])
                j+=1
            else:
                if not res or a[i] != res[-1]:
                    res.append(a[i])
                i+=1
                j+=1
        while i < len(a):
            if not res or a[i] != res[-1]:
                res.append(a[i])
            i+=1
        while j < len(b):
            if not res or b[j] != res[-1]:
                res.append(b[j])
            j+=1
        return res
