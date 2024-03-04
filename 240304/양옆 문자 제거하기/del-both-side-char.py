string = input()
# list를 이용한 방법
string = list(string)
string.pop(1)
string.pop(-2)
string = "".join(string)
print(string)

# # slicing을 이용한 방법
# string = string[:1] + string[2:-2] + string[-1:]
# print(string)


# 기본 개념
# # list를 이용한 방법
# s = 'baknana'
# arr = list(s)
# arr.pop(2)
# s = "".join(arr)
# print(s)

# # slicing을 이용한 방법 
# s = 'baknana'
# print(s)
# print()
# s = s[:2] + s[3:]
# print(s)