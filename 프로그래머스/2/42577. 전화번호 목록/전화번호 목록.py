def solution(phone_book):
    answer = True
    dict = {}
    for p in phone_book:
        dict[p] = True
    for phone in phone_book:
        temp = ""
        for p in phone:
            temp += p
            if temp in dict and temp != phone:
                return False
    return answer