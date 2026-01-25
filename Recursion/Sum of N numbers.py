def sum_n(n):
    if n == 0:          # base case
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))
