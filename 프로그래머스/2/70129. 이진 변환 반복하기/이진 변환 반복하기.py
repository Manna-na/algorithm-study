
def solution(s):
    answer = []
    cnt = 0
    cnt_zero = 0
    while len(s) > 1:
        cnt_zero += s.count("0")
        s = isFin(s)
        cnt += 1
    answer.append(cnt)
    answer.append(cnt_zero)
    return answer

def isFin(s):
    s = s.replace("0", "")
    num_len = len(s)
    s = bin(num_len).replace("0b", "")
    return s