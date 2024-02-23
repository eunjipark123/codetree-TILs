# n = 3

# for i in range(n):
#     for j in range(n):
#         print(i * n + j + 1, end = " ")
#     print()

# cnt = 1
# for i in range(2):
#     for j in range(4):
#         print(cnt, end = "")
#         cnt += 1
#     print()

n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        print(cnt, end = " ")
        cnt += 1
    print()