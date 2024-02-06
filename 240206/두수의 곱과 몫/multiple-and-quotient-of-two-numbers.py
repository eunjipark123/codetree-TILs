arr = input().split()
a = int(arr[0])
b = int(arr[1])

print(f"{a} * {b} = {a * b}")
# 실수로 출력되어 자꾸 틀림 
# print(f"{a} / {b} = {a // b}")
c = int(a / b)
print(f"{a} / {b} = {c}")