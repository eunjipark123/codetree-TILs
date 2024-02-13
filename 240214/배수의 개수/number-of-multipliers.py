cnt_3 = 0
cnt_5 = 0

for _ in range(10):
    n = int(input())
    if n % 3 == 0 and n % 5 == 0:
        cnt_3 += 1
        cnt_5 += 1
    elif n % 3 == 0:
        cnt_3 += 1
    elif n % 5 == 0:
        cnt_5 += 1

print(cnt_3, cnt_5)