def solution(a, b):
    answer = 0
    list_zip = [ a*b for a, b in list(zip(a, b)) ]
    for num in list_zip:
        answer += num
    return answer



# def solution(a, b):

#     return sum([x*y for x, y in zip(a,b)])