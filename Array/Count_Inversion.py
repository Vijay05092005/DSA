class Solution:
    def inversionCount(self, arr):
        return self.mergesort(0,len(arr)-1,arr)
    
    def mergesort(self,low,high,arr):
        inv=0
        if low < high :
            mid=(low+high)//2
            inv+=self.mergesort(low,mid,arr)
            inv+=self.mergesort(mid+1,high,arr)
            inv+=self.merge(low,mid,high,arr)
        return inv
    
    def merge(self,low,mid,high,arr):
        left=low
        right=mid+1
        inv=0
        temp=[]
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                inv+=(mid-left+1)
                right+=1
        while left <= mid:
            temp.append(arr[left])
            left+=1
        while right <= high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        return inv
