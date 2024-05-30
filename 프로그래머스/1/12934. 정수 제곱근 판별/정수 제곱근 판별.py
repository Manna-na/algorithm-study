import math

def solution(n):
    sqrt_num = n**0.5
    if math.ceil(sqrt_num)==math.floor(sqrt_num):
        return (int(sqrt_num)+1)**2
    else:
        return -1
