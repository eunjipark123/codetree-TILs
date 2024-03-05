a, b = tuple(map(int, input().split()))

def is_multiple3(n):
    return n % 3 == 0

def is_in369(n):
    return "3" in str(n) or "6" in str(n) or "9" in str(n)

def is_369(a, b):
    cnt = 0
    arr = []
    for i in range(a, b + 1):
        if is_multiple3(i) or is_in369(i):
            arr.append(i) 
            cnt += 1

    return cnt

print(is_369(a, b))

    
        







# def all_different(n):
#     return (n % 10) != (n // 10)

# def is_magic_number(n):
#     return n % 3 != 0 and all_different(n)

    
# cnt = 0
# for i in range(10, 100):
#     if is_magic_number(i):
#         cnt += 1

# print(cnt)