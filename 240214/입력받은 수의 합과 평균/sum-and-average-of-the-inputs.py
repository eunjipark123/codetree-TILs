n = int(input())
cnt = 0
sum_val = 0

for i in range(n):
    a = int(input())
    cnt += 1
    sum_val += a

avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")