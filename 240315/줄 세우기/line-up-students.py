# tuple로 풀기

n = int(input())

students = []
for k in range(1, n+1):
    h, w = map(int, input().split())
    students.append((k, h, w))

students.sort(key=lambda x: (-x[1], -x[2], -x[0]))

for k, h, w in students:
    print(h, w, k)