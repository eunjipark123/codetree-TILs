num = input().split()
a = int(num[0])
b = int(num[1])

while a<=b:
    if a%2 == 1:
        print(a, end=" ")
        a *= 2
    else:
        print(a, end=" ")
        a += 3