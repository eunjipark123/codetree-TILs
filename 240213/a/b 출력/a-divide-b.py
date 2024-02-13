arr = input().split()
a, b = int(arr[0]), int(arr[1])

# 이상하게 나옴
# print(f"{a/b:.20f}")

d = a % b * 10
result = 0
result2 = str(a//b)+"."
lists = []

for _ in range(20):
    c = d // b
    result += 0.1 * c
    lists.append(str(c))
    d = d % b * 10

for i in lists:
    result2 += i

print(result2)