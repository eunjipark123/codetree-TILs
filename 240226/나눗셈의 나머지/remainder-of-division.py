inputs = list(map(int, input().split()))
a, b = inputs[0], inputs[1]
rest = [0] * b

while a > 1:
    a //= b
    rest[a % b] += 1

rest_sum = 0

for i in rest:
    rest_sum += i**2

print(rest_sum)