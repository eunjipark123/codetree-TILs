# # 입력값 받기 
# string = input()
# n = int(input())

# # 문자열의 길이 비교
# if n > len(string):
#     print(string[::-1])
# else:
#     # 끝에서부터 n개까지 출력 
#     for i in range(n):
#         print(string[::-1][i], end = "")


string = input()
n = int(input())

leng = len(string)
cnt = 0

for i in range(leng -1, -1, -1):
    if cnt => n:
        break
    print(string[i], end = "")
    cnt += 1