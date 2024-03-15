user = input().split()
user_id, user_lv = user
user_lv = int(user_lv)

class User:
    def __init__(self, user_id = 'codetree', user_lv = 10):
        self.user_id = user_id
        self.user_lv = user_lv

user0 = User()
user1 = User(user_id, user_lv)

print(f"user {user0.user_id} lv {user0.user_lv}")
print(f"user {user1.user_id} lv {user1.user_lv}")