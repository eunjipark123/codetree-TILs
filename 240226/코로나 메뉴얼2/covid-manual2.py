arr_cnt = [0] * 4

for _ in range(3):
    s, t = input().split()
    t = int(t)

    if t >= 37 and s == 'Y':
        type_num = 0;
    elif t >= 37 and s == 'N':
        type_num = 1;
    elif s == 'Y':
        type_num = 2;
    else:
        type_num = 3;

    arr_cnt[type_num] += 1

for i in range(4):
    print(arr_cnt[i], end = " ")

if arr_cnt[0] >= 2:
    print("E")
# for _ in range(3):
#     arr = input().split()
#     if arr[0] == 'Y' and int(arr[1]) >= 37:
#         arr_cnt[0] += 1
#     elif arr[0] == 'N' and int(arr[1]) >= 37:
#         arr_cnt[1] += 1
#     elif arr[0] == 'Y' and int(arr[1]) < 37:
#         arr_cnt[2] += 1
#     else:
#         arr_cnt[3] += 1


# for i in arr_cnt:
#     print(i, end = " ")

# if arr_cnt[0] >= 2:
#     print('E')