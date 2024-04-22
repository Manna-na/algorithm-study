import sys
input = sys.stdin.readline

geminis = list(map(int, input().split()))
startlink = list(map(int, input().split()))

isFlag = False
geminis_sum, startlink_sum = 0, 0
geminis_win = False
for i in range(9):
    if geminis[i] + startlink[i] == 0:
        continue
    geminis_sum += geminis[i]
    if geminis_sum > startlink_sum:
        geminis_win = True

    startlink_sum += startlink[i]

if geminis_sum < startlink_sum and geminis_win:
    print('Yes')
else:
    print('No')