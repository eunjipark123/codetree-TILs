# 입력값 받기 
string = input()
n = int(input())

# 끝에서부터 n개까지 출력 
for i in range(n):
    print(string[::-1][i], end = "")