# 입력값 받기
n = int(input())
strings = [input() for _ in range(n)]
letter = input()

# avg, len을 구할 변수 설정
cnt = 0
sum_val = 0

# list를 돌면서 조건에 해당하면 cnt, sum_val 추가하기 
for string in strings:
    if string[0] == letter:
        cnt += 1
        sum_val += len(string)
    
# 평균값 계산 
avg = sum_val / cnt

# 출력 
print(f"{cnt} {avg:.2f}")