arr = list(map(int, input().split()))
sum_val = str(arr[0] + arr[1])

cnt = 0

for char in sum_val:
    if char == '1':
        cnt += 1

print(cnt)