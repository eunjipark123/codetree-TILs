n = int(input())
cnt = 0
# for i in range(n):
#     if i % 2 == 0:
#         for _ in range(n):
#             cnt += 1
#             print(cnt, end = " ") 
#     else:
#         for _ in range(n):
#             cnt += 2
#             print(cnt, end = " ")
#     print()

# 묶을 수 있는 건 묶어서 표현하기 (간단하게)
for i in range(n):
    for _ in range(n):
        if i % 2 == 0:
            cnt += 1
        else:
            cnt += 2
        print(cnt, end = " ")
    print()