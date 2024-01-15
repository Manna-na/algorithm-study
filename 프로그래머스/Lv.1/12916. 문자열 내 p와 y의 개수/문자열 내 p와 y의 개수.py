def solution(s):
    answer = True
    p_num, y_num = 0, 0
    for s_val in s:
        if s_val == 'p' or s_val=='P':
            p_num+=1
        elif s_val == 'y' or s_val=='Y':
            y_num +=1
            
    if p_num != y_num:
        answer = False

    return answer