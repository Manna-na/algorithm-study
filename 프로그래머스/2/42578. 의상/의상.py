# 1. 의상을 해시테이블로 구성
# 2. 의상 개수 + 1(선택하지 않을 경우) 를 종류별로 count 한 뒤 곱하기
# 3. 아무것도 선택하지 않을 경우 -1


def solution(clothes):
    clothes_hash = {}
    for c in clothes:
        name, type = c[0], c[1]
        if type in clothes_hash:
            clothes_hash[type].append(name)
        else:
            clothes_hash[type] = [name]

    answer = 0
    for i, v in clothes_hash.items():
        choice_count = len(v)+1
        if answer == 0:
            answer += choice_count
        else:
            answer *= choice_count
    return answer-1