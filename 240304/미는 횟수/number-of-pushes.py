a = input()
b = input()

n = 0

while a != b:
    a = a[-1] + a[:-1]
    n += 1

print(n)