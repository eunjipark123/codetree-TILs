n = int(input())
x = 0

# while n > 1:
#     n //= 2
#     x += 1

# print(x)

prod = 1

while True:
    if n == prod:
        break

    prod *= 2
    x += 1

print(x)