a=[1,2,3,4,5,2]
n=len(a)
def suma(a,n,i):
    if i >= n-1:
        return True
    if a[i] > a[i+1]:
        return False
    return suma(a,n,i+1)
print(suma(a,n,0))
