n, m = tuple(map(int, input().split()))

def find_greatest_common_divisor(n, m):
    for i in range(m + 1, 0, -1):
        if m % i == 0 and n % i == 0:
            print(i)
            break

find_greatest_common_divisor(n, m)