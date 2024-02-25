n = int(input())

arr = list(map(int, input().split()))
arr_2 = [i**2 for i in arr]
for i in arr_2:
    print(i, end = " ")


# list_ = [1, 9, 25, 49, 81]

# print([(list_[i] + list_[j]) for i in range(3) for j in range(3)])

# # arr = [1, 2, 3, 5]
# # print(arr)

# # # 첫 번째 방법
# # for i in range(4):
# #     arr[i] *= 2

# # print(arr)

# # # 두 번째 방법
# # arr_2 = []

# # for i in arr:
# #     arr_2.append(2 * i)

# # print(arr_2)

# # arr_list_compre = [i * 2 for i in arr if i % 4 == 0]
# # print(arr_list_compre)