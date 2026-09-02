class Solution:
    def intersect(self, a, b):
        a.sort()
        b.sort()
        i=j=0
        res=[]
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i+=1
            elif a[i] > b[j]:
                j+=1
            else:
                if not res or res[-1]!=a[i]:
                    res.append(a[i])
                i+=1
                j+=1
        return res
