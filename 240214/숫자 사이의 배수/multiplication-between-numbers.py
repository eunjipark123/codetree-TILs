arr = input().split()
a, b = int(arr[0]), int(arr[1])
cnts = 0
sums = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        cnts += 1
        sums += i

print(f"{sums} {sums/cnts:.1f}")