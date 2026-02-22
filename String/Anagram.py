class Solution:
    def areAnagrams(self, s1, s2):
        a={}
        for x in s1:
            a[x]=a.get(x,0)+1
        for x in s2:
            a[x]=a.get(x,0)-1
        for x in a.values():
            if x != 0:
                return False
        return True
