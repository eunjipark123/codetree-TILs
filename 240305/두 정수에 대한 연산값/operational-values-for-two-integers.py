a, b = tuple(map(int, input().split()))

def calcuator(a, b):
    big_num = max(a, b)
    small_num = min(a, b)

    big_num += 25
    small_num *= 2

    return small_num, big_num

a, b = calcuator(a, b)
print(a, b)