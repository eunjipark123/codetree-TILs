n = int(input())

# in으로 해결 
# if n in (1, 3, 5, 7, 8, 10, 12):
#     print(31)
# elif n in (4, 6, 9, 11):
#     print(30)
# else:
#     print(28)

# 짝수 홀ㅅ로 해결
if n == 2:
    print(28)
elif n <= 7:
    if n % 2 == 1:
        print(31)
    else:
        print(30)
else:
    if n % 2 == 1:
        print(30)
    else:
        print(31)