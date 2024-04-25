import sys
input = sys.stdin.readline

a, b, c, d, e, f =map(int, input().split())
x, y = (c*e-b*f)//(a*e-b*d), (a*f-c*d)//(a*e-b*d)
print(x, y)