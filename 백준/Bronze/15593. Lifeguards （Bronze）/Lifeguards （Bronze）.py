N = int(input())
lifeguards = [0]*1000
work = [] # 근무 시간 저장할 리스트
for _ in range(N):
    start, end = map(int, input().split())
    work.append((start, end))
    for i in range(start, end):
        lifeguards[i] += 1

ans = 0
for w in work:
    start, end = w[0], w[1]
    for i in range(start, end): # 현재 근무 시간을 빼기
        lifeguards[i] -= 1
    time = 0    
    for lifeguard in lifeguards: # 커버 가능한 최대 시간 계산
        if lifeguard > 0:        
            time += 1
    ans = max(time, ans) # ans 갱신  
    for i in range(start, end): # 다시 현재 근무 시간 더해주기
        lifeguards[i] += 1  
        
print(ans)