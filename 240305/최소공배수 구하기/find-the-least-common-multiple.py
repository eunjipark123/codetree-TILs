n, m = tuple(map(int, input().split()))

def last_common_multiple(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    
    print(n * m // gcd)



last_common_multiple(n, m)