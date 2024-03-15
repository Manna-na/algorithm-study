def solution(record):
    uid_nick_dict = {}
    for r in record:
        order = r.split()
        if order[0] == "Enter" or order[0] == "Change":
            uid_nick_dict[order[1]] = order[2]
    answer = []
    for r in record:
        order = r.split()
        if order[0] == "Enter":
            answer.append(uid_nick_dict[order[1]]+"님이 들어왔습니다.")
        elif order[0] == "Leave":
            answer.append(uid_nick_dict[order[1]]+"님이 나갔습니다.") 
    return answer