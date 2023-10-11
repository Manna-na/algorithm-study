import sys

def solution(s):
    answer = ''
    list_s = list(s.split())
    min_value = sys.maxsize
    max_value = -sys.maxsize
    for i in list_s:
        if max_value < int(i) :
            max_value= int(i)
        if min_value > int(i):
            min_value=int(i)
            
            
    answer = str(min_value)+" "+str(max_value)
    return answer