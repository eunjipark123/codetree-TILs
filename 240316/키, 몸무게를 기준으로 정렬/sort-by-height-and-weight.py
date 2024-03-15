n = int(input())

class StudentInfo:
    def __init__(self, name, h, w):
        self.name = name 
        self.h = h
        self.w = w

students = []
for _ in range(n):
    name, h, w = input().split()
    h, w = int(h), int(w)
    students.append(StudentInfo(name, h, w))

students.sort(key=lambda x: (x.h, -x.w))

for student in students:
    print(student.name, student.h, student.w)