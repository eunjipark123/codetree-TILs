n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        # print("친근한 수입니당")
        continue
    # print("친근한 수가 아니네요")
    cnt += 1

# print(f"최종 합계 : {cnt}")
print(cnt)