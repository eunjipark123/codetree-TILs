arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

for i in arr:
    if i == 0:
        break
    cnt += 1
    sum_val += i

avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")