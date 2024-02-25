strings = ['L', 'E', 'B', 'R', 'O', 'S']

letter = input()

if letter in strings:
    print(strings.index(letter))
else:
    print("None")

# word = ['A', 'P', 'P', 'L', 'E']

# idx = -1

# for i in range(len(word)):
#     if word[i] == 'L':
#         idx = i

# # 문자가 존재하지 않는 경우
# if idx == -1:
#     print("not exist")
# else:
#     print(idx)

# #enumerate는 인덱스와 리스트 원소를 튜플 쌍으로 보여준다.  
# print(list(enumerate(word)))

# idx = -1

# for i, char in enumerate(word):
#     if char == 'L':
#         idx = i

# print("not exist") if idx == -1 else print(idx)

# # in, not in
# if 'L' in word:
#     print("'L' is in list")
# if 'L' not in word:
#     print("'L' is not in list")

# print(word.index('L'))

# # 오류 발생 케이스 - 꼭 in, not in 부터 체크하기 
# # print(word.index('K'))

# if "K" in word:
#     print(word.index('K'))
# else:
#     print("nothing")

# if "l" in word:
#     print(word.index('L'))
# else:
#     print("nothing")

# # 문자가 여러 개 존재할 경우 

# if "P" in word:
#     print(word.index("P"))
# else:
#     print("nothing")