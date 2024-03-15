# 클래스로 풀어보기 
class Student:
    def __init__(self, name, h, w):
        self.name = name 
        self.h = h
        self.w = w

    def print_it(self):
        print(self.name, self.h, self.w)


# 빈 리스트 생성
students = []

# 입력 받은 값을 리스트에 넣기
n = int(input())
for _ in range(n):
    name, h, w = input().split()
    students.append(Student(name, int(h), int(w)))

# 정렬 
students.sort(key=lambda x: x.h)

# 출력
for elem in students:
    elem.print_it()