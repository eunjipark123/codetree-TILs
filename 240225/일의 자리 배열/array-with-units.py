arr = list(map(int, input().split()))

# print(arr)

# for i in range(2, 10):
#     arr.append((arr[i-2] + arr[i-1])%10)

# for i in arr:
#     print(i, end = " ")


arr_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr_list[0] = arr[0]
arr_list[1] = arr[1]

for i in range(2, 10):
    arr_list[i] = (arr_list[i - 1] + arr_list[i - 2]) % 10

for i in arr_list:
    print(i, end = " ")