import sys
input = sys.stdin.readline

ans = 0
mushrooms = [int(input()) for _ in range(10)]
last_used = 0
for m in range(len(mushrooms)):
    ans += mushrooms[m]
    last_used = m
    if ans >= 100:
        break

if abs(ans-100) == abs(100-(ans-mushrooms[last_used])): print(max(ans, ans-mushrooms[last_used]))
elif abs(ans-100) < abs(100-(ans-mushrooms[last_used])): print(ans)
else: print(ans-mushrooms[last_used])