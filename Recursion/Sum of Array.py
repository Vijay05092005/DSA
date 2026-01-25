a=[1,2,3,4,5,5]
n=len(a)
def suma(a,n,i):
    if i >= n:
        return 0
    return (a[i] + suma(a,n,i+1))
print(suma(a,n,0))
