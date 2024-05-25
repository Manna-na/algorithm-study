def solution(number, limit, power):
    ans = 0
    
    for i in range(1, number+1):
        # 약수 개수 세기
        cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j != i // j:
                    cnt += 1
            # 공격력 제한수치 넘는지 확인
            if cnt > limit:
                ans += power
                break
        else:
            ans += cnt
    
    return ans
