n = int(input())
ords = 65

for _ in range(n):
    for _ in range(n):
        print(f"{chr(ords)}", end = "")
        ords += 1
    print()