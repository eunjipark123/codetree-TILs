arr = input().split()
a, b = int(arr[0]), int(arr[1])

# 변수 선언
sum_ab = 0

for i in range (a, b + 1):
    sum_ab += i

print(sum_ab)