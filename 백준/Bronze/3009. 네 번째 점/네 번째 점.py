import sys
input = sys.stdin.readline

dict_x = {}
dict_y = {}
for _ in range(3):
    x, y = map(int, input().split())
    dict_x[x] = dict_x.get(x, 0) + 1
    dict_y[y] = dict_y.get(y, 0) + 1

ans = ''
for k, v in dict_x.items():
    if v < 2:
        ans += str(k)
ans += ' '
for k, v in dict_y.items():
    if v < 2:
        ans += str(k)
print(ans)