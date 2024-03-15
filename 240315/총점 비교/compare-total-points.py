# class
class Score:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def print_score(self):
        print(self.name, self.a, self.b, self.c)

# 리스트 채우기
n = int(input())
scores = []

for _ in range(n):
    name, a, b, c = input().split()
    scores.append(Score(name, int(a), int(b), int(c)))

# 정렬 
scores.sort(key=lambda x: x.a + x.b + x.c)

# 출력 
for score in scores:
    score.print_score()