import sys
input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

selected = [0] * 7
def recur(cur, start):
    if cur == 7:
        if sum(selected) == 100:
            for i in range(7):
                print(selected[i])
            exit()
        return
    for i in range(start, 9):
        selected[cur] = dwarfs[i]
        recur(cur + 1, i+1)
recur(0, 0)