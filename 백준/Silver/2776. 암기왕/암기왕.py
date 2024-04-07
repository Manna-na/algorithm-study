import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    one = set(list(map(int, input().split())))
    m = int(input())
    two = list(map(int, input().split()))
    for t in two:
        if t in one:
            print(1)
        else:
            print(0)