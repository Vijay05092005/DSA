n=4
for i in range(1,n+1):
    for j in range(0,i-1):
        print(" ",end=" ")
    for k in range(n-i+1,0,-1):
        print(k,end=" ")
    print()
