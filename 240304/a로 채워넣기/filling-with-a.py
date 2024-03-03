string = input()
# 첫 번째 방법 (새롭게 만들어서 결합하기)
s = string[:1]+'a'+string[2:-2]+'a'+string[-1]
print(s)