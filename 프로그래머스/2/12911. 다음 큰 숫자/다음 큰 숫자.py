def solution(n):
    answer = 0
    next_num = n
    while True:
        number = bin(n).replace("0b", "")
        next_num += 1
        next = bin(next_num).replace("0b", "")
        if number.count("1") == next.count("1"):
            answer = next_num
            break
    return answer