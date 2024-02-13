cnt_3 = 0
cnt_5 = 0

# 지저분한 방법이군..! 
# for _ in range(10):
#     n = int(input())
#     if n % 3 == 0 and n % 5 == 0:
#         cnt_3 += 1
#         cnt_5 += 1
#     elif n % 3 == 0:
#         cnt_3 += 1
#     elif n % 5 == 0:
#         cnt_5 += 1

# print(cnt_3, cnt_5)
    
for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        cnt_3 += 1
    # 독립되어 작용하므로 이렇게 써도 되는구나.. 
    if n % 5 == 0:
        cnt_5 += 1
    
print(cnt_3, cnt_5)