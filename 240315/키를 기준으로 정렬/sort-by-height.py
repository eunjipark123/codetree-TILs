n = int(input())

# 튜플로 풀어보기
students = [tuple(input().split()) for _ in range(n)]
students.sort(key=lambda x: x[1])

for name, h, w in students:
    print(name, h, w)