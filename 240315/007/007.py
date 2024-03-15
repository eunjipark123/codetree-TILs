# class로 풀기

class Password:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
    
    def print_pw(self):
        print(f"secret code : {self.code}")
        print(f"meeting point : {self.place}")
        print(f"time : {self.time}")

pw1 = tuple(input().split())
code, place, time = pw1

pw1_instance = Password(code, place, time)
pw1_instance.print_pw()


# # tuple로 풀기
# code, place, time = tuple(input().split())
# print(f"secret code : {code}")
# print(f"meeting point : {place}")
# print(f"time : {time}")

# from datetime import datetime

# class Say:
#     def __init__(self):
#         print(f"[{datetime.now()}] __init__() method called")

#     def hello(self):
#         print(f"[{datetime.now()}] hello!")

# say = Say()
# say.hello()

# # class Student:
# #     def __init__(self, name, kor, eng, math):
# #         self.n = name
# #         self.k = kor
# #         self.e = eng
# #         self.m = math

# #     def score_avg(self):
# #         sum = self.k + self.e + self.k
# #         avg = sum / 3
# #         return avg

# #     def print_avg(self):
# #         print(f"{self.n}'s average score is : {self.score_avg():.2f}")
# # student1 = Student("Jack", 90, 80, 90)

# # print(student1.k)
# # print(student1.e)
# # print(student1.m)

# # student1.print_avg()