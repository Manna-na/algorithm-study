import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))

sum_ls = [i for i in ls]
for i in range(1, n):
    sum_ls[i] += sum_ls[i-1]

max_k = sum_ls[k-1]
for i in range(1, n-k+1):
    now_k = sum_ls[i+k-1] - sum_ls[i-1]
    if now_k > max_k:
        max_k = now_k

print(max_k)