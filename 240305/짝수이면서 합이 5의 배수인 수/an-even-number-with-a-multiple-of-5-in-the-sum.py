# 문제
n = int(input())

def is_even_multiple5(n):
    return n % 2 == 0 and (n//10 + n % 10) % 5 == 0

if is_even_multiple5(n):
    print("Yes")
else:
    print("No")


# 개념
# def is_magic_number(n):
#     return n % 3 != 0 and n % 5 == 0


# cnt = 0
# for i in range(1, 101):
#     if is_magic_number(i):
#         cnt += 1

# print(cnt)