def div(n,i):
    if i > int(n**(0.5)):
        return
    if n%i==0:
        print(i)
        if n%(n//i)==0 and i!=(n//i):
            print(n//i)
    div(n,i+1)
div(33,1)
