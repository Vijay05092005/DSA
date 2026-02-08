def merge(l,m,h,arr):
    r=[]
    i=l
    j=m+1
    while i <= m and j <= h:
        if arr[i] <= arr[j]:
            r.append(arr[i])
            i+=1
        elif arr[j] <= arr[i]:
            r.append(arr[j])
            j+=1
    while i <= m:
        r.append(arr[i])
        i+=1
    while j <= h:
        r.append(arr[j])
        j+=1
    k=l
    for x in r:
        arr[k]=x
        k+=1
def mergesort(l,h,arr):
    if l < h:
        mid=(l+h)//2
        mergesort(l,mid,arr)
        mergesort(mid+1,h,arr)
        merge(l,mid,h,arr)
arr=[34,23,1,45,67,5,43,22,45,21,3,7,98,7]
mergesort(0,len(arr)-1,arr)
print(arr)
