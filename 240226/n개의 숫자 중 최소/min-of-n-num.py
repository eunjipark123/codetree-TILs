n = int(input())
arr = list(map(int, input().split()))
cnt = 0

min_val = arr[0]
for elem in arr[1:]:
    if elem < min_val:
        min_val = elem

for elem in arr:
    if elem == min_val:
        cnt += 1

print(min_val, cnt)

# arr = [11, 15, 12, 15, 13, 19]
# import sys

# min_val = sys.maxsize
# print(min_val)

# for elem in arr:
#     if elem < min_val:
#         min_val = elem

# print(min_val)


# min_val = arr[0]

# for elem in arr[1:]:
#     if elem < min_val:
#         min_val = elem

# print(min_val)