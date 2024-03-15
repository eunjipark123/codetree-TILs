# tuple로 풀어보기

n = int(input())

students  = []
for num in range(1, n + 1):
    x, y = tuple(map(int, input().split()))
    
    # 거리 계산
    d = abs(x - 0) + abs(y - 0)
    # 번호와 거리만 추가
    students.append((num, d))

# 거리 기준으로 정렬 
students.sort(key=lambda x: x[1])

# 번호 출력
for num, _ in students:
    print(num)