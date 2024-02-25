arr = list(map(int, input().split()))
arr_cnt = [0] * 10

for i in range(100):
    if arr[i] == 0:
        break
    
    arr_cnt[arr[i] // 10] += 1


for i in range(1, 10):
    print(f"{i} - {arr_cnt[i]}")