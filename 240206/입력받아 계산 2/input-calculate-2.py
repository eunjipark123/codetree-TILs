# 공백을 사이에 두고 입력
# split() 함수를 이용한다. 

# a = input()
# # 리스트 형태로 출력
# print(a.split())

# arr = [5, 6, 10]
# print(f"First element is arr[0]")
# print(f"Second element is arr[1]")
# print(f"Last element is arr[2]")

# print(f"{a[0]}은(는) 첫 번째로 입력된 녀석입니다. ")

# a = input().split()
# multi = int(a[0]) * int(a[1])
# print(multi)

# 해설 방법
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 출력
print(a * b)