# class로 풀기

class StudentInfo:
    def __init__(self, h, w, k):
        self.h = h
        self.w = w
        self.k = k

    def print_info(self):
        print(self.h, self.w, self.k)


n = int(input())
students = []

for k in range(1, n + 1):
    h, w = map(int, input().split())
    students.append(StudentInfo(h, w, k))

students.sort(key=lambda x: (-x.h, -x.w, x.k))

for student in students:
    student.print_info()