import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
ans = deque([])
for _ in range(N):
    order = input().strip()
    if order[:2] == "pu":
        order, n = order.split()
        if order == "push_front":
            ans.appendleft(int(n))
        elif order=="push_back":
            ans.append(int(n))
    elif order[:3] == "pop":
        if len(ans) == 0:
            print(-1)
        elif order=="pop_front":
            print(ans.popleft())
        elif order=="pop_back":
            print(ans.pop())
    elif order == "size":
        print(len(ans))
    elif order == "empty":
        if len(ans) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(ans) == 0:
            print(-1)
        else:
            print(ans[0])
    else:
        if len(ans) == 0:
            print(-1)
        else:
            print(ans[-1])