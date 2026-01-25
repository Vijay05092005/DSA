n=20300
def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
print(count(n))
