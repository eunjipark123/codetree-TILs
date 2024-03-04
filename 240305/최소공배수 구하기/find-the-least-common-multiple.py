n, m = tuple(map(int, input().split()))

def last_common_multiple(n, m):
    num = m
    while True:
        if num % n == 0 and num % m == 0:
            print(num)
            break
        
        num += 1

last_common_multiple(n, m)