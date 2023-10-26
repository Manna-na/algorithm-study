def solution(food):
    # 몫이 1이상이어야 해
    # 문자열로 처리
    # 물은 중간에
    
    answer = ''
    for index, num in enumerate(food):
        if num // 2  >= 1:
            answer += (str(index) * (num//2)) 
    answer += '0' + answer[::-1]
            
    return answer