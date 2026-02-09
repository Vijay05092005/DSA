#Brute Force Approach
class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k = k % n
        a=[]
        for i in range(n-k,n):
            a.append(nums[i])
        for i in range(0,n-k):
            a.append(nums[i])
        for i in range(0,n):
            nums[i]=a[i]
#Optimal Approach
class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        a=[]
        if k!=0:
            nums[:]=nums[-k:]+nums[:-k]
