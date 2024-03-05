# 입력
a = input()

def judge_more_than_2_alpha(a):
    if len(a) == 1:
        return False
    
    for i in range(1, len(a)):
        if a[i] not in a[:i]:
            return True    
    
    return False 

    
if judge_more_than_2_alpha(a):
    print('Yes')
else:
    print('No')