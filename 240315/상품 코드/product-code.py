class Products:
    def __init__(self, name="", code=0):
        self.name = name
        self.code = code
    
    def print_it(self):
        print(f"product {self.code} is {self.name}")

# 초기화된 값 
p1 = Products()
p1.name = "codetree"
p1.code = 50

# 입력값 받기
name, code = input().split()
p2 = Products(name, int(code))

# 출력
p1.print_it()
p2.print_it()