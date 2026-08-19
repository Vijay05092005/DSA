class Solution(object):
    def splitArray(self, nums, k):
        l=max(nums)
        h=sum(nums)
        sol=l
        while l <= h:
            mid=(l+h)//2
            s=0
            sub=1
            for x in nums:
                if x+s <= mid:
                    s+=x
                else:
                    sub+=1
                    s=x
            if sub <= k:
                sol=mid
                h=mid-1
            else:
                l=mid+1
        return sol
