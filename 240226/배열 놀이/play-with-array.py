# # 첫 번째 줄 : n, q
# inputs = input().split()
# n , q = int(inputs[0]), int(inputs[1])

# # 두 번째 줄 : 원소
# elements = list(map(int, input().split()))

# # 세 번째 줄 : 질의
# for _ in range(q):
#     quest = list(map(int, input().split()))

#     if quest[0] == 1:
#         a = quest[1]
#         print(elements[a-1], end = "")
    
#     elif quest[0] == 2:
#         a = quest[1]
#         if a in elements:
#             print(elements.index(a)+1, end = "")
#         else:
#             print(0, end = "")
    
#     else:
#         a, b = quest[1], quest[2]
#         for i in range(a - 1, b):
#             print(elements[i], end = " ")
#     print()        
    
# 정수 n과 q을 입력받습니다.
n, q = tuple(map(int,input().split()))
	
# arr를 입력받습니다.
arr = list(map(int, input().split()))

# q개의 질의를 수행합니다.
for _ in range(q):
	# 질의를 입력받습니다.
	quest = list(map(int, input().split()))
	
	# 몇번째 질의인지 확인합니다.
	if quest[0] == 1:
		# a번째 원소를 출력합니다.
		a = quest[1]
		print(arr[a - 1])
		
	elif quest[0] == 2:
		# 배열에 숫자 a가 있다면 가장 index가 작은 원소가 몇번째인지 출력합니다. 없다면 0을 출력합니다.
		a = quest[1]
		idx = -1
		if a in arr:
			idx = arr.index(a)
		print(idx + 1)
		
	else:
		# a번째 원소부터 b번째 원소까지 공백을 사이에 두고 출력합니다.
		a = quest[1]
		b = quest[2]
		for i in range(a - 1, b):
			print(arr[i], end=" ")
		print()