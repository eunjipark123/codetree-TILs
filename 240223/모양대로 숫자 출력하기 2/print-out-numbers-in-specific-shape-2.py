n = int(input())
# cnt = 1

# for _ in range(n):
#     for _ in range(n):
#         print(2 * cnt, end = " ")
#         cnt += 1
#         if cnt >= 5:
#             cnt = 1
#     print()

cnt = 2

for _ in range(n):
    for _ in range(n):
        print(cnt, end = " ")
        cnt += 2
        if cnt == 10:
            cnt = 2
    print()