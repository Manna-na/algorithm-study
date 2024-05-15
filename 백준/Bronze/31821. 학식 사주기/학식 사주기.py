import sys
input = sys.stdin.readline

n = int(input())
menu = [int(input()) for _ in range(n)]
m = int(input())
ans = 0
for i in range(m):
    student = int(input())
    ans += menu[student-1]

print(ans)