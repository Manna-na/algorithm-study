def solution(a, b):
    answer = ''
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_str = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day_sum = [0]
    for i in range(1, len(day)):
        day_sum.append(day_sum[i-1] +day[i])
    answer = day_str[(day_sum[a-1]+b)%7]
    return answer