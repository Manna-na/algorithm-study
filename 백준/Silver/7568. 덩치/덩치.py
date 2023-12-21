import sys
input = sys.stdin.readline
n = int(input())
peoples = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j :
            if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
                rank += 1
    print(rank, end=" ")