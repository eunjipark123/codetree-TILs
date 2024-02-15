# 합성수 : 1보다 커야 하고, 소수가 아니어야 함

n = int(input())
exists = False

for i in range(2, n):
    if n % i == 0:
        exists = True
        break

print("C") if exists == True else print("N")