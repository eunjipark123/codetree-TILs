a, b, c = tuple(map(int, input().split()))

def min_value_creator(*args):
    return min(args)

print(min_value_creator(a, b, c))


# 개념 
# # 디폴트 값 지정해주기 
# # def add(a, b, c=0):
# #     return a + b + c

# # print(add(1, 3))


# # 인자 수와 무관하게 가져오기
# def add(*args):
#     print(f"args: {args}")

# add(1, 3, 5, 7)

# def add(*args):
#     return sum(args)

# print(add(1, 3, 5, 7))