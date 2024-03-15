# 국영수 순으로 우선순위, 높은 학생부터 출력
n = int(input())

# 튜플로 풀이
scores = [tuple(input().split()) for _ in range(n)]
scores.sort(key=lambda x: (x[1], x[2], x[3]), reverse = True)


for name, kor, eng, math in scores:
    print(name, kor, eng, math)