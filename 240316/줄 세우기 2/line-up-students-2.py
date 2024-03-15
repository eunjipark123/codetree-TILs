class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

    def print_student(self):
        print(self.h, self.w, self.num)


# 입력 받기 
n = int(input())
students = []

for num in range(1, n + 1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, num))

students.sort(key=lambda x: (x.h, -x.w))

for student in students:
    student.print_student()