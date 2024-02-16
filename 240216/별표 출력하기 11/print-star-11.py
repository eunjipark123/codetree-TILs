# 문제 풀이
n = int(input())

for i in range(2 * n + 1):
    for j in range(2 * n + 1):
        if i % 2 == 0 or j % 2 == 0:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()


#  n = 5
# 처음에 생각한 규칙 (첫행과 마지막행에 *을 출력하고, 그렇지 않은 행은 다르게)
# for i in range(n):
#     if i == 0 or i == (n - 1):
#         for _ in range(n):
#             print("*", end = "")
#     else:
#         for j in range(n):
#             if j == 0 or j == (n - 1):
#                 print("*", end = "")
#             else:
#                 print(" ", end = "")
#     print()

# for i in range(n):
#     if i == 0 or i == 4:
#         for _ in range(n):
#             print("*", end = " ")
#     else:
#         for j in range(n):
#             if j == 0 or j == 4:
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i in (0, 4) or j in (0, 4):
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()