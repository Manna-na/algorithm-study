import sys
input = sys.stdin.readline

h, w = map(int, input().split())
array=[['' for _ in range(w)] for _ in range(h)]
for i in range(h):
    str =input().strip()
    for j in range(w):
        array[i][j] = str[j]

ans = [[-1 for _ in range(w)] for _ in range(h)]

for i in range(h):
    now_c = -1
    for j in range(w):
        if array[i][j] =='c':
            now_c = j
            ans[i][j] = 0
        elif now_c > -1:
            ans[i][j] = j-now_c

for i in range(h):
    for j in range(w):
        print(ans[i][j], end= ' ')
    print()