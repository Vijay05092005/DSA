class Solution:
    def sort012(self, arr):
        l=m=0
        h=len(arr)-1
        while m <= h:
            if arr[m]==1:
                m+=1
            elif arr[m]==0:
                arr[m],arr[l]=arr[l],arr[m]
                l+=1
                m+=1
            else:
                arr[h],arr[m]=arr[m],arr[h]
                h-=1
