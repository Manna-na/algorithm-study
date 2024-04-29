import sys
input = sys.stdin.readline

n = int(input())
def check_strike(min, num):
    s = 0
    for j in range(3):
        if min[j] == num[j]:
            s += 1
    return s
def check_ball(min, num):
    b = 0
    for j in range(3):
        if min[j] in num and min[j] != num[j]:
            b += 1
    return b

check_array = []
for i in range(123, 988):
    i = str(i)
    if i[0] != i[1] and i[1] != i[2] and i[2] != i[0] and '0' not in i:
        check_array.append(i)

for _ in range(n):
    min, strike, ball = map(int, input().split())
    min = str(min)
    new_check = []
    for a in range(len(check_array)):
        now_num = str(check_array[a])
        now_strike = check_strike(now_num, min)
        now_ball = check_ball(now_num, min)
        if now_ball == ball and now_strike == strike:
            new_check.append(check_array[a])
    check_array = new_check
print(len(check_array))