n = int(input())
char = 'A'

for i in range(n):
    for _ in range(i + 1):
        print(char, end = "")
        char = chr(ord(char) + 1)
    print()