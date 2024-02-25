arr = list(map(int, input().split()))
# n = len(arr)
new_arr = []
# for i in range(n):
#     if arr[i] == 0:
#         break
#     new_arr.append(arr[i])

# for i in new_arr:
#     if i % 2 == 1:
#         print(i + 3, end = " ")
#     else:
#         print(i // 2, end = " ")


# for i in arr:
#     if i == 0:
#         break
#     if i % 2 == 1:
#         print(i + 3, end = " ")
#     else:
#         print(i // 2, end = " ")


for i in range(100):
    if arr[i] == 0:
        break
    if arr[i] % 2 == 0:
        new_arr.append(arr[i] // 2)
    else:
        new_arr.append(arr[i] + 3)

for elem in new_arr:
    print(elem, end = " ")