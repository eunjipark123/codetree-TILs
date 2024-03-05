m, d = tuple(map(int, input().split()))

def date_by_month_2021(m):
    if m in (1, 3, 5, 7, 8, 10, 12):
        date = [i for i in range(1, 32)]
    
    elif m == 2:
        date = [i for i in range(1, 29)]
    
    else:
        date = [i for i in range(1, 31)]

    return date


def is_date_exsist_in_2021(m, d):
    if d in date_by_month_2021(m):
        answer = 'Yes'
    else:
        answer = 'No'

    return answer

print(is_date_exsist_in_2021(m, d))