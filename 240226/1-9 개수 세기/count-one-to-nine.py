n = int(input())

arr = list(map(int, input().split()))
arr_cnt = [0] * 10

for elem in arr:
    arr_cnt[elem] += 1

for i in arr_cnt[1:]:
    print(i)
# arr = [1, 5, 2, 2, 1, 6, 3, 1, 3, 4]

# for i in range(1, 7):
#     cnt = 0
#     for elem in arr:
#         if elem == i:
#             cnt += 1
        
#     print(f"숫자 {i} - {cnt}번")

# count_arr = [0] * 7

# for elem in arr:
#     count_arr[elem] += 1

# for i in range(1, 7):
#     print(f"숫자 {i} - {count_arr[i]}번")