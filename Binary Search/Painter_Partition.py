class Solution:
    def minTime (self, arr, k):
        l=max(arr)
        h=sum(arr)
        sol=l
        while l <= h:
            mid=(l+h)//2
            pa=1
            tot=0
            for x in arr:
                if tot+x <= mid:
                    tot+=x
                else:
                    pa+=1
                    tot=x
            if pa <=k:
                sol=mid
                h=mid-1
            else:
                l=mid+1
        return sol
