import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
for i in range(n-3):
    if ls[0] > ls[n-1]:
        ls[0] -= 1
    else:
        ls[n-1] -= 1
ls[0] = ls[0]-1
ls[n-1] = ls[n-1]-1
if ls[0] > ls[n-1]:
    print(ls[0])
else:
    print(ls[n-1])