n = int(input())

def n_sum_divide(n):
    sum_val = n * (n + 1) // 2 
    return sum_val // 10

print(n_sum_divide(n))