users = []

for _ in range(5):
    code_name, score = tuple(input().split())
    users.append((code_name, int(score)))

min_idx = 0 
for i in range(1, 5):
    _, min_score = users[min_idx]
    _, curr_user_score = users[i]

    if min_score > curr_user_score:
        min_idx = i

code_name, score = users[min_idx]
print(code_name, score)