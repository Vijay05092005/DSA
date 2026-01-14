n=4
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(0,(2*n)-(2*i-1)):
        print("*",end=" ")
    print()
