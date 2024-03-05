a, b = tuple(map(int, input().split()))

def return_power(a, b):
#     return a**b



    cnt = 1
    for _ in range(b):
        cnt *= a
    
    return cnt


print(return_power(a, b))