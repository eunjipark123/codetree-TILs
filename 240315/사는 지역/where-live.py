# 사전순, 이름이 가장 뒤에 있는 사람, 클래스 사용
class UserInfo:
    def __init__(self, name, digit, region):
        self.name = name
        self.digit = digit
        self.region = region

    def print_userinfo(self):
        print(f"name {self.name}")
        print(f"addr {self.digit}")
        print(f"city {self.region}")

n = int(input())

users = []
for _ in range(n):
    name, digit, region = input().split()
    users.append(UserInfo(name, digit, region))


max_idx = 0

for i in range(1, n):
    if users[max_idx].name < users[i].name:
        max_idx = i

users[max_idx].print_userinfo()