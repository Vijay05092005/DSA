l=15
r=25
a=[1]*(r+1)
a[0]=a[1]=0
for i in range(2,int(r**0.5)+1):
    if a[i]==1:
        for j in range(i*i,r+1,i):
            a[j]=0
sum=0
for i in range(l,r+1):
    if a[i]==1:
        sum=sum+i
print(sum)
