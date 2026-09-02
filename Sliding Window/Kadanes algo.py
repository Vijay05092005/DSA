class Solution:
    def maxSubarraySum(self, arr):
        cur=arr[0]
        tot=arr[0]
        for i in range(1,len(arr)):
            cur=max(arr[i],cur+arr[i])
            tot=max(tot,cur)
        return tot
