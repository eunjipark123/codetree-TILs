arr_cnt = [0] * 4

for _ in range(3):
    arr = input().split()
    if arr[0] == 'Y' and int(arr[1]) >= 37:
        arr_cnt[0] += 1
    elif arr[0] == 'N' and int(arr[1]) >= 37:
        arr_cnt[1] += 1
    elif arr[0] == 'Y' and int(arr[1]) < 37:
        arr_cnt[2] += 1
    else:
        arr_cnt[3] += 1


for i in arr_cnt:
    print(i, end = " ")

if arr_cnt[0] >= 2:
    print('E')