n, k, t = input().split()
n = int(n)
k = int(k)
lent = len(t)
arr = []

# 문자 일치 확인 -> 일치하면 빈리스트에 추가
for _ in range(n):
    string = input()
    if len(string) >= lent and string[:lent] == t:
        arr.append(string)

# 빈 리스트를 순서대로 정렬
arr = sorted(arr)

# k 번째 단어 출력
print(arr[k-1])