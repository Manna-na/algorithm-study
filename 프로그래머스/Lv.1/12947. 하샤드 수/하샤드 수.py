def solution(x):
    sum_x = 0
    list_x = list(str(x))
    for i in list_x:
        sum_x += int(i)
    if x % sum_x ==0:
        return True
    else:
        return False
