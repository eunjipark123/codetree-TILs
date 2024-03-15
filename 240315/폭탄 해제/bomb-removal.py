# class 정의
class Bombs:
# constructor 정의
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

# 내부 메서드 정의 (출력 메서드)
    def print_bombs(self):
        print(f"code : {self.code}")
        print(f"color : {self.color}")
        print(f"second : {self.sec}")

# 입력값 받기
code, color, sec = input().split()

# 클래스에 넣기
b1 = Bombs(code, color, sec)

# 메서드 출력
b1.print_bombs()