# 별의 갯수
# 3줄 -> 첫 번째 줄은 공백이 2개, 두번째 줄은 공백이 1개, 세 번재 줄은 공백이 0개
# 5줄 -> 첫 번째 줄은 공백이 4개, 두 번재 줄은 공백이 3개,, 

# n = 5

# for i in range(5):
#     for _ in range(n - i - 1):
#         print(" ", end = "")
#     for _ in range(2 * i + 1):
#         print("*", end = "")
#     print()

n = int(input())

for i in range(n):
    for _ in range(1, i + 1):
        print(" ", end = " ")

    for _ in range(2 * (n - i)-1):
        print("*", end = " ")
    
 
    print()