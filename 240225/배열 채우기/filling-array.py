arr = list(map(int, input().split()))
arr_lists = []

# for i in arr:
#     if i == 0:
#         break
#     else:
#         arr_lists.append(i)

# for i in arr_lists[::-1]:
#     print(i, end = " ")

cnt = 0
for el in arr:
    if el == 0:
        break
    cnt += 1

# print(cnt)
for i in range(cnt -1, -1, -1):
    print(arr[i], end = " ")