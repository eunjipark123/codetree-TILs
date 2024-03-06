n = int(input())

def sum_val(n):
    if n <= 2:
        return n

    return sum_val(n - 2) + n


print(sum_val(n))