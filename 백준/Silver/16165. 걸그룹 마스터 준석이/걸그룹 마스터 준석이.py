import sys
input = sys.stdin.readline

N, M = map(int, input().split())
group = {}
for i in range(N):
    group_name = input().rstrip()
    group_number = int(input())
    members = [input().rstrip() for _ in range(group_number)]
    members.sort()
    group[group_name] = members

for i in range(M):
    name = input().rstrip()
    type = int(input().rstrip())
    for i, v in group.items():
        if type == 0:
            if i == name:
                print("\n".join(v))
        else: # type == 1
            if name in group[i]: # 멤버 이름이 group[i]에 들어있을때
                print(i)
