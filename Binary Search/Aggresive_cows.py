class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()
        l=1
        h=arr[-1]-arr[0]
        sol=0
        while l <= h:
            mid=(l+h)//2
            cow=1
            prev=arr[0]
            for x in arr:
                if x-prev >= mid:
                    cow+=1
                    prev=x
            if cow >= k:
                sol=mid
                l=mid+1
            else:
                h=mid-1
        return sol
