arr = list(map(int, input().split()))

# 첫 번째 방법
sum_val_even = 0
sum_val_three = 0
cnt_three = 0
# even = []
# three = []
n = len(arr)

for i in range(1, n, 2):
    sum_val_even += arr[i]
    # even.append(arr[i])

for j in range(2, n, 3):
    sum_val_three += arr[j]
    cnt_three += 1
    # three.append(arr[j])

avg_three = sum_val_three / cnt_three

print(f"{sum_val_even} {avg_three:.1f}")
# print(even)
# print(three)

# arr = list(map(int, input().split()))
# # sum_val = 0
# # n = len(arr)

# # for i in range(0, n, 2):
# #     sum_val += arr[i]

# # print(sum_val)

# print(sum(arr[::2]))