n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

def caculator(n, m):
    sum_val = 0
    mlist = []
    while m >= 1:
        mlist.append(m)
        sum_val += a[m-1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return sum_val

print(caculator(n, m))