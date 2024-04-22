import sys
input = sys.stdin.readline

geminis = list(map(int, input().split()))
startlink = list(map(int, input().split()))


geminis_sum, startlink_sum = 0, 0
geminis_win = False
count = 0

for i in range(9):
    if geminis[i] + startlink[i] == 0:
        continue
    geminis_sum += geminis[i]
    # print((i+1),"회 초 - geminis :", geminis_sum, "startlink :", startlink_sum)
    if geminis_sum > startlink_sum:
        # geminis_win = True
        count += 1
    startlink_sum += startlink[i]
    # print((i + 1), "회 말 - geminis :", geminis_sum, "startlink :", startlink_sum)

if geminis_sum < startlink_sum and count > 0:
    print('Yes')
else:
    print('No')