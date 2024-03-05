y, m, d = tuple(map(int, input().split()))
def is_leap_year(y):
    if y % 4 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 400 == 0:
        return True
    return False

def last_date_month_by_year(y, m):
    if m == 2:
        if is_leap_year(y):
            return 29
        return 28
    if m in (4, 6, 9, 11):
        return 30
    return 31

def define_seasons(m):
    if m >= 3 and m < 6:
        return 'Spring'
    if m >= 6 and m < 9:
        return 'Summer'
    if m >= 9 and m < 12:
        return 'Fall'    
    else:
        return 'Winter'

def date_existence_with_seasons(y, m, d):
    if d <= last_date_month_by_year(y, m):
        return define_seasons(m)
    
    return -1

print(date_existence_with_seasons(y, m, d))