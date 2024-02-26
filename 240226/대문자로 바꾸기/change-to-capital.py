n = 5

b = ([list(input().split()) for _ in range(n)])

for row in b:
    for i in row:
        print(chr(ord(i) + (ord('A') - ord('a'))), end = " ")
    print()