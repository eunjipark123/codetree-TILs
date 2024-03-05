a, b = tuple(map(int, input().split()))

def is_perfect_num(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if (n % 3 == 0) and (n % 9 != 0):
        return False
    return True

def calculate_perfect_num(a, b):
    cnt = 0

    for i in range(a, b + 1):
        if is_perfect_num(i):
            cnt += 1
    
    return cnt

print(calculate_perfect_num(a, b))