N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
res = 0
for i in range(len(A)):
    max_B = max(B)
    res += max_B*A[i]
    B.remove(max_B)

print(res)