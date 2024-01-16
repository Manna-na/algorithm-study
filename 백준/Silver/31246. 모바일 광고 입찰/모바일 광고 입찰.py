import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ai, bi =[], []
for i in range(N):
    A, B = map(int, input().split())
    ai.append(A)
    bi.append(B)

answer = 0
bid = []
for i in range(N):
    if ai[i] < bi[i]:
        bid.append(bi[i] - ai[i])
    else:
        answer += 1

if answer >= K:
    print(0)
else:
    bid.sort()
    total = answer
    for i in bid:
        total += 1
        if total >= K:
            print(i)
            break

