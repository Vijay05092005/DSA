n=20300
def count(n):
    if n%10==n:
        if n%10==0:
            return 1
        else:
            return 0
    if n%10==0:
        return 1+count(n//10)
    else:
        return count(n//10)
print(count(n))
