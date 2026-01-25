n=34982
def sumc(n):
    if n==0:
        return 0
    return (n%10)+sumc(n//10)
print(sumc(n))
