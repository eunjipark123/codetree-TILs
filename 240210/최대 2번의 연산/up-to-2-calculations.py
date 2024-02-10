a = int(input())

if a % 2 == 0:
    b = a / 2
else:
    b = (a + 1)/2

if b % 2 == 1:
    a = (b + 1)/2
else:
    a = b / 2

print(int(a))