n = int(input())
arr = list(map(int, input().split()))

cnt = 1
max_val = arr[0]
sec_val = arr[0]

for elem in arr[1:]:
    if elem > max_val:
        cnt = 1
        max_val = elem
        sec_val = max_val
    
    elif elem == max_val:
        cnt = 0
        max_val = sec_val

if cnt == 0:
    print(-1)
else:
    print(max_val)