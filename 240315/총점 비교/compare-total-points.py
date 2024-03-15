# tuple

n = int(input())
scores = [tuple(input().split()) for _ in range(n)]

scores.sort(key=lambda x: int(x[1]) + int(x[2]) + int(x[3]))

for name, a, b, c in scores:
    print(name, a, b, c)