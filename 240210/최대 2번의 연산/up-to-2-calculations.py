a = int(input())

if a % 2 == 0:
    a /= 2
else:
    a = (a + 1)/2

if a % 2 == 1:
    a = (a + 1)/2
else:
    a /= 2

print(int(a))