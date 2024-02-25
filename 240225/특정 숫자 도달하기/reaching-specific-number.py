arr =list(map(int, input().split()))
sum_val = 0
cnt = 0
tests = []
if_true = False

for i in arr:
    if i >= 250:
        if_true = True
        break
    tests.append(i)

for i in tests:
    sum_val += i
    cnt += 1

avg = round(sum_val / cnt, 1)

print(sum_val, avg)