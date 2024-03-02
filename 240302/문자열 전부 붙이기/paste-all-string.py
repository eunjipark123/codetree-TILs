# n = int(input())
# string = ""

# for _ in range(n):
#     string += input()


# print(string)

n = int(input())

string = [
    input()
    for _ in range(n)
]

str_all = ""

for s in string:
    str_all += s

print(str_all)