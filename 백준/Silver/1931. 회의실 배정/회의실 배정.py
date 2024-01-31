import sys
input = sys.stdin.readline

N = int(input())
conf = [tuple(map(int, input().split())) for _ in range(N)]
conf.sort(key=lambda x:(x[1], x[0]))
now = conf[0]
result = 1
for next in range(1, len(conf)):
    if now[1] <= conf[next][0]:
        now = conf[next]
        result += 1
print(result)