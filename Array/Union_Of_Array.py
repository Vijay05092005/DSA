class Solution:    
    def findUnion(self, a, b):
        i=0
        j=0
        k=[]
        a.sort()
        b.sort()
        while i < len(a) and j < len(b):
            if k and k[-1]==a[i]:
                i+=1
                continue
            if k and k[-1]==b[j]:
                j+=1
                continue
            if a[i]<b[j]:
                k.append(a[i])
                i+=1
            elif a[i]>b[j]:
                k.append(b[j])
                j+=1
            else:
                k.append(a[i])
                i+=1
                j+=1
        while i < len(a):
            if not k or k[-1]!=a[i]:
                k.append(a[i])
                i+=1
        while j < len(b):
            if not k or k[-1]!=b[j]:
                k.append(b[j])
                j+=1
        return k
