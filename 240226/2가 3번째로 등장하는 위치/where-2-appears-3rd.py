n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if cnt == 3:
        print(i)
        break
    if arr[i] != 2:
        continue
    else:
        cnt += 1