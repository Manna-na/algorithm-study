import sys
input = sys.stdin.readline
# 최대를 찾고 왼쪽, 오른쪽 탐험하자
n = int(input())
polygons = []
for _ in range(n):
    x, y = map(int, input().split())
    polygons.append([x, y])

max_size = max(polygons, key=lambda x:x[1])
polygons.sort(key=lambda x:(x[0],x[1]))
max_index = polygons.index(max_size)
ans = polygons[max_index][1]
now_height = 0
# 오른쪽 부터
for r in range(max_index):
    if polygons[r][1] > now_height:
        now_height = polygons[r][1]
    ans += (polygons[r+1][0] - polygons[r][0]) * now_height

now_height = 0
# 왼쪽 탐험
for l in range(len(polygons)-1, max_index, -1):
    if polygons[l][1] > now_height:
        now_height = polygons[l][1]
    ans += (polygons[l][0] - polygons[l-1][0]) * now_height
print(ans)