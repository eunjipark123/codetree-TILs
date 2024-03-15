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


users = sorted(users, key = lambda x: x.name, reverse = True)
users[0].print_userinfo()