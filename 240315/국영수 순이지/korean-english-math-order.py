# Class로 풀이
# Class 정의
class Score:
    def __init__(self, name, k, e, m):
        self.name = name
        self.k = k
        self.e = e
        self.m = m

    def print_score(self):
        print(self.name, self.k, self.e, self.m)

# 입력값 받기
n = int(input())

# 빈 리스트 생성
scores = []

# 리스트에 인스턴스 넣기
for i in range(n):
    name, k, e, m = input().split()
    scores.append(Score(name, int(k),int(e), int(m)))

# 정렬
scores.sort(key=lambda x: (-x.k, -x.e, -x.m))

# 출력
for elem in scores:
    elem.print_score()