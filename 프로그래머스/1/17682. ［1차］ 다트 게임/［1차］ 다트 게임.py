import math
def solution(dartResult):
    answer = 0
    bonus = {"S": 1, "D": 2, "T":3}
    options = {"*":2, "#":-1}
    idx = 0
    before_score = 0   
    while idx < len(dartResult):
        now = 0
        if dartResult[idx:idx+2] == "10":
            now = 10
            idx += 2
        elif dartResult[idx] in [str(i) for i in range(0, 10)]:
            now = int(dartResult[idx])
            idx += 1
        if dartResult[idx] in bonus.keys():
            temp_now = int(math.pow(now, bonus[dartResult[idx]]))
            now = temp_now
            idx += 1
        if idx < len(dartResult) and dartResult[idx] in options.keys():
            if dartResult[idx] == "*":
                answer -= before_score
                answer += before_score * 2
            now *= options[dartResult[idx]]
            idx += 1
        answer += now
        before_score = now
            
    return answer