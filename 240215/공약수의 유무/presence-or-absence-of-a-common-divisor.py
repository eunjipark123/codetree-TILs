arr = input().split()
a, b = int(arr[0]), int(arr[1])

exists = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % 1 == 0:
        exists = True
        break

print(1) if exists == True else print(0)