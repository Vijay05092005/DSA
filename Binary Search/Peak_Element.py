class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        i=0
        j=n-1
        while i <= j:
            mid=(i+j)//2
            if mid==i or mid==j:
                if nums[i]<nums[j]:
                    return j
                else:
                    return i
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                i=mid+1
            else:
                j=mid-1
