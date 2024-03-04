n = int(input())
sum_val = 0

for _ in range(n):
    sum_val += int(input())


results = str(sum_val)
print(results[1:] + results[0])