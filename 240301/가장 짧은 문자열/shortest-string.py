a = input()
b = input()
c = input()

a = len(a)
b = len(b)
c = len(c)

if a >= b >= c:
    print(a - c)
elif a >= c >= b:
    print(a - b)
elif b >= a >= c:
    print(b - c)
elif b >= c >= a:
    print(b - a)
elif c >= a >= b:
    print(c - b)
elif c >= b >= a:
    print(c - a)