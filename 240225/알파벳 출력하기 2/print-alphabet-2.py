n = int(input())
char = 'A'
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n - i):
        print(char, end = " ")
        if char == "Z":
            char = 'A'
        else:
            char = chr(ord(char) + 1)
    print()