class Solution:
    def checkEqual(self, a, b) -> bool:
        c1={}
        if len(a)!=len(b):
            return False
        for x in a:
            c1[x]=c1.get(x,0)+1
        for y in b:
            if c1.get(y,0) > 0:
                c1[y]=c1.get(y)-1
                if c1.get(y,0) == 0:
                    del c1[y]
            else:
                return False
        return len(c1)==0
