# a, b = 9, 4
# # avg 단순 계산
# avg1 = (a + b) / 2

# # 리스트로 만들어서 돌리기 (비싼 함수)
# arr = [a, b]
# avg2 = sum(arr) / len(arr)


# print(avg1, avg2)



arr = input().split()
a = int(arr[0])
b = int(arr[1])

print(a + b, (a + b) / 2)