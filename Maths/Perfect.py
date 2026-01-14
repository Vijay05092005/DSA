n=28
sum=1
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        sum+=i
        j=n//i
        if(j!=i):
            sum+=j
if sum==n:
    print("Perfect")
else:
    print("Not a perfect")
