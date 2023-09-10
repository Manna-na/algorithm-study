N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

# 연산 횟수
count = 0

# 행렬을 변환하는 연산(원소 뒤집기)
def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

# A와 B가 같으면 True, 다르면 False 리턴
def compare():
    for i in range(N):
        for j in range(M):
            if N - 3 < i or M - 3 < j:
                if A[i][j] != B[i][j]:
                    return False
    return True

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            count += 1

if compare():
    print(count)
else:
    print(-1)