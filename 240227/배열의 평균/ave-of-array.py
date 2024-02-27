arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 가로합
for i in range(2):
    avg_h = sum(arr[i]) / len(arr[i])
    print(f"{avg_h:.1f}", end = " ")
print()

# 세로합
for j in range(4):
    sum_val = 0
    cnt = 0
    for i in range(2):    
        sum_val += arr[i][j]
        cnt += 1
    avg_v = sum_val / cnt
    print(f"{avg_v:.1f}", end = " ")
print()

# 전체
sum_val = 0
cnt = 0
for i in range(2):
    sum_val += sum(arr[i])
    cnt += len(arr[i])
avg = sum_val / cnt
print(f"{avg:.1f}")
        










# for i in range(2):
#     avg_i = sum(arr[i]) / len(arr[i])
#     print(f"{avg_i:.1f}", end = " ")
# print()

# list_0 = []
# list_1 = []
# list_2 = []
# list_3 = []

# for i in range(2):
#     for j in range(4):
#         if j == 0:
#             list_0.append(arr[i][j])
#         elif j == 1:
#             list_1.append(arr[i][j])
#         elif j == 2:
#             list_2.append(arr[i][j])
#         else:
#             list_3.append(arr[i][j])

# arr_2 = [list_0, list_1, list_2, list_3]
# for j in range(4):
#     avg_j = sum(arr_2[j]) / len(arr_2[j])
#     print(f"{avg_j:.1f}", end = " ")
# print()

# sum_val = 0
# cnt_val = 0
# for i in range(2):
#     sum_val += sum(arr[i])
#     cnt_val += len(arr[i])

# avg = sum_val / cnt_val
# print(f"{avg:.1f}")