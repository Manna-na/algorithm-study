import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
sum_ls = [i for i in ls]
for i in range(1, n):
    sum_ls[i] += sum_ls[i-1]
for _ in range(m):
    s, e = map(int, input().split())
    if s-1 == 0: print(sum_ls[e-1])
    else: print(sum_ls[e-1]-sum_ls[s-2])