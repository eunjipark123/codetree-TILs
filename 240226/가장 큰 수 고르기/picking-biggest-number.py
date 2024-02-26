arr = list(map(int, input().split()))
max_val = arr[0]

for elem in arr:
    if elem > max_val:
        max_val = elem

print(max_val)


# lists = [1, 5, 2, 5, 3, 9]
# lists = [-1, -5, -2, -5, -3, -9]

# # max_lists = 0
# # for i in lists:
# #     if i >= max_lists:
# #         max_lists = i

# # print(max_lists)


# # max_lists = lists[0]

# # for i in lists[1:]:
# #     if i > max_lists:
# #         max_lists = i 
    
# # print(max_lists)

# import sys

# max_val = -sys.maxsize 
# print(max_val)

# for i in lists:
#     if i > max_val:
#         max_val = i
    
# print(max_val)