class Solution(object):
    def firstBadVersion(self, n):
        i=1
        j=n
        while i <= j:
            m=(i+j)//2
            if isBadVersion(m):
                j=m-1
            else:
                i=m+1
        return i
